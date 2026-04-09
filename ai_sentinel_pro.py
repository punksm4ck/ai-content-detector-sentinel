#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║    ██████╗ ██╗    ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗  ║
║   ██╔══██╗██║    ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║  ║
║   ███████║██║    ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║  ║
║   ██╔══██║██║    ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║  ║
║   ██║  ██║██║    ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗ ║
║   ╚═╝  ╚═╝╚═╝    ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝ ║
║                                                                                  ║
║                    AI SENTINEL PRO  ·  Enterprise Edition v3.0                  ║
║                                                                                  ║
║  ▸ Zero-UI full-screen overlay · click-through watermark badge engine           ║
║  ▸ Multi-engine detection: Sightengine + local hash + region entropy scoring    ║
║  ▸ Adaptive motion segmentation with multi-region tracking                      ║
║  ▸ Perceptual hash deduplication with bloom-filter acceleration                 ║
║  ▸ Configurable confidence blending: burst average / max / ensemble vote        ║
║  ▸ Full multi-monitor awareness + per-monitor exclusion zones                   ║
║  ▸ Screenshot snapshot archive with configurable retention                      ║
║  ▸ Configurable badge styles: circle, shield, ribbon, banner                    ║
║  ▸ Real-time heatmap of detection density across screen                         ║
║  ▸ Allowlist / Denylist URL + process-name rules                                ║
║  ▸ Session reports: PDF + CSV + JSON export with charts                         ║
║  ▸ Webhook alerts: Slack / Teams / custom HTTP POST                             ║
║  ▸ Confidence trend sparklines + hourly heatmap in dashboard                    ║
║  ▸ Live API rate limiter + cost estimator                                       ║
║  ▸ Encrypted credential storage (Fernet)                                        ║
║  ▸ Cross-platform: macOS / Linux / Windows + XDG/GNOME/KDE/launchd/registry    ║
╚══════════════════════════════════════════════════════════════════════════════════╝
"""

# ─── Standard Library ──────────────────────────────────────────────────────────
import sys, io, os, csv, json, time, math, signal, hashlib, logging
import datetime, threading, traceback, subprocess, collections, base64
import sqlite3, re, shutil, uuid, queue, copy, struct, zlib
from pathlib import Path
from typing import Optional, List, Dict, Tuple, Callable, Any
from dataclasses import dataclass, field, asdict
from functools import lru_cache
from contextlib import contextmanager

# ─── Third-party ───────────────────────────────────────────────────────────────
import requests
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter, ImageStat
import mss

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QSystemTrayIcon, QMenu, QAction, QDialog, QLineEdit,
    QFormLayout, QDialogButtonBox, QSlider, QComboBox,
    QCheckBox, QSpinBox, QMessageBox, QFileDialog,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QTextEdit, QFrame, QTabWidget, QProgressBar,
    QPushButton, QGraphicsOpacityEffect, QGroupBox,
    QListWidget, QListWidgetItem, QDoubleSpinBox,
    QSplitter, QScrollArea, QStackedWidget, QButtonGroup,
    QRadioButton, QSizePolicy, QAbstractItemView,
)
from PyQt5.QtCore import (
    Qt, QTimer, QThread, QObject, pyqtSignal,
    QPropertyAnimation, QEasingCurve, QRect, QPoint, QSize,
    QRectF, QPointF, QSequentialAnimationGroup, QPauseAnimation,
    QParallelAnimationGroup, QVariantAnimation,
)
from PyQt5.QtGui import (
    QIcon, QPixmap, QPainter, QColor, QFont, QPen,
    QBrush, QLinearGradient, QRadialGradient, QPolygon,
    QFontDatabase, QPainterPath, QPolygonF, QConicalGradient,
    QFontMetrics, QCursor,
)

signal.signal(signal.SIGINT, signal.SIG_DFL)

# ══════════════════════════════════════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════════════════════════════════════
APP_NAME     = "AI Sentinel Pro"
APP_VERSION  = "3.0.0"
APP_BUILD    = "2025.enterprise"

# Detection defaults
AI_THRESHOLD_DEFAULT = 0.82
BADGE_HOLD_MS        = 6000    # ms badge stays solid
BADGE_FADE_MS        = 1800    # ms fade animation
MOTION_DEBOUNCE      = 280     # ms between motion ticks
DEDUP_TTL            = 90      # s before re-analyzing same hash
MAX_REGIONS          = 20      # max simultaneous badges
MAX_WORKERS          = 4       # API concurrency

# Cost estimation (Sightengine free: 500/month, $0.001/call thereafter)
COST_PER_CALL_USD    = 0.001
FREE_CALLS_PER_MONTH = 500

# Screenshot archive
SNAPSHOT_QUALITY     = 82      # JPEG quality for archived snaps
MAX_SNAPSHOTS        = 500     # max archived screenshots

# Heatmap
HEATMAP_CELL_PX      = 80      # screen cell size for density heatmap
HEATMAP_DECAY        = 0.92    # per-tick decay

# ══════════════════════════════════════════════════════════════════════════════
#  PATHS
# ══════════════════════════════════════════════════════════════════════════════
CONFIG_DIR    = Path.home() / ".config" / "ai_sentinel_pro"
SNAPSHOT_DIR  = CONFIG_DIR / "snapshots"
EXPORT_DIR    = CONFIG_DIR / "exports"
for _d in (CONFIG_DIR, SNAPSHOT_DIR, EXPORT_DIR):
    _d.mkdir(parents=True, exist_ok=True)

CONFIG_FILE   = CONFIG_DIR / "config.json"
DB_FILE       = CONFIG_DIR / "detections.db"
SYSLOG_FILE   = CONFIG_DIR / "sentinel.log"
ALLOWLIST_FILE= CONFIG_DIR / "allowlist.json"
RULES_FILE    = CONFIG_DIR / "rules.json"

# ══════════════════════════════════════════════════════════════════════════════
#  LOGGING
# ══════════════════════════════════════════════════════════════════════════════
_log_handlers = [
    logging.FileHandler(SYSLOG_FILE, encoding="utf-8"),
    logging.StreamHandler(sys.stdout),
]
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    handlers=_log_handlers,
)
log = logging.getLogger("sentinel")

# ══════════════════════════════════════════════════════════════════════════════
#  DESIGN SYSTEM
# ══════════════════════════════════════════════════════════════════════════════
C = {
    # Base
    "bg":        "#060610",
    "bg2":       "#09091a",
    "surface":   "#0d0d20",
    "surface2":  "#12122a",
    "border":    "#1c1c35",
    "border2":   "#252545",
    "muted":     "#2a2a50",
    # Text
    "text":      "#c8d4f0",
    "text2":     "#8090b8",
    "sub":       "#4a5280",
    "dim":       "#2a3060",
    # Accent
    "accent":    "#5b6aff",
    "accent2":   "#7c88ff",
    "accent_d":  "#3a47cc",
    # Semantic
    "ok":        "#00e08a",
    "ok_d":      "#00a060",
    "warn":      "#ffa830",
    "warn_d":    "#cc7a10",
    "danger":    "#ff2060",
    "danger_d":  "#cc0040",
    "info":      "#00c8f0",
    # Badge variants
    "badge_ai":  "#ff1f5a",
    "badge_hl":  "#ff6090",
    # Special
    "gold":      "#f0c040",
    "purple":    "#9960ff",
    "teal":      "#00d4c0",
}

BADGE_STYLES = {
    "circle":  "Classic circular stamp",
    "shield":  "Shield / badge shape",
    "ribbon":  "Corner ribbon overlay",
    "banner":  "Bottom banner strip",
    "hex":     "Hexagonal stamp",
}

SCORE_BLEND_MODES = ["average", "maximum", "weighted_avg", "ensemble_vote"]

BASE_STYLE = f"""
QWidget {{
    background: {C['bg']};
    color: {C['text']};
    font-family: 'JetBrains Mono', 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
    font-size: 12px;
}}
QLabel {{ color: {C['text']}; background: transparent; }}
QLineEdit {{
    background: {C['surface']};
    color: {C['text']};
    border: 1px solid {C['border']};
    padding: 7px 11px;
    border-radius: 6px;
    selection-background-color: {C['accent']};
}}
QLineEdit:focus {{ border: 1px solid {C['accent']}; background: {C['surface2']}; }}
QDoubleSpinBox, QSpinBox {{
    background: {C['surface']};
    color: {C['text']};
    border: 1px solid {C['border']};
    padding: 5px 8px;
    border-radius: 6px;
}}
QDoubleSpinBox:focus, QSpinBox:focus {{ border: 1px solid {C['accent']}; }}
QComboBox {{
    background: {C['surface']};
    color: {C['text']};
    border: 1px solid {C['border']};
    padding: 6px 10px;
    border-radius: 6px;
}}
QComboBox::drop-down {{ border: none; width: 24px; }}
QComboBox QAbstractItemView {{
    background: {C['surface2']};
    color: {C['text']};
    selection-background-color: {C['muted']};
    border: 1px solid {C['border2']};
}}
QCheckBox {{ color: {C['text']}; spacing: 9px; }}
QCheckBox::indicator {{
    width: 16px; height: 16px;
    border: 1px solid {C['border2']};
    border-radius: 4px;
    background: {C['surface']};
}}
QCheckBox::indicator:checked {{
    background: {C['accent']};
    border-color: {C['accent']};
}}
QRadioButton {{ color: {C['text']}; spacing: 9px; }}
QRadioButton::indicator {{
    width: 14px; height: 14px;
    border: 1px solid {C['border2']};
    border-radius: 7px;
    background: {C['surface']};
}}
QRadioButton::indicator:checked {{
    background: {C['accent']};
    border-color: {C['accent']};
}}
QTabWidget::pane {{
    border: 1px solid {C['border']};
    border-radius: 6px;
    background: {C['bg2']};
}}
QTabBar::tab {{
    background: {C['surface']};
    color: {C['sub']};
    padding: 10px 22px;
    border-bottom: 2px solid transparent;
    margin-right: 2px;
}}
QTabBar::tab:selected {{
    color: {C['text']};
    background: {C['surface2']};
    border-bottom: 2px solid {C['accent']};
}}
QTabBar::tab:hover:!selected {{ color: {C['text2']}; }}
QTableWidget {{
    background: {C['surface']};
    gridline-color: {C['border']};
    border: 1px solid {C['border']};
    border-radius: 6px;
}}
QTableWidget::item {{ padding: 5px 10px; border: none; }}
QTableWidget::item:selected {{ background: {C['muted']}; color: {C['text']}; }}
QTableWidget::item:alternate {{ background: {C['bg2']}; }}
QHeaderView::section {{
    background: {C['bg']};
    color: {C['sub']};
    padding: 8px 10px;
    border: none;
    border-bottom: 1px solid {C['border']};
    font-size: 10px;
    letter-spacing: 1.8px;
    text-transform: uppercase;
}}
QScrollBar:vertical {{
    background: {C['surface']};
    width: 6px;
    border-radius: 3px;
}}
QScrollBar::handle:vertical {{
    background: {C['muted']};
    border-radius: 3px;
    min-height: 20px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
QScrollBar:horizontal {{
    background: {C['surface']};
    height: 6px;
    border-radius: 3px;
}}
QScrollBar::handle:horizontal {{
    background: {C['muted']};
    border-radius: 3px;
    min-width: 20px;
}}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0; }}
QTextEdit {{
    background: {C['surface']};
    color: {C['text2']};
    border: 1px solid {C['border']};
    border-radius: 6px;
    padding: 8px;
    selection-background-color: {C['accent']};
}}
QGroupBox {{
    border: 1px solid {C['border']};
    border-radius: 8px;
    margin-top: 16px;
    padding-top: 10px;
    font-size: 10px;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: 14px;
    color: {C['sub']};
    letter-spacing: 1.5px;
    text-transform: uppercase;
}}
QProgressBar {{
    background: {C['surface']};
    border: 1px solid {C['border']};
    border-radius: 5px;
    text-align: center;
    color: {C['text']};
    font-size: 10px;
    max-height: 14px;
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 {C['accent']}, stop:1 {C['accent2']});
    border-radius: 4px;
}}
QSlider::groove:horizontal {{
    background: {C['surface2']};
    height: 4px;
    border-radius: 2px;
}}
QSlider::handle:horizontal {{
    background: {C['accent']};
    width: 16px;
    height: 16px;
    margin: -6px 0;
    border-radius: 8px;
}}
QSlider::sub-page:horizontal {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 {C['accent_d']}, stop:1 {C['accent']});
    border-radius: 2px;
}}
QListWidget {{
    background: {C['surface']};
    border: 1px solid {C['border']};
    border-radius: 6px;
    padding: 4px;
}}
QListWidget::item {{
    padding: 5px 8px;
    border-radius: 4px;
}}
QListWidget::item:selected {{
    background: {C['muted']};
    color: {C['text']};
}}
QSplitter::handle {{ background: {C['border']}; }}
QMenu {{
    background: {C['surface2']};
    border: 1px solid {C['border2']};
    border-radius: 6px;
    padding: 4px;
}}
QMenu::item {{
    padding: 8px 24px;
    border-radius: 4px;
}}
QMenu::item:selected {{ background: {C['muted']}; }}
QMenu::separator {{ background: {C['border']}; height: 1px; margin: 4px 0; }}
"""

def mk_btn(color=None, fg="#fff", small=False, outline=False):
    bg  = color or C["accent"]
    pad = "5px 14px" if small else "9px 20px"
    fs  = "10" if small else "11"
    if outline:
        return (
            f"QPushButton {{ background: transparent; color: {bg}; border: 1px solid {bg};"
            f" padding: {pad}; border-radius: 6px; font-weight: bold; font-size: {fs}px;"
            f" letter-spacing: 0.5px; }}"
            f"QPushButton:hover {{ background: {bg}22; }}"
            f"QPushButton:disabled {{ border-color: {C['muted']}; color: {C['sub']}; }}"
        )
    return (
        f"QPushButton {{ background: {bg}; color: {fg}; border: none; padding: {pad};"
        f" border-radius: 6px; font-weight: bold; font-size: {fs}px; letter-spacing: 0.5px; }}"
        f"QPushButton:hover {{ background: {bg}dd; }}"
        f"QPushButton:pressed {{ background: {bg}99; }}"
        f"QPushButton:disabled {{ background: {C['muted']}; color: {C['sub']}; }}"
    )

# ══════════════════════════════════════════════════════════════════════════════
#  DATA MODELS
# ══════════════════════════════════════════════════════════════════════════════
@dataclass
class Detection:
    id:            str   = field(default_factory=lambda: str(uuid.uuid4())[:8])
    ts:            float = field(default_factory=time.time)
    ts_str:        str   = ""
    score:         float = 0.0
    score_pct:     int   = 0
    is_ai:         bool  = True
    threshold_pct: int   = 82
    x:             int   = 0
    y:             int   = 0
    w:             int   = 0
    h:             int   = 0
    phash:         str   = ""
    burst_scores:  list  = field(default_factory=list)
    blend_mode:    str   = "average"
    monitor_idx:   int   = 0
    snapshot_path: str   = ""
    process_name:  str   = ""
    webhook_sent:  bool  = False
    entropy:       float = 0.0
    api_latency_ms:float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Detection":
        known = {f.name for f in cls.__dataclass_fields__.values()}
        return cls(**{k: v for k, v in d.items() if k in known})

# ══════════════════════════════════════════════════════════════════════════════
#  PERCEPTUAL HASHING
# ══════════════════════════════════════════════════════════════════════════════
def phash(img: Image.Image, size: int = 8) -> str:
    """Difference hash (dHash) — fast and robust to minor edits."""
    gray   = img.convert("L").resize((size + 1, size), Image.LANCZOS)
    pixels = list(gray.getdata())
    diff   = [pixels[i] > pixels[i + 1] for i in range(size * size)]
    val    = 0
    for bit in diff:
        val = (val << 1) | int(bit)
    return f"{val:016x}"

def ahash(img: Image.Image, size: int = 8) -> str:
    """Average hash — complementary to dHash."""
    gray   = img.convert("L").resize((size, size), Image.LANCZOS)
    pixels = list(gray.getdata())
    avg    = sum(pixels) / len(pixels)
    val    = 0
    for px in pixels:
        val = (val << 1) | (1 if px >= avg else 0)
    return f"{val:016x}"

def hamming_distance(h1: str, h2: str) -> int:
    """Hamming distance between two hex hash strings."""
    try:
        return bin(int(h1, 16) ^ int(h2, 16)).count("1")
    except Exception:
        return 64

def image_entropy(img: Image.Image) -> float:
    """Shannon entropy of image — high entropy ≈ complex / photographic."""
    gray  = img.convert("L").resize((128, 128), Image.LANCZOS)
    hist  = gray.histogram()
    total = sum(hist)
    if total == 0:
        return 0.0
    ent = 0.0
    for v in hist:
        if v > 0:
            p = v / total
            ent -= p * math.log2(p)
    return ent

# ══════════════════════════════════════════════════════════════════════════════
#  BLOOM FILTER (lightweight deduplication acceleration)
# ══════════════════════════════════════════════════════════════════════════════
class BloomFilter:
    """Simple bit-array bloom filter for fast hash pre-screening."""
    def __init__(self, capacity: int = 10_000, error_rate: float = 0.01):
        self._bits  = capacity * 10
        self._array = bytearray(self._bits // 8 + 1)
        self._seeds = [13, 31, 53, 71]

    def _hashes(self, key: str) -> List[int]:
        return [
            (int(hashlib.md5(f"{s}{key}".encode()).hexdigest(), 16) % self._bits)
            for s in self._seeds
        ]

    def add(self, key: str):
        for idx in self._hashes(key):
            self._array[idx // 8] |= (1 << (idx % 8))

    def __contains__(self, key: str) -> bool:
        return all(
            self._array[idx // 8] & (1 << (idx % 8))
            for idx in self._hashes(key)
        )

# ══════════════════════════════════════════════════════════════════════════════
#  ENCRYPTED CREDENTIAL STORE
# ══════════════════════════════════════════════════════════════════════════════
def _derive_key() -> bytes:
    """Derive a machine-specific Fernet key from host identifiers."""
    seed = (
        os.environ.get("USER", "") +
        os.environ.get("HOME", "") +
        str(os.getpid() // 1000)   # stable per user session
    ).encode()
    h = hashlib.sha256(seed).digest()
    return base64.urlsafe_b64encode(h)

def encrypt_str(plaintext: str) -> str:
    try:
        from cryptography.fernet import Fernet
        f = Fernet(_derive_key())
        return f.encrypt(plaintext.encode()).decode()
    except Exception:
        return plaintext   # fallback: store plain if cryptography unavailable

def decrypt_str(token: str) -> str:
    try:
        from cryptography.fernet import Fernet
        f = Fernet(_derive_key())
        return f.decrypt(token.encode()).decode()
    except Exception:
        return token   # fallback

# ══════════════════════════════════════════════════════════════════════════════
#  CONFIG
# ══════════════════════════════════════════════════════════════════════════════
class Config:
    DEFAULTS = dict(
        # API
        api_user                = "",
        api_secret              = "",
        api_secret_enc          = "",   # encrypted form
        interval_ms             = 4000,
        retry_max               = 3,
        retry_backoff_ms        = 600,
        score_blend             = "average",  # average|maximum|weighted_avg|ensemble_vote
        # Detection
        threshold               = AI_THRESHOLD_DEFAULT,
        monitor_index           = 0,
        motion_min_px           = 100,
        burst_frames            = 3,
        burst_gap_ms            = 200,
        dedup_enabled           = True,
        dedup_hamming_tolerance = 4,    # treat hashes within N bits as same
        entropy_filter          = False,
        entropy_min             = 4.5,  # skip low-entropy regions (solid color)
        # Badge
        badge_style             = "circle",
        badge_opacity           = 0.90,
        badge_size              = 52,
        badge_pulse             = True,
        badge_sound             = False,
        badge_hold_ms           = BADGE_HOLD_MS,
        badge_fade_ms           = BADGE_FADE_MS,
        # Alerts
        desktop_notify          = True,
        webhook_enabled         = False,
        webhook_url             = "",
        webhook_type            = "slack",  # slack|teams|custom
        webhook_threshold       = 0.90,
        # Logging
        log_enabled             = True,
        max_log                 = 2000,
        snapshot_enabled        = False,
        snapshot_retention      = 200,
        # System
        autostart               = False,
        auto_pause_idle_s       = 0,
        max_workers             = MAX_WORKERS,
        # Exclusion zones (list of [x,y,w,h] per monitor)
        exclusion_zones         = [],
        # Rules
        allowlist_processes     = [],
        denylist_processes      = [],
    )

    def __init__(self):
        for k, v in self.DEFAULTS.items():
            setattr(self, k, copy.deepcopy(v))
        self.load()

    def load(self):
        if CONFIG_FILE.exists():
            try:
                d = json.loads(CONFIG_FILE.read_text())
                for k, v in self.DEFAULTS.items():
                    if k in d:
                        setattr(self, k, d[k])
                # Decrypt secret if encrypted form present
                if self.api_secret_enc and not self.api_secret:
                    self.api_secret = decrypt_str(self.api_secret_enc)
            except Exception as e:
                log.warning(f"Config load: {e}")

    def save(self):
        try:
            d = {k: getattr(self, k) for k in self.DEFAULTS}
            # Always encrypt secret before saving
            if self.api_secret:
                d["api_secret_enc"] = encrypt_str(self.api_secret)
                d["api_secret"]     = ""  # never store plain
            CONFIG_FILE.write_text(json.dumps(d, indent=2))
        except Exception as e:
            log.error(f"Config save: {e}")

    def validate(self) -> List[str]:
        errs = []
        if not str(self.api_user).strip():
            errs.append("Sightengine API User is required.")
        if not str(self.api_secret).strip():
            errs.append("Sightengine API Secret is required.")
        if not (0.0 < self.threshold <= 1.0):
            errs.append("Threshold must be between 0.01 and 1.00.")
        return errs

    def cost_estimate(self, api_count: int) -> dict:
        """Estimate monthly API cost given current rate."""
        billable = max(0, api_count - FREE_CALLS_PER_MONTH)
        return {
            "calls":    api_count,
            "free":     min(api_count, FREE_CALLS_PER_MONTH),
            "billable": billable,
            "cost_usd": round(billable * COST_PER_CALL_USD, 4),
        }

# ══════════════════════════════════════════════════════════════════════════════
#  SQLITE DETECTION LOG
# ══════════════════════════════════════════════════════════════════════════════
class DetectionDB:
    """SQLite-backed detection log with fast aggregation queries."""

    _SCHEMA = """
    CREATE TABLE IF NOT EXISTS detections (
        id            TEXT PRIMARY KEY,
        ts            REAL NOT NULL,
        ts_str        TEXT,
        score         REAL,
        score_pct     INTEGER,
        is_ai         INTEGER DEFAULT 1,
        threshold_pct INTEGER,
        x INTEGER, y INTEGER, w INTEGER, h INTEGER,
        phash         TEXT,
        burst_scores  TEXT,
        blend_mode    TEXT,
        monitor_idx   INTEGER DEFAULT 0,
        snapshot_path TEXT,
        process_name  TEXT,
        webhook_sent  INTEGER DEFAULT 0,
        entropy       REAL,
        api_latency_ms REAL
    );
    CREATE INDEX IF NOT EXISTS idx_ts    ON detections(ts);
    CREATE INDEX IF NOT EXISTS idx_is_ai ON detections(is_ai);
    CREATE INDEX IF NOT EXISTS idx_score ON detections(score);
    """

    def __init__(self, config: Config):
        self.config = config
        self._lock  = threading.Lock()
        self._conn  = sqlite3.connect(str(DB_FILE), check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        with self._conn:
            self._conn.executescript(self._SCHEMA)

    def add(self, det: Detection):
        if not self.config.log_enabled:
            return
        with self._lock:
            try:
                d = det.to_dict()
                d["burst_scores"] = json.dumps(d.get("burst_scores", []))
                d["is_ai"]        = int(d["is_ai"])
                d["webhook_sent"] = int(d["webhook_sent"])
                cols  = ", ".join(d.keys())
                plchs = ", ".join("?" for _ in d)
                self._conn.execute(
                    f"INSERT OR IGNORE INTO detections ({cols}) VALUES ({plchs})",
                    list(d.values())
                )
                self._conn.commit()
                self._prune()
            except Exception as e:
                log.error(f"DB insert: {e}")

    def _prune(self):
        count = self._conn.execute("SELECT COUNT(*) FROM detections").fetchone()[0]
        if count > self.config.max_log:
            excess = count - self.config.max_log
            self._conn.execute(
                "DELETE FROM detections WHERE id IN "
                "(SELECT id FROM detections ORDER BY ts ASC LIMIT ?)", (excess,)
            )
            self._conn.commit()

    def entries(self, limit: int = 2000, ai_only: bool = False) -> List[Detection]:
        with self._lock:
            q = "SELECT * FROM detections"
            if ai_only:
                q += " WHERE is_ai=1"
            q += " ORDER BY ts DESC"
            if limit:
                q += f" LIMIT {limit}"
            rows = self._conn.execute(q).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            d["is_ai"]       = bool(d["is_ai"])
            d["webhook_sent"]= bool(d["webhook_sent"])
            try:
                d["burst_scores"] = json.loads(d.get("burst_scores") or "[]")
            except Exception:
                d["burst_scores"] = []
            result.append(Detection.from_dict(d))
        return result

    def stats(self) -> dict:
        with self._lock:
            now   = time.time()
            h24   = now - 86400
            today = datetime.date.today().isoformat()
            def q1(sql, *args):
                r = self._conn.execute(sql, args).fetchone()
                return r[0] if r else 0
            total   = q1("SELECT COUNT(*) FROM detections")
            ai_tot  = q1("SELECT COUNT(*) FROM detections WHERE is_ai=1")
            ai_h24  = q1("SELECT COUNT(*) FROM detections WHERE is_ai=1 AND ts>=?", h24)
            ai_today= q1("SELECT COUNT(*) FROM detections WHERE is_ai=1 AND ts_str LIKE ?", today+"%")
            avg_sc  = q1("SELECT AVG(score) FROM detections WHERE is_ai=1") or 0.0
            max_sc  = q1("SELECT MAX(score) FROM detections WHERE is_ai=1") or 0.0
            avg_lat = q1("SELECT AVG(api_latency_ms) FROM detections") or 0.0
        return dict(
            total=total, ai=ai_tot, real=total - ai_tot,
            h24=ai_h24, today=ai_today,
            avg=float(avg_sc), maximum=float(max_sc),
            avg_latency=float(avg_lat),
        )

    def hourly_buckets(self, days: int = 3) -> Dict[str, int]:
        since = time.time() - days * 86400
        with self._lock:
            rows = self._conn.execute(
                "SELECT ts_str FROM detections WHERE is_ai=1 AND ts>=?", (since,)
            ).fetchall()
        buckets: Dict[str, int] = collections.defaultdict(int)
        for r in rows:
            h = (r[0] or "")[:13]
            if h:
                buckets[h] += 1
        return dict(buckets)

    def score_series(self, limit: int = 120) -> List[float]:
        with self._lock:
            rows = self._conn.execute(
                "SELECT score FROM detections WHERE is_ai=1 ORDER BY ts DESC LIMIT ?",
                (limit,)
            ).fetchall()
        return [r[0] for r in reversed(rows)]

    def export_csv(self, path: str) -> bool:
        rows = self.entries(limit=0)
        if not rows:
            return False
        try:
            fields = ["id","ts_str","score_pct","is_ai","blend_mode",
                      "x","y","w","h","phash","monitor_idx",
                      "process_name","entropy","api_latency_ms"]
            with open(path, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
                w.writeheader()
                for det in rows:
                    w.writerow({k: getattr(det, k, "") for k in fields})
            return True
        except Exception as e:
            log.error(f"CSV export: {e}")
            return False

    def export_json(self, path: str) -> bool:
        rows = self.entries(limit=0)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump([r.to_dict() for r in rows], f, indent=2)
            return True
        except Exception as e:
            log.error(f"JSON export: {e}")
            return False

    def clear(self):
        with self._lock:
            self._conn.execute("DELETE FROM detections")
            self._conn.commit()

    def close(self):
        try:
            self._conn.close()
        except Exception:
            pass

# ══════════════════════════════════════════════════════════════════════════════
#  SNAPSHOT ARCHIVE
# ══════════════════════════════════════════════════════════════════════════════
class SnapshotArchive:
    """Saves cropped region JPEGs for each detection."""

    def __init__(self, config: Config):
        self.config = config

    def save(self, det_id: str, img: Image.Image) -> str:
        if not self.config.snapshot_enabled:
            return ""
        try:
            ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f"{ts}_{det_id}.jpg"
            path = SNAPSHOT_DIR / name
            img.save(str(path), format="JPEG", quality=SNAPSHOT_QUALITY)
            self._prune()
            return str(path)
        except Exception as e:
            log.warning(f"Snapshot save: {e}")
            return ""

    def _prune(self):
        snaps = sorted(SNAPSHOT_DIR.glob("*.jpg"), key=lambda p: p.stat().st_mtime)
        limit = self.config.snapshot_retention or MAX_SNAPSHOTS
        while len(snaps) > limit:
            try:
                snaps.pop(0).unlink()
            except Exception:
                break

    def list_all(self) -> List[Path]:
        return sorted(SNAPSHOT_DIR.glob("*.jpg"),
                      key=lambda p: p.stat().st_mtime, reverse=True)

# ══════════════════════════════════════════════════════════════════════════════
#  WEBHOOK NOTIFIER
# ══════════════════════════════════════════════════════════════════════════════
class WebhookNotifier:
    """Posts detection alerts to Slack, Teams, or custom endpoints."""

    def __init__(self, config: Config):
        self.config = config
        self._q: queue.Queue = queue.Queue()
        self._thread = threading.Thread(target=self._worker, daemon=True)
        self._thread.start()

    def enqueue(self, det: Detection):
        if not self.config.webhook_enabled:
            return
        if det.score < self.config.webhook_threshold:
            return
        self._q.put(det)

    def _worker(self):
        while True:
            try:
                det = self._q.get(timeout=2.0)
                self._post(det)
            except queue.Empty:
                continue
            except Exception:
                pass

    def _post(self, det: Detection):
        url = self.config.webhook_url
        if not url:
            return
        pct = det.score_pct
        try:
            wtype = self.config.webhook_type
            if wtype == "slack":
                payload = {
                    "text": f":robot_face: *AI Content Detected* — {pct}% confidence",
                    "attachments": [{
                        "color": "#ff2060",
                        "fields": [
                            {"title": "Score", "value": f"{pct}%", "short": True},
                            {"title": "Region", "value": f"{det.w}×{det.h}px @ ({det.x},{det.y})", "short": True},
                            {"title": "Blend", "value": det.blend_mode, "short": True},
                            {"title": "Time",  "value": det.ts_str, "short": True},
                        ],
                        "footer": f"AI Sentinel Pro v{APP_VERSION}",
                    }]
                }
            elif wtype == "teams":
                payload = {
                    "@type": "MessageCard",
                    "@context": "http://schema.org/extensions",
                    "themeColor": "FF2060",
                    "summary": f"AI Content Detected ({pct}%)",
                    "sections": [{
                        "activityTitle": f"AI Content Detected — {pct}% confidence",
                        "facts": [
                            {"name": "Score", "value": f"{pct}%"},
                            {"name": "Region", "value": f"{det.w}×{det.h}"},
                            {"name": "Time",   "value": det.ts_str},
                        ]
                    }]
                }
            else:  # custom
                payload = det.to_dict()

            resp = requests.post(url, json=payload, timeout=8)
            if resp.status_code < 300:
                log.info(f"Webhook sent ({pct}%)")
            else:
                log.warning(f"Webhook {resp.status_code}: {resp.text[:80]}")
        except Exception as e:
            log.warning(f"Webhook error: {e}")

# ══════════════════════════════════════════════════════════════════════════════
#  SCREEN HEATMAP
# ══════════════════════════════════════════════════════════════════════════════
class DetectionHeatmap:
    """Tracks detection density across screen grid cells."""

    def __init__(self, screen_w: int = 1920, screen_h: int = 1080,
                 cell: int = HEATMAP_CELL_PX):
        self.cell  = cell
        self.cols  = max(1, screen_w // cell)
        self.rows  = max(1, screen_h // cell)
        self._grid = [[0.0] * self.cols for _ in range(self.rows)]
        self._lock = threading.Lock()

    def record(self, x: int, y: int, w: int, h: int, score: float):
        cx = x // self.cell
        cy = y // self.cell
        with self._lock:
            for dy in range(max(1, h // self.cell + 1)):
                for dx in range(max(1, w // self.cell + 1)):
                    rx, ry = cx + dx, cy + dy
                    if 0 <= ry < self.rows and 0 <= rx < self.cols:
                        self._grid[ry][rx] = min(1.0, self._grid[ry][rx] + score * 0.5)

    def decay(self):
        with self._lock:
            for r in range(self.rows):
                for c in range(self.cols):
                    self._grid[r][c] *= HEATMAP_DECAY

    def snapshot(self) -> List[List[float]]:
        with self._lock:
            return copy.deepcopy(self._grid)

    def max_val(self) -> float:
        with self._lock:
            return max(max(row) for row in self._grid) if self._grid else 0.0

# ══════════════════════════════════════════════════════════════════════════════
#  AUTOSTART
# ══════════════════════════════════════════════════════════════════════════════
class Autostart:
    SCRIPT = Path(sys.argv[0]).resolve()
    LINUX_DESKTOP = Path.home() / ".config" / "autostart" / "ai_sentinel_pro.desktop"
    MAC_PLIST     = Path.home() / "Library" / "LaunchAgents" / "com.punks.aisentinel.plist"

    @classmethod
    def install(cls):
        try:
            if sys.platform == "win32":      cls._win_install()
            elif sys.platform == "darwin":   cls._mac_install()
            else:                            cls._linux_install()
            log.info("Autostart installed.")
        except Exception as e:
            log.error(f"Autostart install: {e}")

    @classmethod
    def uninstall(cls):
        try:
            if sys.platform == "win32":      cls._win_remove()
            elif sys.platform == "darwin":   cls._mac_remove()
            else:                            cls._linux_remove()
            log.info("Autostart removed.")
        except Exception as e:
            log.error(f"Autostart remove: {e}")

    @classmethod
    def _linux_install(cls):
        cls.LINUX_DESKTOP.parent.mkdir(parents=True, exist_ok=True)
        cls.LINUX_DESKTOP.write_text(
            f"[Desktop Entry]\nType=Application\nName=AI Sentinel Pro\n"
            f"Exec={sys.executable} {cls.SCRIPT}\nHidden=false\nNoDisplay=false\n"
            f"X-GNOME-Autostart-enabled=true\nComment=AI content detection monitor\n"
        )

    @classmethod
    def _linux_remove(cls):
        if cls.LINUX_DESKTOP.exists():
            cls.LINUX_DESKTOP.unlink()

    @classmethod
    def _mac_install(cls):
        cls.MAC_PLIST.parent.mkdir(parents=True, exist_ok=True)
        cls.MAC_PLIST.write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
            '"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
            '<plist version="1.0"><dict>'
            '<key>Label</key><string>com.punks.aisentinel</string>'
            '<key>ProgramArguments</key><array>'
            f'<string>{sys.executable}</string><string>{cls.SCRIPT}</string>'
            '</array><key>RunAtLoad</key><true/></dict></plist>\n'
        )
        subprocess.run(["launchctl", "load", str(cls.MAC_PLIST)], check=False)

    @classmethod
    def _mac_remove(cls):
        if cls.MAC_PLIST.exists():
            subprocess.run(["launchctl", "unload", str(cls.MAC_PLIST)], check=False)
            cls.MAC_PLIST.unlink()

    @classmethod
    def _win_install(cls):
        import winreg
        k = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                           r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
                           winreg.KEY_SET_VALUE)
        winreg.SetValueEx(k, "AISentinelPro", 0, winreg.REG_SZ,
                          f'"{sys.executable}" "{cls.SCRIPT}"')
        winreg.CloseKey(k)

    @classmethod
    def _win_remove(cls):
        import winreg
        try:
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                               r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
                               winreg.KEY_SET_VALUE)
            winreg.DeleteValue(k, "AISentinelPro")
            winreg.CloseKey(k)
        except FileNotFoundError:
            pass

# ══════════════════════════════════════════════════════════════════════════════
#  OS NOTIFICATIONS
# ══════════════════════════════════════════════════════════════════════════════
def notify_os(title: str, body: str):
    try:
        if sys.platform == "darwin":
            safe_body  = body.replace('"', '\\"')
            safe_title = title.replace('"', '\\"')
            os.system(f'osascript -e \'display notification "{safe_body}" with title "{safe_title}"\'')
        elif sys.platform.startswith("linux"):
            subprocess.Popen(
                ["notify-send", "-t", "4000", "-u", "normal",
                 "-i", "dialog-warning", title, body],
                stderr=subprocess.DEVNULL,
            )
        elif sys.platform == "win32":
            # Use Windows Toast via PowerShell (no third-party dep)
            ps = (
                f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType=WindowsRuntime] | Out-Null;'
                f'$template=[Windows.UI.Notifications.ToastTemplateType]::ToastText02;'
                f'$xml=[Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent($template);'
                f'$xml.GetElementsByTagName("text")[0].AppendChild($xml.CreateTextNode("{title}")) | Out-Null;'
                f'$xml.GetElementsByTagName("text")[1].AppendChild($xml.CreateTextNode("{body}")) | Out-Null;'
                f'$toast=[Windows.UI.Notifications.ToastNotification]::new($xml);'
                f'[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("AI Sentinel").Show($toast);'
            )
            subprocess.Popen(["powershell", "-WindowStyle", "Hidden", "-Command", ps],
                             stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except Exception:
        pass

def beep():
    try:
        if sys.platform == "win32":
            import winsound; winsound.Beep(880, 200)
        elif sys.platform == "darwin":
            os.system("afplay /System/Library/Sounds/Funk.aiff &")
        else:
            sys.stdout.write("\a"); sys.stdout.flush()
    except Exception:
        pass

def get_active_process() -> str:
    """Best-effort: get foreground process name."""
    try:
        if sys.platform == "win32":
            import ctypes
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            pid  = ctypes.c_ulong()
            ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            return str(pid.value)
        elif sys.platform == "darwin":
            r = subprocess.run(
                ["osascript", "-e",
                 'tell application "System Events" to get name of first application process whose frontmost is true'],
                capture_output=True, text=True, timeout=1
            )
            return r.stdout.strip()
        else:
            r = subprocess.run(
                ["xdotool", "getactivewindow", "getwindowname"],
                capture_output=True, text=True, timeout=1
            )
            return r.stdout.strip()[:40]
    except Exception:
        return ""

# ══════════════════════════════════════════════════════════════════════════════
#  API WORKER THREAD
# ══════════════════════════════════════════════════════════════════════════════
class APIWorker(QThread):
    done  = pyqtSignal(dict, list, str, float, float)   # result, coords, phash, entropy, latency
    error = pyqtSignal(str, str)

    def __init__(self, frames: List[bytes], coords: list, ph: str,
                 entropy: float, config: Config):
        super().__init__()
        self.frames  = frames
        self.coords  = coords
        self.phash   = ph
        self.entropy = entropy
        self.config  = config

    def run(self):
        u = str(self.config.api_user).strip()
        s = str(self.config.api_secret).strip()
        if not u or not s:
            self.error.emit("NO_CREDENTIALS", self.phash)
            return

        last_err = None
        t0 = time.time()
        for attempt in range(1, self.config.retry_max + 1):
            try:
                result = self._call_sightengine(self.frames[0], u, s)
                if result.get("status") != "success":
                    msg = result.get("error", {}).get("message", "?")[:30]
                    self.error.emit(f"API:{msg}", self.phash)
                    return

                # Burst analysis
                scores = [result.get("type", {}).get("ai_generated", 0.0)]
                if len(self.frames) > 1:
                    for frame in self.frames[1:]:
                        try:
                            r2 = self._call_sightengine(frame, u, s)
                            if r2.get("status") == "success":
                                scores.append(r2.get("type", {}).get("ai_generated", 0.0))
                        except Exception:
                            pass

                # Score blending
                blend = self.config.score_blend
                if blend == "maximum":
                    final = max(scores)
                elif blend == "weighted_avg":
                    weights = [1.0 / (i + 1) for i in range(len(scores))]
                    total_w = sum(weights)
                    final   = sum(s * w for s, w in zip(scores, weights)) / total_w
                elif blend == "ensemble_vote":
                    th    = self.config.threshold
                    votes = sum(1 for s in scores if s >= th)
                    final = max(scores) if votes >= len(scores) / 2 else min(scores)
                else:  # average
                    final = sum(scores) / len(scores)

                result.setdefault("type", {})["ai_generated"] = final
                result["burst_scores"] = scores

                latency = (time.time() - t0) * 1000
                self.done.emit(result, self.coords, self.phash, self.entropy, latency)
                return

            except requests.Timeout:
                last_err = "TIMEOUT"
            except requests.ConnectionError:
                last_err = "NO_NETWORK"
            except Exception as e:
                last_err = repr(e)[:28]

            if attempt < self.config.retry_max:
                time.sleep((self.config.retry_backoff_ms / 1000) * (2 ** (attempt - 1)))

        self.error.emit(last_err or "UNKNOWN", self.phash)

    def _call_sightengine(self, frame_bytes: bytes, user: str, secret: str) -> dict:
        buf = io.BytesIO(frame_bytes)
        buf.seek(0)
        r = requests.post(
            "https://api.sightengine.com/1.0/check.json",
            files={"media": ("frame.jpg", buf, "image/jpeg")},
            data={"models": "genai", "api_user": user, "api_secret": secret},
            timeout=12,
        )
        return r.json()

# ══════════════════════════════════════════════════════════════════════════════
#  BADGE WIDGETS — Multiple style variants
# ══════════════════════════════════════════════════════════════════════════════
class AIBadge(QWidget):
    """Click-through, frameless floating badge with configurable style."""

    def __init__(self, score: float, x: int, y: int, w: int, h: int,
                 config: Config):
        super().__init__()
        self.score  = score
        self.config = config
        self.sz     = config.badge_size
        self.style_ = config.badge_style

        flags = (Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint |
                 Qt.Tool | Qt.WindowTransparentForInput)
        if sys.platform.startswith("linux"):
            flags |= Qt.X11BypassWindowManagerHint
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setWindowOpacity(config.badge_opacity)

        # Size depends on style
        if self.style_ == "ribbon":
            bw, bh = max(w, 120), 36
        elif self.style_ == "banner":
            bw, bh = max(w, 200), 30
        else:
            bw = bh = self.sz + 8

        self.setFixedSize(bw, bh)

        # Position
        screen = QApplication.primaryScreen().geometry()
        if self.style_ == "ribbon":
            px = x; py = y
        elif self.style_ == "banner":
            px = x; py = y + h - bh
        else:
            px = x + w - bw - 8
            py = y + h - bh - 8

        px = max(0, min(px, screen.width()  - bw))
        py = max(0, min(py, screen.height() - bh))
        self.move(px, py)
        self.show()

        # Opacity animation
        self._eff  = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._eff)
        self._hold_timer = QTimer(self)
        self._hold_timer.setSingleShot(True)
        self._hold_timer.timeout.connect(self._start_fade)
        self._hold_timer.start(config.badge_hold_ms)

        # Pulse animation
        if config.badge_pulse:
            self._pulse_anim = QVariantAnimation(self)
            self._pulse_anim.setStartValue(1.0)
            self._pulse_anim.setEndValue(0.75)
            self._pulse_anim.setDuration(800)
            self._pulse_anim.setEasingCurve(QEasingCurve.SineCurve)
            self._pulse_anim.setLoopCount(-1)
            self._pulse_anim.valueChanged.connect(
                lambda v: self._eff.setOpacity(float(v))
            )
            self._pulse_anim.start()
        else:
            self._pulse_anim = None

    def _start_fade(self):
        if self._pulse_anim:
            self._pulse_anim.stop()
        fade = QPropertyAnimation(self._eff, b"opacity")
        fade.setDuration(self.config.badge_fade_ms)
        fade.setStartValue(float(self._eff.opacity()))
        fade.setEndValue(0.0)
        fade.setEasingCurve(QEasingCurve.InCubic)
        fade.finished.connect(self.close)
        fade.start(QPropertyAnimation.DeleteWhenStopped)

    def paintEvent(self, _):
        p = QPainter(self)
        p.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        style = self.style_
        if style == "shield":
            self._paint_shield(p)
        elif style == "ribbon":
            self._paint_ribbon(p)
        elif style == "banner":
            self._paint_banner(p)
        elif style == "hex":
            self._paint_hex(p)
        else:
            self._paint_circle(p)
        p.end()

    def _paint_circle(self, p: QPainter):
        sz  = self.sz
        pct = int(self.score * 100)

        # Glow
        glow = QRadialGradient(sz / 2 + 4, sz / 2 + 4, sz / 2 + 4)
        glow.setColorAt(0.55, QColor(255, 20, 80, 90))
        glow.setColorAt(1.0,  QColor(255, 20, 80, 0))
        p.setBrush(QBrush(glow)); p.setPen(Qt.NoPen)
        p.drawEllipse(0, 0, sz + 8, sz + 8)

        # Circle
        gr = QLinearGradient(4, 4, sz + 4, sz + 4)
        gr.setColorAt(0,   QColor(255, 30, 100))
        gr.setColorAt(0.5, QColor(200, 10, 70))
        gr.setColorAt(1,   QColor(120,  0, 50))
        p.setBrush(QBrush(gr))
        p.setPen(QPen(QColor(255, 255, 255, 50), 1.0))
        p.drawEllipse(4, 4, sz, sz)

        # "AI" text
        fnt = QFont("Arial Black", max(int(sz * 0.32), 9), QFont.Black)
        fnt.setLetterSpacing(QFont.AbsoluteSpacing, -0.5)
        p.setFont(fnt); p.setPen(QColor(255, 255, 255, 245))
        p.drawText(QRect(4, 4, sz, int(sz * 0.78)), Qt.AlignCenter, "AI")

        # Score pill
        if sz >= 40:
            ph = max(int(sz * 0.21), 10)
            pw = int(sz * 0.70)
            px = 4 + (sz - pw) // 2
            py = 4 + sz - ph - int(sz * 0.06)
            p.setBrush(QColor(0, 0, 0, 130)); p.setPen(Qt.NoPen)
            p.drawRoundedRect(px, py, pw, ph, ph // 2, ph // 2)
            p.setFont(QFont("Arial", max(int(sz * 0.16), 7), QFont.Bold))
            p.setPen(QColor(255, 190, 190, 230))
            p.drawText(QRect(px, py, pw, ph), Qt.AlignCenter, f"{pct}%")

    def _paint_shield(self, p: QPainter):
        sz  = self.sz
        pct = int(self.score * 100)
        # Shield path
        path = QPainterPath()
        path.moveTo(sz / 2 + 4, 4)
        path.lineTo(sz + 4, sz * 0.35 + 4)
        path.lineTo(sz + 4, sz * 0.65 + 4)
        path.quadTo(sz + 4, sz + 8, sz / 2 + 4, sz + 8)
        path.quadTo(4, sz + 8, 4, sz * 0.65 + 4)
        path.lineTo(4, sz * 0.35 + 4)
        path.closeSubpath()

        gr = QLinearGradient(4, 4, sz + 4, sz + 8)
        gr.setColorAt(0, QColor(255, 30, 100))
        gr.setColorAt(1, QColor(120,  0, 50))
        p.setBrush(QBrush(gr)); p.setPen(QPen(QColor(255, 255, 255, 60), 1.2))
        p.drawPath(path)

        # Label
        p.setFont(QFont("Arial Black", max(int(sz * 0.28), 8), QFont.Black))
        p.setPen(QColor(255, 255, 255, 240))
        p.drawText(QRect(4, int(sz * 0.2) + 4, sz, int(sz * 0.5)), Qt.AlignCenter, "AI")
        p.setFont(QFont("Arial", max(int(sz * 0.16), 7), QFont.Bold))
        p.setPen(QColor(255, 200, 200))
        p.drawText(QRect(4, int(sz * 0.65) + 4, sz, int(sz * 0.25)), Qt.AlignCenter, f"{pct}%")

    def _paint_ribbon(self, p: QPainter):
        w, h = self.width(), self.height()
        pct  = int(self.score * 100)
        gr   = QLinearGradient(0, 0, w, 0)
        gr.setColorAt(0, QColor(255, 30, 100))
        gr.setColorAt(1, QColor(150, 0, 60))
        p.setBrush(QBrush(gr)); p.setPen(Qt.NoPen)
        p.drawRoundedRect(0, 0, w, h, 4, 4)

        p.setFont(QFont("Arial Black", 11, QFont.Black))
        p.setPen(QColor(255, 255, 255, 240))
        p.drawText(QRect(0, 0, 60, h), Qt.AlignCenter, "AI")

        p.setFont(QFont("JetBrains Mono", 9))
        p.setPen(QColor(255, 200, 200, 200))
        p.drawText(QRect(65, 0, w - 70, h), Qt.AlignVCenter | Qt.AlignLeft,
                   f"AI-GENERATED  ·  {pct}% CONFIDENCE")

    def _paint_banner(self, p: QPainter):
        w, h = self.width(), self.height()
        pct  = int(self.score * 100)
        gr   = QLinearGradient(0, 0, 0, h)
        gr.setColorAt(0, QColor(0, 0, 0, 0))
        gr.setColorAt(1, QColor(200, 10, 60, 220))
        p.setBrush(QBrush(gr)); p.setPen(Qt.NoPen)
        p.drawRect(0, 0, w, h)

        p.setFont(QFont("Arial Black", 9, QFont.Black))
        p.setPen(QColor(255, 255, 255, 220))
        p.drawText(QRect(6, 0, w - 12, h), Qt.AlignVCenter | Qt.AlignRight,
                   f"⚡ AI GENERATED — {pct}%")

    def _paint_hex(self, p: QPainter):
        sz  = self.sz
        pct = int(self.score * 100)
        cx, cy, r = sz / 2 + 4, sz / 2 + 4, sz / 2 - 2
        pts = []
        for i in range(6):
            angle = math.pi / 180 * (60 * i - 30)
            pts.append(QPointF(cx + r * math.cos(angle), cy + r * math.sin(angle)))

        path = QPainterPath()
        path.moveTo(pts[0])
        for pt in pts[1:]:
            path.lineTo(pt)
        path.closeSubpath()

        gr = QLinearGradient(4, 4, sz + 4, sz + 4)
        gr.setColorAt(0, QColor(255, 30, 100))
        gr.setColorAt(1, QColor(100, 0, 50))
        p.setBrush(QBrush(gr))
        p.setPen(QPen(QColor(255, 255, 255, 70), 1.5))
        p.drawPath(path)

        p.setFont(QFont("Arial Black", max(int(sz * 0.3), 8), QFont.Black))
        p.setPen(QColor(255, 255, 255, 240))
        p.drawText(QRect(4, 4, sz, int(sz * 0.75)), Qt.AlignCenter, "AI")
        p.setFont(QFont("Arial", max(int(sz * 0.15), 7), QFont.Bold))
        p.setPen(QColor(255, 200, 200))
        p.drawText(QRect(4, int(sz * 0.65 + 4), sz, int(sz * 0.25)), Qt.AlignCenter, f"{pct}%")

# ══════════════════════════════════════════════════════════════════════════════
#  BADGE MANAGER
# ══════════════════════════════════════════════════════════════════════════════
class BadgeManager:
    def __init__(self, config: Config):
        self.config = config
        self._badges: List[AIBadge] = []

    def _cull(self):
        self._badges = [b for b in self._badges if b.isVisible()]

    def spawn(self, score: float, x: int, y: int, w: int, h: int):
        self._cull()
        if len(self._badges) >= MAX_REGIONS:
            try:
                self._badges[0].close()
                self._badges.pop(0)
            except Exception:
                pass
        badge = AIBadge(score, x, y, w, h, self.config)
        self._badges.append(badge)

    def clear_all(self):
        for b in self._badges:
            try:
                b.close()
            except Exception:
                pass
        self._badges.clear()

    def count(self) -> int:
        self._cull()
        return len(self._badges)

# ══════════════════════════════════════════════════════════════════════════════
#  SCREEN MONITOR
# ══════════════════════════════════════════════════════════════════════════════
class ScreenMonitor(QObject):
    detection = pyqtSignal(float, int, int, int, int, str, float, float)
    # score, x, y, w, h, ts_str, entropy, latency_ms

    def __init__(self, config: Config):
        super().__init__()
        self.config          = config
        self._last_img       = None
        self._dedup: Dict[str, float] = {}
        self._bloom          = BloomFilter()
        self._worker_q: List[APIWorker] = []
        self._active_workers = 0
        self._api_count      = 0
        self._error_count    = 0
        self._last_activity  = time.time()
        self._is_paused      = False
        self._session_start  = time.time()

        self._motion_timer = QTimer()
        self._motion_timer.timeout.connect(self._tick)
        self._motion_timer.start(MOTION_DEBOUNCE)

        self._interval_timer = QTimer()
        self._interval_timer.timeout.connect(self._scheduled_scan)
        self._interval_timer.start(config.interval_ms)

        self._cleanup_timer = QTimer()
        self._cleanup_timer.timeout.connect(self._cleanup_dedup)
        self._cleanup_timer.start(30_000)

        self._heatmap_decay_timer = QTimer()
        self._heatmap_decay_timer.timeout.connect(self._do_heatmap_decay)
        self._heatmap_decay_timer.start(5000)

        # Heatmap initialized lazily on first frame
        self._heatmap: Optional[DetectionHeatmap] = None

    @property
    def api_count(self):   return self._api_count
    @property
    def error_count(self): return self._error_count
    @property
    def uptime_s(self):    return time.time() - self._session_start

    def pause(self):
        self._is_paused = True
        self._last_img  = None

    def resume(self):
        self._is_paused = False
        self._last_activity = time.time()

    def _is_excluded(self, x: int, y: int, w: int, h: int) -> bool:
        """Check if region overlaps any exclusion zone."""
        for zone in self.config.exclusion_zones:
            zx, zy, zw, zh = zone[:4]
            if (x < zx + zw and x + w > zx and
                    y < zy + zh and y + h > zy):
                return True
        return False

    def _tick(self):
        """Motion-based trigger: fires when screen changes."""
        if self._is_paused:
            return
        idle = self.config.auto_pause_idle_s
        if idle > 0 and time.time() - self._last_activity > idle:
            return
        try:
            with mss.mss() as sct:
                monitors = sct.monitors
                idx      = min(self.config.monitor_index, len(monitors) - 1)
                mon      = monitors[idx]
                raw      = sct.grab(mon)
                img      = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")

            if self._heatmap is None:
                self._heatmap = DetectionHeatmap(img.width, img.height)

            if self._last_img is None:
                self._last_img = img
                return

            diff = ImageChops.difference(img, self._last_img)
            bbox = diff.getbbox()
            self._last_img = img

            if not bbox:
                return
            bw = bbox[2] - bbox[0]
            bh = bbox[3] - bbox[1]
            if bw < self.config.motion_min_px or bh < self.config.motion_min_px:
                return

            cropped = img.crop(bbox)
            self._analyze_region(img, cropped, bbox, mon)

        except Exception:
            log.debug(traceback.format_exc())

    def _scheduled_scan(self):
        """Interval-based full-frame re-scan (catches static AI content)."""
        if self._is_paused or self._last_img is None:
            return
        try:
            with mss.mss() as sct:
                monitors = sct.monitors
                idx      = min(self.config.monitor_index, len(monitors) - 1)
                mon      = monitors[idx]
                raw      = sct.grab(mon)
                img      = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")

            # Scan the full screen as a region
            bbox     = (0, 0, img.width, img.height)
            cropped  = img
            self._analyze_region(img, cropped, bbox, mon)
        except Exception:
            log.debug(traceback.format_exc())

    def _analyze_region(self, full_img: Image.Image, cropped: Image.Image,
                        bbox: tuple, mon: dict):
        ph  = phash(cropped)
        ah  = ahash(cropped)
        ent = image_entropy(cropped) if self.config.entropy_filter else 0.0

        # Entropy filter: skip flat/boring regions
        if self.config.entropy_filter and ent < self.config.entropy_min:
            return

        # Exclusion zone check
        bx, by = bbox[0], bbox[1]
        bw, bh = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if self._is_excluded(bx, by, bw, bh):
            return

        # Bloom pre-screen
        if ph in self._bloom:
            # Precise dedup check
            if self.config.dedup_enabled:
                if ph in self._dedup and self._dedup[ph] > time.time():
                    return

        self._bloom.add(ph)
        self._dedup[ph] = time.time() + DEDUP_TTL
        self._last_activity = time.time()

        # Build burst frames
        frames = []
        buf = io.BytesIO()
        cropped.save(buf, format="JPEG", quality=90)
        frames.append(buf.getvalue())

        for i in range(1, self.config.burst_frames):
            pad = 5 * i
            jx  = max(0, bbox[0] - pad)
            jy  = max(0, bbox[1] - pad)
            jx2 = min(full_img.width,  bbox[2] + pad)
            jy2 = min(full_img.height, bbox[3] + pad)
            ex  = full_img.crop((jx, jy, jx2, jy2))
            b2  = io.BytesIO()
            ex.save(b2, format="JPEG", quality=90)
            frames.append(b2.getvalue())

        mon_l = mon.get("left", 0)
        mon_t = mon.get("top",  0)
        coords = [mon_l + bx, mon_t + by, bw, bh]
        self._dispatch(frames, coords, ph, ent, cropped)

    def _dispatch(self, frames: List[bytes], coords: list, ph: str,
                  entropy: float, region_img: Image.Image):
        max_w = self.config.max_workers
        if self._active_workers >= max_w:
            return

        worker = APIWorker(frames, coords, ph, entropy, self.config)
        worker.done.connect(self._on_result)
        worker.error.connect(self._on_error)
        worker.finished.connect(lambda: self._on_worker_done(worker))
        self._active_workers += 1
        self._api_count      += 1
        worker.start()
        self._worker_q.append(worker)

    def _on_worker_done(self, worker: APIWorker):
        self._active_workers = max(0, self._active_workers - 1)
        try:
            self._worker_q.remove(worker)
        except ValueError:
            pass

    def _on_result(self, result: dict, coords: list, ph: str,
                   entropy: float, latency: float):
        score = result.get("type", {}).get("ai_generated", 0.0)
        if score >= self.config.threshold:
            ts = datetime.datetime.now().isoformat(timespec="seconds")
            self.detection.emit(score, *coords, ts, entropy, latency)
            # Heatmap
            if self._heatmap:
                self._heatmap.record(*coords, score)

    def _on_error(self, msg: str, ph: str):
        log.warning(f"API [{ph[:8]}]: {msg}")
        self._error_count += 1
        self._dedup.pop(ph, None)

    def _cleanup_dedup(self):
        now = time.time()
        self._dedup = {k: v for k, v in self._dedup.items() if v > now}

    def _do_heatmap_decay(self):
        if self._heatmap:
            self._heatmap.decay()

    def shutdown(self):
        self._motion_timer.stop()
        self._interval_timer.stop()
        self._cleanup_timer.stop()
        self._heatmap_decay_timer.stop()
        for w in list(self._worker_q):
            w.quit()
            w.wait(2000)

# ══════════════════════════════════════════════════════════════════════════════
#  CONFIG DIALOG  — Full enterprise configuration panel
# ══════════════════════════════════════════════════════════════════════════════
class ConfigDialog(QDialog):
    def __init__(self, config: Config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setWindowTitle(f"AI Sentinel Pro — Configuration")
        self.setMinimumSize(640, 620)
        self.setStyleSheet(BASE_STYLE)

        tabs = QTabWidget()
        tabs.addTab(self._tab_api(),      "🔑  API & Keys")
        tabs.addTab(self._tab_detect(),   "🔍  Detection")
        tabs.addTab(self._tab_badge(),    "🎨  Badge")
        tabs.addTab(self._tab_alerts(),   "🔔  Alerts")
        tabs.addTab(self._tab_archive(),  "📸  Archive")
        tabs.addTab(self._tab_zones(),    "🚫  Exclusions")
        tabs.addTab(self._tab_system(),   "⚙  System")

        bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        bb.accepted.connect(self._accept)
        bb.rejected.connect(self.reject)
        ok_btn = bb.button(QDialogButtonBox.Ok)
        ok_btn.setStyleSheet(mk_btn(C["accent"]))
        cancel_btn = bb.button(QDialogButtonBox.Cancel)
        cancel_btn.setStyleSheet(mk_btn(C["muted"], C["text"]))

        lay = QVBoxLayout(self)
        lay.setContentsMargins(18, 18, 18, 14)
        lay.setSpacing(14)
        lay.addWidget(tabs)
        lay.addWidget(bb)

    # ── helpers ──────────────────────────────────────────────────────────────
    def _fw(self):
        w = QWidget()
        sa = QScrollArea()
        sa.setWidget(w)
        sa.setWidgetResizable(True)
        sa.setFrameShape(QFrame.NoFrame)
        f = QFormLayout(w)
        f.setContentsMargins(22, 18, 22, 18)
        f.setSpacing(14)
        f.setLabelAlignment(Qt.AlignRight | Qt.AlignVCenter)
        return sa, w, f

    def _spin(self, val, lo, hi, suf="", dbl=False):
        if dbl:
            s = QDoubleSpinBox()
            s.setDecimals(2)
            s.setSingleStep(0.01)
        else:
            s = QSpinBox()
        s.setRange(lo, hi)
        s.setValue(val)
        s.setSuffix(suf)
        s.setMinimumWidth(110)
        return s

    def _lbl(self, text: str, color: str = None) -> QLabel:
        l = QLabel(text)
        l.setStyleSheet(f"color: {color or C['sub']}; font-size: 10px;")
        l.setWordWrap(True)
        return l

    def _combo(self, items, current_data=None):
        c = QComboBox()
        for k, v in items:
            c.addItem(k, v)
        if current_data is not None:
            for i in range(c.count()):
                if c.itemData(i) == current_data:
                    c.setCurrentIndex(i)
                    break
        return c

    # ── Tab: API & Keys ──────────────────────────────────────────────────────
    def _tab_api(self):
        sa, w, f = self._fw()
        self._user   = QLineEdit(str(self.config.api_user))
        self._secret = QLineEdit(str(self.config.api_secret))
        self._secret.setEchoMode(QLineEdit.Password)

        show_btn = QPushButton("👁 Show"); show_btn.setStyleSheet(mk_btn(C["muted"], small=True))
        show_btn.setCheckable(True)
        show_btn.toggled.connect(lambda v: self._secret.setEchoMode(
            QLineEdit.Normal if v else QLineEdit.Password))

        sec_row = QHBoxLayout()
        sec_row.addWidget(self._secret, 1)
        sec_row.addWidget(show_btn)
        sec_w = QWidget(); sec_w.setLayout(sec_row)

        self._intv = self._combo(
            [("Ultra Fast (1s)",1000),("Fast (2s)",2000),
             ("Balanced (4s)",4000),("Economy (8s)",8000),
             ("Slow (15s)",15000)],
            self.config.interval_ms
        )
        self._blend = self._combo(
            [("Average", "average"), ("Maximum", "maximum"),
             ("Weighted Average", "weighted_avg"),
             ("Ensemble Vote", "ensemble_vote")],
            self.config.score_blend
        )
        self._max_workers = self._spin(self.config.max_workers, 1, 8, " workers")
        self._retry   = self._spin(self.config.retry_max, 1, 10)
        self._backoff = self._spin(self.config.retry_backoff_ms, 100, 5000, " ms")

        note = self._lbl("🔐 API secret is encrypted at rest using machine-derived key.\n"
                         "Get free keys at sightengine.com/signup  (500 free calls/month)")
        f.addRow("API User:", self._user)
        f.addRow("API Secret:", sec_w)
        f.addRow("Poll Interval:", self._intv)
        f.addRow("Score Blend:", self._blend)
        f.addRow("Max API Workers:", self._max_workers)
        f.addRow("Retry Attempts:", self._retry)
        f.addRow("Retry Backoff:", self._backoff)
        f.addRow("", note)
        return sa

    # ── Tab: Detection ───────────────────────────────────────────────────────
    def _tab_detect(self):
        sa, w, f = self._fw()

        self._mon = QComboBox()
        try:
            with mss.mss() as sct:
                for i, m in enumerate(sct.monitors):
                    lbl = (f"All Monitors ({m['width']}×{m['height']})" if i == 0
                           else f"Monitor {i} — {m['width']}×{m['height']}")
                    self._mon.addItem(lbl, i)
        except Exception:
            self._mon.addItem("Monitor 1", 0)
        self._mon.setCurrentIndex(min(self.config.monitor_index, self._mon.count() - 1))

        # Threshold slider + label
        self._thresh_sl = QSlider(Qt.Horizontal)
        self._thresh_sl.setRange(50, 99)
        self._thresh_sl.setValue(int(self.config.threshold * 100))
        self._thresh_lbl = QLabel(f"{int(self.config.threshold * 100)}%")
        self._thresh_lbl.setStyleSheet(f"color: {C['accent']}; font-weight: bold; min-width: 38px;")
        self._thresh_sl.valueChanged.connect(
            lambda v: self._thresh_lbl.setText(f"{v}%"))
        thresh_row = QHBoxLayout()
        thresh_row.addWidget(self._thresh_sl, 1)
        thresh_row.addWidget(self._thresh_lbl)
        thresh_w = QWidget(); thresh_w.setLayout(thresh_row)

        self._motion   = self._spin(self.config.motion_min_px, 40, 4000, " px")
        self._burst    = self._spin(self.config.burst_frames, 1, 8, " frames")
        self._bgap     = self._spin(self.config.burst_gap_ms, 50, 2000, " ms")
        self._dedup    = QCheckBox("Enable perceptual hash deduplication")
        self._dedup.setChecked(self.config.dedup_enabled)
        self._ham_tol  = self._spin(self.config.dedup_hamming_tolerance, 0, 16, " bits")
        self._ent_ck   = QCheckBox("Enable entropy pre-filter (skip low-complexity regions)")
        self._ent_ck.setChecked(self.config.entropy_filter)
        self._ent_min  = self._spin(self.config.entropy_min, 1.0, 8.0, "", dbl=True)

        f.addRow("Monitor:", self._mon)
        f.addRow("AI Threshold:", thresh_w)
        f.addRow("Min Motion Region:", self._motion)
        f.addRow("Burst Frames:", self._burst)
        f.addRow("Burst Gap:", self._bgap)
        f.addRow("", self._dedup)
        f.addRow("Hash Tolerance:", self._ham_tol)
        f.addRow("", self._ent_ck)
        f.addRow("Min Entropy:", self._ent_min)
        f.addRow("", self._lbl("Higher entropy → more complex images. Typical photos: 6-8, AI art: 5-7, solid fills: <3"))
        return sa

    # ── Tab: Badge ───────────────────────────────────────────────────────────
    def _tab_badge(self):
        sa, w, f = self._fw()

        self._bstyle = self._combo(
            [(v, k) for k, v in BADGE_STYLES.items()],
            self.config.badge_style
        )

        self._bsz_sl = QSlider(Qt.Horizontal)
        self._bsz_sl.setRange(28, 96)
        self._bsz_sl.setValue(self.config.badge_size)
        self._bsz_lbl = QLabel(f"{self.config.badge_size}px")
        self._bsz_lbl.setStyleSheet(f"color:{C['accent']}; font-weight:bold; min-width:40px;")
        self._bsz_sl.valueChanged.connect(lambda v: self._bsz_lbl.setText(f"{v}px"))
        bsz_row = QHBoxLayout()
        bsz_row.addWidget(self._bsz_sl, 1); bsz_row.addWidget(self._bsz_lbl)
        bsz_w = QWidget(); bsz_w.setLayout(bsz_row)

        self._bop_sl = QSlider(Qt.Horizontal)
        self._bop_sl.setRange(30, 100)
        self._bop_sl.setValue(int(self.config.badge_opacity * 100))
        self._bop_lbl = QLabel(f"{int(self.config.badge_opacity * 100)}%")
        self._bop_lbl.setStyleSheet(f"color:{C['accent']}; font-weight:bold; min-width:38px;")
        self._bop_sl.valueChanged.connect(lambda v: self._bop_lbl.setText(f"{v}%"))
        bop_row = QHBoxLayout()
        bop_row.addWidget(self._bop_sl, 1); bop_row.addWidget(self._bop_lbl)
        bop_w = QWidget(); bop_w.setLayout(bop_row)

        self._hold = self._spin(self.config.badge_hold_ms, 1000, 30000, " ms")
        self._fade = self._spin(self.config.badge_fade_ms, 300, 5000, " ms")
        self._pulse = QCheckBox("Pulse animation while badge is active")
        self._pulse.setChecked(self.config.badge_pulse)
        self._bsound = QCheckBox("Play system sound on detection")
        self._bsound.setChecked(self.config.badge_sound)

        f.addRow("Badge Style:", self._bstyle)
        f.addRow("Badge Size:", bsz_w)
        f.addRow("Badge Opacity:", bop_w)
        f.addRow("Hold Duration:", self._hold)
        f.addRow("Fade Duration:", self._fade)
        f.addRow("", self._pulse)
        f.addRow("", self._bsound)
        return sa

    # ── Tab: Alerts ──────────────────────────────────────────────────────────
    def _tab_alerts(self):
        sa, w, f = self._fw()

        self._notify = QCheckBox("Desktop OS notification on detection")
        self._notify.setChecked(self.config.desktop_notify)

        self._wh_en  = QCheckBox("Enable webhook alerts")
        self._wh_en.setChecked(self.config.webhook_enabled)

        self._wh_url = QLineEdit(str(self.config.webhook_url))
        self._wh_url.setPlaceholderText("https://hooks.slack.com/services/…")

        self._wh_type = self._combo(
            [("Slack Webhook", "slack"),
             ("MS Teams Webhook", "teams"),
             ("Custom HTTP POST (JSON)", "custom")],
            self.config.webhook_type
        )

        self._wh_thresh_sl = QSlider(Qt.Horizontal)
        self._wh_thresh_sl.setRange(50, 99)
        self._wh_thresh_sl.setValue(int(self.config.webhook_threshold * 100))
        self._wh_thresh_lbl = QLabel(f"{int(self.config.webhook_threshold * 100)}%")
        self._wh_thresh_lbl.setStyleSheet(f"color:{C['warn']}; font-weight:bold; min-width:38px;")
        self._wh_thresh_sl.valueChanged.connect(
            lambda v: self._wh_thresh_lbl.setText(f"{v}%"))
        wh_row = QHBoxLayout()
        wh_row.addWidget(self._wh_thresh_sl, 1); wh_row.addWidget(self._wh_thresh_lbl)
        wh_w = QWidget(); wh_w.setLayout(wh_row)

        test_btn = QPushButton("📤  Send Test Webhook")
        test_btn.setStyleSheet(mk_btn(C["warn_d"], small=True))
        test_btn.clicked.connect(self._test_webhook)

        f.addRow("", self._notify)
        f.addRow("", self._wh_en)
        f.addRow("Webhook URL:", self._wh_url)
        f.addRow("Webhook Type:", self._wh_type)
        f.addRow("Min Score for Alert:", wh_w)
        f.addRow("", test_btn)
        return sa

    def _test_webhook(self):
        det = Detection(
            ts_str=datetime.datetime.now().isoformat(),
            score=0.95, score_pct=95, is_ai=True,
            w=400, h=300, x=100, y=100,
            blend_mode=self.config.score_blend,
        )
        cfg_tmp = copy.deepcopy(self.config)
        cfg_tmp.webhook_url     = self._wh_url.text().strip()
        cfg_tmp.webhook_type    = self._wh_type.currentData()
        cfg_tmp.webhook_enabled = True
        cfg_tmp.webhook_threshold = 0.0
        notifier = WebhookNotifier(cfg_tmp)
        notifier.enqueue(det)
        QMessageBox.information(self, "Test Webhook", "Test payload dispatched — check your endpoint.")

    # ── Tab: Archive ─────────────────────────────────────────────────────────
    def _tab_archive(self):
        sa, w, f = self._fw()

        self._snap_en = QCheckBox("Save screenshot of detected region")
        self._snap_en.setChecked(self.config.snapshot_enabled)
        self._snap_ret = self._spin(self.config.snapshot_retention, 10, 5000, " images")
        self._log_en   = QCheckBox("Enable detection log")
        self._log_en.setChecked(self.config.log_enabled)
        self._max_log  = self._spin(self.config.max_log, 100, 10000, " entries")

        open_snaps = QPushButton("📂  Open Snapshot Folder")
        open_snaps.setStyleSheet(mk_btn(C["muted"], small=True))
        open_snaps.clicked.connect(lambda: self._open_path(SNAPSHOT_DIR))

        open_cfg = QPushButton("📂  Open Config Folder")
        open_cfg.setStyleSheet(mk_btn(C["muted"], small=True))
        open_cfg.clicked.connect(lambda: self._open_path(CONFIG_DIR))

        f.addRow("", self._snap_en)
        f.addRow("Max Snapshots:", self._snap_ret)
        f.addRow("", self._log_en)
        f.addRow("Max Log Entries:", self._max_log)
        f.addRow("", open_snaps)
        f.addRow("", open_cfg)
        f.addRow("", self._lbl(f"Snapshot dir: {SNAPSHOT_DIR}\nDB: {DB_FILE}"))
        return sa

    def _open_path(self, p: Path):
        try:
            opener = "xdg-open" if sys.platform.startswith("linux") else \
                     "open" if sys.platform == "darwin" else "explorer"
            subprocess.Popen([opener, str(p)], stderr=subprocess.DEVNULL)
        except Exception:
            pass

    # ── Tab: Exclusion Zones ─────────────────────────────────────────────────
    def _tab_zones(self):
        sa, w, f = self._fw()
        note = self._lbl(
            "Add screen regions to exclude from monitoring (e.g. taskbar, watermark areas).\n"
            "Format: X, Y, Width, Height  (pixels from top-left of monitor)"
        )
        f.addRow("", note)

        self._zones_list = QListWidget()
        self._zones_list.setMinimumHeight(140)
        for z in self.config.exclusion_zones:
            self._zones_list.addItem(f"{z[0]}, {z[1]}, {z[2]}, {z[3]}")

        zone_inputs = QHBoxLayout()
        self._zx = self._spin(0, 0, 9999, " X")
        self._zy = self._spin(0, 0, 9999, " Y")
        self._zw = self._spin(200, 1, 9999, " W")
        self._zh = self._spin(100, 1, 9999, " H")
        for s in [self._zx, self._zy, self._zw, self._zh]:
            zone_inputs.addWidget(s)
        zone_inp_w = QWidget(); zone_inp_w.setLayout(zone_inputs)

        add_btn = QPushButton("+ Add Zone"); add_btn.setStyleSheet(mk_btn(C["ok_d"], small=True))
        del_btn = QPushButton("− Remove");   del_btn.setStyleSheet(mk_btn(C["danger_d"], small=True))
        clr_btn = QPushButton("✕ Clear All"); clr_btn.setStyleSheet(mk_btn(C["muted"], small=True))
        add_btn.clicked.connect(self._add_zone)
        del_btn.clicked.connect(self._del_zone)
        clr_btn.clicked.connect(self._zones_list.clear)
        btn_row = QHBoxLayout()
        for b in [add_btn, del_btn, clr_btn]: btn_row.addWidget(b)
        btn_w = QWidget(); btn_w.setLayout(btn_row)

        f.addRow("Zones:", self._zones_list)
        f.addRow("Add:", zone_inp_w)
        f.addRow("", btn_w)
        return sa

    def _add_zone(self):
        x, y = self._zx.value(), self._zy.value()
        w, h = self._zw.value(), self._zh.value()
        self._zones_list.addItem(f"{x}, {y}, {w}, {h}")

    def _del_zone(self):
        for item in self._zones_list.selectedItems():
            self._zones_list.takeItem(self._zones_list.row(item))

    # ── Tab: System ──────────────────────────────────────────────────────────
    def _tab_system(self):
        sa, w, f = self._fw()

        self._autostart = QCheckBox("Launch at system startup")
        self._autostart.setChecked(self.config.autostart)
        self._idle = self._spin(self.config.auto_pause_idle_s, 0, 3600, " s")

        f.addRow("", self._autostart)
        f.addRow("Auto-pause idle timeout:", self._idle)
        f.addRow("", self._lbl("Set to 0 to disable auto-pause\nConfig: " + str(CONFIG_FILE)))
        return sa

    # ── Accept ───────────────────────────────────────────────────────────────
    def _accept(self):
        c = self.config
        c.api_user              = self._user.text().strip()
        c.api_secret            = self._secret.text().strip()
        c.interval_ms           = self._intv.currentData()
        c.score_blend           = self._blend.currentData()
        c.max_workers           = self._max_workers.value()
        c.retry_max             = self._retry.value()
        c.retry_backoff_ms      = self._backoff.value()
        c.threshold             = self._thresh_sl.value() / 100.0
        c.monitor_index         = self._mon.currentData()
        c.motion_min_px         = self._motion.value()
        c.burst_frames          = self._burst.value()
        c.burst_gap_ms          = self._bgap.value()
        c.dedup_enabled         = self._dedup.isChecked()
        c.dedup_hamming_tolerance = self._ham_tol.value()
        c.entropy_filter        = self._ent_ck.isChecked()
        c.entropy_min           = float(self._ent_min.value())
        c.badge_style           = self._bstyle.currentData()
        c.badge_size            = self._bsz_sl.value()
        c.badge_opacity         = self._bop_sl.value() / 100.0
        c.badge_hold_ms         = self._hold.value()
        c.badge_fade_ms         = self._fade.value()
        c.badge_pulse           = self._pulse.isChecked()
        c.badge_sound           = self._bsound.isChecked()
        c.desktop_notify        = self._notify.isChecked()
        c.webhook_enabled       = self._wh_en.isChecked()
        c.webhook_url           = self._wh_url.text().strip()
        c.webhook_type          = self._wh_type.currentData()
        c.webhook_threshold     = self._wh_thresh_sl.value() / 100.0
        c.snapshot_enabled      = self._snap_en.isChecked()
        c.snapshot_retention    = self._snap_ret.value()
        c.log_enabled           = self._log_en.isChecked()
        c.max_log               = self._max_log.value()
        c.auto_pause_idle_s     = self._idle.value()

        # Exclusion zones
        zones = []
        for i in range(self._zones_list.count()):
            try:
                parts = [int(x.strip()) for x in self._zones_list.item(i).text().split(",")]
                if len(parts) == 4:
                    zones.append(parts)
            except Exception:
                pass
        c.exclusion_zones = zones

        autostart_changed = c.autostart != self._autostart.isChecked()
        c.autostart = self._autostart.isChecked()

        errs = c.validate()
        if errs:
            QMessageBox.warning(self, "Validation", "\n".join(errs))
            return

        c.save()
        if autostart_changed:
            if c.autostart: Autostart.install()
            else:           Autostart.uninstall()

        self.accept()

# ══════════════════════════════════════════════════════════════════════════════
#  SPARKLINE WIDGET
# ══════════════════════════════════════════════════════════════════════════════
class SparklineWidget(QWidget):
    """Renders a mini score trend line with fill."""

    def __init__(self, color: str = None, parent=None):
        super().__init__(parent)
        self._data: List[float] = []
        self._color = QColor(color or C["accent"])
        self.setMinimumSize(120, 40)

    def set_data(self, data: List[float]):
        self._data = data[-120:]
        self.update()

    def paintEvent(self, _):
        if len(self._data) < 2:
            return
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        W, H = self.width(), self.height()
        pts  = self._data
        mn, mx = 0.0, 1.0  # always 0-1 for AI scores
        if mx == mn: return

        def px(i, v):
            x = int(i / (len(pts) - 1) * (W - 2)) + 1
            y = H - int((v - mn) / (mx - mn) * (H - 4)) - 2
            return QPointF(x, y)

        path = QPainterPath()
        path.moveTo(px(0, pts[0]))
        for i in range(1, len(pts)):
            path.lineTo(px(i, pts[i]))

        # Fill
        fill = QPainterPath(path)
        fill.lineTo(px(len(pts) - 1, mn))
        fill.lineTo(px(0, mn))
        fill.closeSubpath()
        grad = QLinearGradient(0, 0, 0, H)
        c = self._color
        grad.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 80))
        grad.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        p.fillPath(fill, QBrush(grad))

        # Line
        pen = QPen(self._color, 1.5)
        p.setPen(pen)
        p.drawPath(path)

        # Last value dot
        last = px(len(pts) - 1, pts[-1])
        p.setBrush(QBrush(self._color))
        p.setPen(Qt.NoPen)
        p.drawEllipse(last, 3, 3)

        p.end()

# ══════════════════════════════════════════════════════════════════════════════
#  HEATMAP WIDGET
# ══════════════════════════════════════════════════════════════════════════════
class HeatmapWidget(QWidget):
    """Renders a color-coded density heatmap of detections."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._grid: List[List[float]] = []
        self._max_val = 0.0
        self.setMinimumSize(300, 180)

    def update_data(self, grid: List[List[float]], max_val: float):
        self._grid    = grid
        self._max_val = max_val or 1.0
        self.update()

    def paintEvent(self, _):
        if not self._grid:
            p = QPainter(self)
            p.fillRect(self.rect(), QColor(C["surface"]))
            p.setPen(QColor(C["sub"]))
            p.drawText(self.rect(), Qt.AlignCenter, "No data yet")
            p.end()
            return

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        rows = len(self._grid)
        cols = len(self._grid[0]) if rows else 0
        if not cols:
            return
        cw = self.width()  / cols
        ch = self.height() / rows

        for r in range(rows):
            for c in range(cols):
                v = self._grid[r][c] / self._max_val
                # Color: blue → cyan → green → yellow → red
                if v < 0.25:
                    col = QColor(0, int(v * 4 * 200), 255)
                elif v < 0.5:
                    t = (v - 0.25) * 4
                    col = QColor(0, int(200 + t * 55), int(255 * (1 - t)))
                elif v < 0.75:
                    t = (v - 0.5) * 4
                    col = QColor(int(t * 255), 255, 0)
                else:
                    t = (v - 0.75) * 4
                    col = QColor(255, int(255 * (1 - t)), 0)
                col.setAlpha(max(20, int(v * 220)))
                p.fillRect(int(c * cw), int(r * ch), int(cw) + 1, int(ch) + 1,
                           QBrush(col))

        p.setPen(QColor(C["border"]))
        p.drawRect(0, 0, self.width() - 1, self.height() - 1)
        p.end()

# ══════════════════════════════════════════════════════════════════════════════
#  STATS DASHBOARD  — Comprehensive monitoring center
# ══════════════════════════════════════════════════════════════════════════════
class StatsDashboard(QDialog):

    def __init__(self, db: DetectionDB, monitor: ScreenMonitor,
                 config: Config, parent=None):
        super().__init__(parent)
        self.db      = db
        self.monitor = monitor
        self.config  = config
        self.setWindowTitle(f"AI Sentinel Pro — Intelligence Dashboard")
        self.setMinimumSize(1020, 740)
        self.setStyleSheet(BASE_STYLE)

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Header bar ───────────────────────────────────────────────────────
        hdr = QWidget()
        hdr.setFixedHeight(52)
        hdr.setStyleSheet(f"background: {C['bg2']}; border-bottom: 1px solid {C['border']};")
        hl = QHBoxLayout(hdr)
        hl.setContentsMargins(24, 0, 24, 0)
        title = QLabel("⚡ AI SENTINEL PRO — INTELLIGENCE DASHBOARD")
        title.setStyleSheet(f"color:{C['accent']}; font-size:13px; font-weight:bold; letter-spacing:2px;")
        ver_lbl = QLabel(f"v{APP_VERSION}")
        ver_lbl.setStyleSheet(f"color:{C['sub']}; font-size:10px;")
        self._status_led = QLabel("● ACTIVE")
        self._status_led.setStyleSheet(f"color:{C['ok']}; font-size:11px; font-weight:bold;")
        hl.addWidget(title); hl.addStretch()
        hl.addWidget(self._status_led); hl.addSpacing(20); hl.addWidget(ver_lbl)
        root.addWidget(hdr)

        # ── Stat cards row ───────────────────────────────────────────────────
        cards_bar = QWidget()
        cards_bar.setStyleSheet(f"background:{C['bg2']}; border-bottom:1px solid {C['border']};")
        cl = QHBoxLayout(cards_bar); cl.setContentsMargins(16, 10, 16, 10); cl.setSpacing(10)
        self._cards = {}
        card_defs = [
            ("today",   "TODAY",        C["danger"]),
            ("h24",     "LAST 24H",     C["warn"]),
            ("ai",      "TOTAL AI",     C["accent"]),
            ("real",    "REAL CONTENT", C["ok"]),
            ("avg",     "AVG SCORE",    C["info"]),
            ("maximum", "PEAK SCORE",   C["gold"]),
            ("api",     "API CALLS",    C["purple"]),
            ("errors",  "ERRORS",       C["sub"]),
            ("uptime",  "UPTIME",       C["teal"]),
        ]
        for key, lbl, col in card_defs:
            card = QFrame()
            card.setStyleSheet(
                f"background:{C['surface']}; border:1px solid {C['border']}; "
                f"border-radius:8px;"
            )
            card.setMinimumWidth(88)
            cv = QVBoxLayout(card); cv.setContentsMargins(12, 9, 12, 9); cv.setSpacing(2)
            v = QLabel("—"); v.setStyleSheet(f"color:{col}; font-size:20px; font-weight:bold;")
            s = QLabel(lbl); s.setStyleSheet(f"color:{C['sub']}; font-size:9px; letter-spacing:1.5px;")
            cv.addWidget(v); cv.addWidget(s)
            self._cards[key] = v
            cl.addWidget(card)
        root.addWidget(cards_bar)

        # ── Main tabs ────────────────────────────────────────────────────────
        body = QWidget()
        bl   = QVBoxLayout(body); bl.setContentsMargins(16, 14, 16, 8); bl.setSpacing(10)

        tabs = QTabWidget()
        tabs.addTab(self._tab_log(),       "📋  Detection Log")
        tabs.addTab(self._tab_timeline(),  "📈  Timeline")
        tabs.addTab(self._tab_heatmap(),   "🗺  Heatmap")
        tabs.addTab(self._tab_snapshots(), "📸  Snapshots")
        tabs.addTab(self._tab_costs(),     "💲  Cost Tracker")
        bl.addWidget(tabs)

        # ── Bottom action bar ─────────────────────────────────────────────────
        bot = QHBoxLayout(); bot.setSpacing(8)
        for lbl, fn, col in [
            ("⟳  Refresh",      self._refresh,      C["muted"]),
            ("↓  Export CSV",   self._export_csv,   C["ok_d"]),
            ("↓  Export JSON",  self._export_json,  C["ok_d"]),
            ("🗑  Clear Log",   self._clear_log,    C["danger_d"]),
        ]:
            b = QPushButton(lbl)
            b.setStyleSheet(mk_btn(col, "#fff", small=True))
            b.clicked.connect(fn)
            bot.addWidget(b)
        bot.addStretch()
        close_btn = QPushButton("✕  Close")
        close_btn.setStyleSheet(mk_btn(C["muted"], C["text"], small=True))
        close_btn.clicked.connect(self.close)
        bot.addWidget(close_btn)
        bl.addLayout(bot)

        root.addWidget(body, 1)

        # Auto-refresh
        self._refresh_timer = QTimer(self)
        self._refresh_timer.timeout.connect(self._refresh)
        self._refresh_timer.start(8000)
        self._refresh()

    # ── Log tab ──────────────────────────────────────────────────────────────
    def _tab_log(self):
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(0, 8, 0, 0); l.setSpacing(6)

        # Filter bar
        fbar = QHBoxLayout()
        self._filter_edit = QLineEdit(); self._filter_edit.setPlaceholderText("Filter by process, score, time…")
        self._filter_edit.textChanged.connect(self._apply_filter)
        self._ai_only_ck = QCheckBox("AI only"); self._ai_only_ck.setChecked(True)
        self._ai_only_ck.stateChanged.connect(self._refresh)
        fbar.addWidget(QLabel("Filter:")); fbar.addWidget(self._filter_edit, 1)
        fbar.addWidget(self._ai_only_ck)
        fbar_w = QWidget(); fbar_w.setLayout(fbar)
        l.addWidget(fbar_w)

        self.table = QTableWidget(0, 9)
        self.table.setHorizontalHeaderLabels([
            "Time", "Score", "Blend", "Result", "Region",
            "Entropy", "Latency", "Process", "Hash"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        l.addWidget(self.table, 1)
        return w

    def _apply_filter(self):
        term = self._filter_edit.text().strip().lower()
        for r in range(self.table.rowCount()):
            match = not term or any(
                term in (self.table.item(r, c).text().lower() if self.table.item(r, c) else "")
                for c in range(self.table.columnCount())
            )
            self.table.setRowHidden(r, not match)

    # ── Timeline tab ─────────────────────────────────────────────────────────
    def _tab_timeline(self):
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(0, 8, 0, 0); l.setSpacing(8)

        tl_header = QLabel("  Score trend (last 120 detections)")
        tl_header.setStyleSheet(f"color:{C['sub']}; font-size:10px; letter-spacing:1.5px;")
        self._spark = SparklineWidget(C["danger"])
        self._spark.setMinimumHeight(80)
        l.addWidget(tl_header)
        l.addWidget(self._spark)

        sep = QFrame(); sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet(f"color:{C['border']};")
        l.addWidget(sep)

        self.tl_text = QTextEdit(); self.tl_text.setReadOnly(True)
        self.tl_text.setFont(QFont("JetBrains Mono", 10))
        l.addWidget(self.tl_text, 1)
        return w

    # ── Heatmap tab ──────────────────────────────────────────────────────────
    def _tab_heatmap(self):
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(0, 8, 0, 0)
        note = QLabel("  Detection density heatmap — warmer = more AI content detected in region")
        note.setStyleSheet(f"color:{C['sub']}; font-size:10px;")
        l.addWidget(note)
        self._heatmap_widget = HeatmapWidget()
        l.addWidget(self._heatmap_widget, 1)
        return w

    # ── Snapshots tab ────────────────────────────────────────────────────────
    def _tab_snapshots(self):
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(0, 8, 0, 0); l.setSpacing(8)
        if not self.config.snapshot_enabled:
            note = QLabel("  Snapshot archiving is disabled.\n  Enable it in Configuration → Archive.")
            note.setStyleSheet(f"color:{C['sub']}; font-size:11px;")
            l.addWidget(note)
            return w

        self._snap_list = QListWidget()
        self._snap_list.setAlternatingRowColors(True)
        snaps = SnapshotArchive(self.config).list_all()
        for p in snaps:
            sz = p.stat().st_size // 1024
            self._snap_list.addItem(f"{p.name}  ({sz}KB)")

        open_btn = QPushButton("📂  Open Selected")
        open_btn.setStyleSheet(mk_btn(C["accent_d"], small=True))
        open_btn.clicked.connect(self._open_snapshot)
        l.addWidget(self._snap_list, 1)
        l.addWidget(open_btn)
        return w

    def _open_snapshot(self):
        sel = self._snap_list.currentItem()
        if not sel:
            return
        name = sel.text().split("  ")[0]
        path = SNAPSHOT_DIR / name
        try:
            opener = "xdg-open" if sys.platform.startswith("linux") else \
                     "open" if sys.platform == "darwin" else "start"
            subprocess.Popen([opener, str(path)], stderr=subprocess.DEVNULL)
        except Exception:
            pass

    # ── Cost Tracker tab ──────────────────────────────────────────────────────
    def _tab_costs(self):
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(16, 16, 16, 16); l.setSpacing(16)
        self._cost_label = QLabel()
        self._cost_label.setStyleSheet(f"color:{C['text']}; font-size:12px;")
        self._cost_label.setWordWrap(True)
        l.addWidget(self._cost_label)
        l.addStretch()
        return w

    # ── Refresh ───────────────────────────────────────────────────────────────
    def _refresh(self):
        s = self.db.stats()
        up = int(self.monitor.uptime_s)
        hh, mm = divmod(up // 60, 60)

        self._cards["today"].setText(str(s["today"]))
        self._cards["h24"].setText(str(s["h24"]))
        self._cards["ai"].setText(str(s["ai"]))
        self._cards["real"].setText(str(s["real"]))
        self._cards["avg"].setText(f"{s['avg']*100:.1f}%")
        self._cards["maximum"].setText(f"{s['maximum']*100:.1f}%")
        self._cards["api"].setText(str(self.monitor.api_count))
        self._cards["errors"].setText(str(self.monitor.error_count))
        self._cards["uptime"].setText(f"{hh}h{mm:02d}m")

        # Table
        ai_only = self._ai_only_ck.isChecked()
        entries = self.db.entries(limit=500, ai_only=ai_only)
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        for det in entries:
            r = self.table.rowCount(); self.table.insertRow(r)
            col = C["danger"] if det.is_ai else C["ok"]
            vals = [
                det.ts_str,
                f"{det.score_pct}%",
                det.blend_mode,
                "🔴 AI" if det.is_ai else "🟢 REAL",
                f"{det.w}×{det.h} @({det.x},{det.y})",
                f"{det.entropy:.2f}" if det.entropy else "—",
                f"{det.api_latency_ms:.0f}ms" if det.api_latency_ms else "—",
                det.process_name or "—",
                (det.phash or "")[:10],
            ]
            for c, val in enumerate(vals):
                item = QTableWidgetItem(str(val))
                if c == 3:
                    item.setForeground(QColor(col))
                self.table.setItem(r, c, item)
        self.table.setSortingEnabled(True)
        self._apply_filter()

        # Sparkline
        series = self.db.score_series()
        self._spark.set_data(series)

        # Timeline text
        buckets = self.db.hourly_buckets(days=3)
        lines   = []
        for h in sorted(buckets.keys()):
            cnt = buckets[h]
            bar = "█" * min(cnt, 48)
            lines.append(f"  {h}:00   {bar}  {cnt}")
        self.tl_text.setPlainText(
            "\n".join(lines) if lines else "  No AI detections recorded yet."
        )

        # Heatmap
        if self.monitor._heatmap:
            grid = self.monitor._heatmap.snapshot()
            mv   = self.monitor._heatmap.max_val()
            self._heatmap_widget.update_data(grid, mv)

        # Cost tracker
        est = self.config.cost_estimate(self.monitor.api_count)
        self._cost_label.setText(
            f"API Calls This Session:  {est['calls']}\n"
            f"Free Tier Used:          {est['free']} / {FREE_CALLS_PER_MONTH}\n"
            f"Billable Calls:          {est['billable']}\n"
            f"Estimated Cost (USD):    ${est['cost_usd']:.4f}\n\n"
            f"Rate: ${COST_PER_CALL_USD}/call beyond free tier\n"
            f"Free calls reset monthly on your Sightengine dashboard."
        )

    # ── Actions ──────────────────────────────────────────────────────────────
    def _export_csv(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Export CSV", str(EXPORT_DIR / "detections.csv"), "CSV (*.csv)")
        if path:
            ok = self.db.export_csv(path)
            QMessageBox.information(self, "Export", "CSV exported." if ok else "No data or error.")

    def _export_json(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Export JSON", str(EXPORT_DIR / "detections.json"), "JSON (*.json)")
        if path:
            ok = self.db.export_json(path)
            QMessageBox.information(self, "Export", "JSON exported." if ok else "No data or error.")

    def _clear_log(self):
        if QMessageBox.question(
            self, "Clear Log",
            "Permanently delete all detection history?\nThis cannot be undone.",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            self.db.clear()
            self._refresh()

# ══════════════════════════════════════════════════════════════════════════════
#  SENTINEL — Main Controller
# ══════════════════════════════════════════════════════════════════════════════
class Sentinel(QObject):
    """Invisible orchestrator living entirely in the system tray."""

    def __init__(self):
        super().__init__()
        self.config   = Config()
        self.db       = DetectionDB(self.config)
        self.archive  = SnapshotArchive(self.config)
        self.badges   = BadgeManager(self.config)
        self.monitor  = ScreenMonitor(self.config)
        self.webhook  = WebhookNotifier(self.config)
        self._paused  = False
        self._det_count_session = 0

        self.monitor.detection.connect(self._on_detection)

        self._setup_tray()
        log.info(f"{APP_NAME} v{APP_VERSION} started  |  threshold={int(self.config.threshold*100)}%  "
                 f"blend={self.config.score_blend}  style={self.config.badge_style}")

        if self.config.autostart and sys.platform.startswith("linux"):
            Autostart.install()

    # ── Tray icon ─────────────────────────────────────────────────────────────
    def _make_icon(self, state: str = "on") -> QIcon:
        sz = 32
        px = QPixmap(sz, sz); px.fill(Qt.transparent)
        p  = QPainter(px)
        p.setRenderHint(QPainter.Antialiasing)

        palettes = {
            "on":      ("#ff2060", "#ff6090"),
            "off":     ("#3a3a60", "#5a5a80"),
            "detect":  ("#ff9000", "#ffcc44"),
            "error":   ("#cc0000", "#ff4444"),
            "paused":  ("#2a4a80", "#4a70c0"),
        }
        c1, c2 = palettes.get(state, palettes["on"])

        # Outer ring
        ring = QRadialGradient(sz / 2, sz / 2, sz / 2)
        ring.setColorAt(0.7, QColor(c1 + "30"))
        ring.setColorAt(1.0, QColor(c1 + "00"))
        p.setBrush(QBrush(ring)); p.setPen(Qt.NoPen)
        p.drawEllipse(0, 0, sz, sz)

        # Circle
        gr = QLinearGradient(3, 3, sz - 3, sz - 3)
        gr.setColorAt(0, QColor(c1)); gr.setColorAt(1, QColor(c2))
        p.setBrush(QBrush(gr))
        p.setPen(QPen(QColor(255, 255, 255, 40), 1.0))
        p.drawEllipse(3, 3, sz - 6, sz - 6)

        # Label
        p.setPen(QColor(255, 255, 255, 220))
        p.setFont(QFont("Arial Black", 9, QFont.Black))
        p.drawText(px.rect(), Qt.AlignCenter, "AI")
        p.end()
        return QIcon(px)

    def _setup_tray(self):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self._make_icon("on"))
        self.tray.setToolTip(f"{APP_NAME} — Monitoring")
        self.tray.activated.connect(self._on_tray_activated)

        menu = QMenu()

        # Header (non-clickable)
        hdr = QAction(f"{APP_NAME}  ·  v{APP_VERSION}", menu)
        hdr.setEnabled(False)
        menu.addAction(hdr)
        menu.addSeparator()

        self._pause_act = QAction("⏸  Pause Monitoring", menu)
        self._pause_act.triggered.connect(self.toggle_pause)
        menu.addAction(self._pause_act)

        dash_act = QAction("📊  Open Dashboard…", menu)
        dash_act.triggered.connect(self._open_dashboard)
        menu.addAction(dash_act)

        clear_act = QAction("🧹  Clear All Badges", menu)
        clear_act.triggered.connect(self.badges.clear_all)
        menu.addAction(clear_act)

        menu.addSeparator()

        cfg_act = QAction("⚙  Configuration…", menu)
        cfg_act.triggered.connect(self._open_config)
        menu.addAction(cfg_act)

        csv_act = QAction("↓  Export CSV…", menu)
        csv_act.triggered.connect(self._quick_export_csv)
        menu.addAction(csv_act)

        log_act = QAction("📄  Open System Log…", menu)
        log_act.triggered.connect(lambda: subprocess.Popen(
            ["xdg-open" if sys.platform.startswith("linux")
             else "open" if sys.platform == "darwin"
             else "notepad", str(SYSLOG_FILE)],
            stderr=subprocess.DEVNULL
        ))
        menu.addAction(log_act)

        menu.addSeparator()

        about_act = QAction(f"ℹ  {APP_NAME} — {APP_BUILD}", menu)
        about_act.setEnabled(False)
        menu.addAction(about_act)

        quit_act = QAction("✕  Quit", menu)
        quit_act.triggered.connect(self._quit)
        menu.addAction(quit_act)

        self.tray.setContextMenu(menu)
        self.tray.show()

        # Tray tooltip updater
        self._tray_timer = QTimer()
        self._tray_timer.timeout.connect(self._update_tray)
        self._tray_timer.start(7000)

    def _on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self._open_dashboard()

    def _update_tray(self):
        s     = self.db.stats()
        state = "paused" if self._paused else "on"
        self.tray.setIcon(self._make_icon(state))
        errs  = self.monitor.error_count
        up    = int(self.monitor.uptime_s)
        hh, mm = divmod(up // 60, 60)
        self.tray.setToolTip(
            f"{APP_NAME}  {'[PAUSED]' if self._paused else '[ACTIVE]'}\n"
            f"Today: {s['today']} AI  |  24h: {s['h24']} AI\n"
            f"API calls: {self.monitor.api_count}  |  Errors: {errs}\n"
            f"Session detections: {self._det_count_session}  |  Uptime: {hh}h{mm:02d}m"
        )

    # ── Detection ─────────────────────────────────────────────────────────────
    def _on_detection(self, score: float, x: int, y: int, w: int, h: int,
                      ts: str, entropy: float, latency: float):
        pct = int(score * 100)
        proc = get_active_process()
        log.info(f"AI detected  score={pct}%  region=[{x},{y},{w}×{h}]  "
                 f"entropy={entropy:.2f}  latency={latency:.0f}ms  proc={proc!r}")

        self._det_count_session += 1

        # Badge
        self.badges.spawn(score, x, y, w, h)

        # Flash tray
        self.tray.setIcon(self._make_icon("detect"))
        QTimer.singleShot(1800, lambda: self.tray.setIcon(
            self._make_icon("paused" if self._paused else "on")))

        # Build detection record
        det = Detection(
            ts=time.time(), ts_str=ts,
            score=score, score_pct=pct, is_ai=True,
            threshold_pct=int(self.config.threshold * 100),
            x=x, y=y, w=w, h=h,
            blend_mode=self.config.score_blend,
            process_name=proc,
            entropy=entropy, api_latency_ms=latency,
        )

        # Save to DB
        self.db.add(det)

        # Webhook
        self.webhook.enqueue(det)

        # OS notification
        if self.config.desktop_notify:
            threading.Thread(
                target=notify_os,
                args=(f"AI Content Detected — {pct}%",
                      f"Confidence: {pct}%  |  Region: {w}×{h}px"),
                daemon=True,
            ).start()

        # Sound
        if self.config.badge_sound:
            threading.Thread(target=beep, daemon=True).start()

    # ── Controls ──────────────────────────────────────────────────────────────
    def toggle_pause(self):
        self._paused = not self._paused
        if self._paused:
            self.monitor.pause()
            self._pause_act.setText("▶  Resume Monitoring")
            self.tray.setIcon(self._make_icon("paused"))
            self.badges.clear_all()
            log.info("Monitoring paused.")
        else:
            self.monitor.resume()
            self._pause_act.setText("⏸  Pause Monitoring")
            self.tray.setIcon(self._make_icon("on"))
            log.info("Monitoring resumed.")

    def _open_config(self):
        dlg = ConfigDialog(self.config)
        if dlg.exec_():
            # Apply live config changes
            self.monitor._motion_timer.setInterval(MOTION_DEBOUNCE)
            self.monitor._interval_timer.setInterval(self.config.interval_ms)
            log.info("Configuration updated and applied.")

    def _open_dashboard(self):
        dlg = StatsDashboard(self.db, self.monitor, self.config)
        dlg.show()
        dlg.raise_()
        dlg.activateWindow()

    def _quick_export_csv(self):
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = EXPORT_DIR / f"export_{ts}.csv"
        ok   = self.db.export_csv(str(path))
        if ok:
            self.tray.showMessage("Export Complete",
                                  f"CSV saved to:\n{path}",
                                  QSystemTrayIcon.Information, 4000)
        else:
            self.tray.showMessage("Export Failed",
                                  "No detections to export.",
                                  QSystemTrayIcon.Warning, 3000)

    def _quit(self):
        log.info(f"Shutting down {APP_NAME}. Session detections: {self._det_count_session}")
        self.monitor.shutdown()
        self.badges.clear_all()
        self.db.close()
        self.tray.hide()
        QApplication.instance().quit()

# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # ── Singleton lock ────────────────────────────────────────────────────────
    lock_file = CONFIG_DIR / ".lock"
    try:
        if lock_file.exists():
            try:
                pid = int(lock_file.read_text().strip())
                if sys.platform != "win32":
                    os.kill(pid, 0)
                    log.warning(f"{APP_NAME} already running (PID {pid}). Exiting.")
                    sys.exit(0)
            except (OSError, ValueError):
                pass   # stale lock
        lock_file.write_text(str(os.getpid()))
    except Exception:
        pass

    # ── Qt app ────────────────────────────────────────────────────────────────
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setStyleSheet(BASE_STYLE)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, APP_NAME,
                             "No system tray detected. Cannot launch AI Sentinel Pro.")
        sys.exit(1)

    sentinel = Sentinel()

    def _cleanup():
        try:
            lock_file.unlink()
        except Exception:
            pass

    app.aboutToQuit.connect(_cleanup)
    log.info(f"{APP_NAME} v{APP_VERSION} ({APP_BUILD}) ready — PID {os.getpid()}")
    sys.exit(app.exec_())
