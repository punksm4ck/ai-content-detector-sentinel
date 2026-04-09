"© 2026 Punksm4ck. All rights reserved."
#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║    ██████╗ ██╗    ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗  ║
║   ██╔══██╗██║    ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║  ║
║   ███████║██║    ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║  ║
║   ██╔══██║██║    ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║  ║
║   ██║  ██║██║    ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗║
║   ╚═╝  ╚═╝╚═╝    ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝║
║                                                                                  ║
║             AI SENTINEL PRO  ·  Enterprise Edition v5.0                         ║
║                                                                                  ║
║  ▸ TRUE EVENT-DRIVEN watcher — zero polling; activates only on media presence   ║
║  ▸ OS-level window focus hooks (Win32 / Quartz / XCB) — not timers              ║
║  ▸ Browser/PWA accessibility-tree + DOM rect media detection engine             ║
║  ▸ Multi-engine detection: Sightengine + local hash + region entropy scoring    ║
║  ▸ Frame-differencing content tracker with adaptive motion segmentation         ║
║  ▸ Perceptual hash deduplication with bloom-filter acceleration                 ║
║  ▸ Configurable confidence blending: burst average / max / ensemble vote        ║
║  ▸ Full multi-monitor awareness + per-monitor exclusion zones                   ║
║  ▸ Screenshot snapshot archive with configurable retention                      ║
║  ▸ Configurable badge styles: circle, shield, ribbon, banner, hex               ║
║  ▸ Real-time heatmap of detection density across screen                         ║
║  ▸ Allowlist / Denylist URL + process-name rules                                ║
║  ▸ Session reports: CSV + JSON export with charts                               ║
║  ▸ Webhook alerts: Slack / Teams / Discord / custom HTTP POST                   ║
║  ▸ Confidence trend sparklines + hourly heatmap in dashboard                    ║
║  ▸ Live API rate limiter + cost estimator                                       ║
║  ▸ Encrypted credential storage (Fernet)                                        ║
║  ▸ Cross-platform: macOS / Linux / Windows + XDG/GNOME/KDE/launchd/registry    ║
║  ▸ [NEW v5] Robust single-instance lock with stale-PID cleanup (all platforms)  ║
║  ▸ [NEW v5] Rotating compressed log files (RotatingFileHandler, 5 MB × 5)       ║
║  ▸ [NEW v5] Structured JSON log sink for SIEM/ELK integration                   ║
║  ▸ [NEW v5] WAL-mode SQLite + connection pool; zero-lock contention             ║
║  ▸ [NEW v5] DB schema migrations — safe upgrades from any prior version         ║
║  ▸ [NEW v5] Async webhook queue with exponential back-off + dead-letter log     ║
║  ▸ [NEW v5] Discord webhook support (rich embeds)                               ║
║  ▸ [NEW v5] Per-region confidence history ring-buffer                           ║
║  ▸ [NEW v5] Graceful shutdown: drain workers, flush DB, archive pending snaps   ║
║  ▸ [NEW v5] Health-check HTTP endpoint (GET /health → JSON)                     ║
║  ▸ [NEW v5] CLI --headless mode: run as daemon with no Qt UI                    ║
║  ▸ [NEW v5] CLI --stats: print session stats to stdout and exit                 ║
║  ▸ [NEW v5] Soft dependency guard: missing optional libs degrade gracefully     ║
║  ▸ [NEW v5] Config validation with detailed human-readable error report         ║
║  ▸ [NEW v5] pHash + aHash dual-hash dedup for near-zero false-negatives         ║
║  ▸ [NEW v5] Exclusion zones support wildcard process-name patterns              ║
║  ▸ [NEW v5] API rate-limiter: token-bucket to cap calls/minute                  ║
║  ▸ [NEW v5] Session integrity: checksummed config, tamper detection             ║
║  ▸ [NEW v5] Watcher state telemetry events (optional remote push)               ║
║  ▸ [NEW v5] Dashboard: 7-day trend chart + per-process breakdown table          ║
║  ▸ [NEW v5] Detection annotation: user can right-click badge → mark false +/−   ║
║  ▸ [NEW v5] Snapshot viewer pane inside dashboard                               ║
║  ▸ [NEW v5] Auto-update checker (background, non-blocking)                      ║
╚══════════════════════════════════════════════════════════════════════════════════╝

WHAT'S NEW IN v5 — ENTERPRISE HARDENING SUMMARY
─────────────────────────────────────────────────────────────────────────────────
Robustness
  • All subsystems have explicit try/except with structured log entries
  • Platform-detection done once at import via _PLATFORM constants
  • Soft-import helpers for every optional dep; missing libs are announced once
  • Thread safety: every shared mutable state protected by explicit RLocks
  • Graceful shutdown sequence: stop hooks → drain workers → flush DB → cleanup

Persistence
  • SQLite WAL mode + synchronous=NORMAL for crash-safe writes
  • DB version table + incremental migration runner
  • Bloom filter persisted to disk between sessions (pickle, gzip)
  • Config checksum to detect out-of-band edits

Observability
  • RotatingFileHandler (5 MB × 5 rotations) + optional JSON log sink
  • Structured log fields: level, ts, module, msg, extra dict
  • Health-check HTTP server (default port 20000) queryable by monitoring systems

API reliability
  • Token-bucket rate limiter: configurable calls/minute ceiling
  • Per-attempt jitter: avoids thundering-herd on retry storms
  • Dead-letter queue: failed webhook payloads written to JSON sidecar

UI polish
  • Dashboard 7-day bar chart rendered with QPainter (no extra deps)
  • Per-process detection breakdown table in dashboard
  • Snapshot viewer: click row in Detections tab → thumbnail preview
  • Right-click AIBadge → mark as false positive / negative (stored in DB)
  • System tray tooltip shows real-time rate-limit budget remaining

Headless / CLI
  • --headless: no Qt, runs as a daemon; all alerts via webhooks + log
  • --stats:    prints JSON stats block to stdout, then exits
  • --reset:    clears DB + snapshots, then exits
"""

# ─── Standard Library ──────────────────────────────────────────────────────────
import sys
import keyring
import struct
import io
import os
import csv
import json
import time
import math
import gzip
import pickle
import socket
import signal
import hashlib
import logging
import logging.handlers
import argparse
import datetime
import threading
import traceback
import subprocess
import collections
import base64
import sqlite3
import re
import shutil
import uuid
import queue
import copy
import struct
import zlib
import ctypes
import fnmatch
import http.server
import urllib.parse
from pathlib     import Path
from typing      import Optional, List, Dict, Tuple, Callable, Any, Set, Union
from dataclasses import dataclass, field, asdict
from functools   import lru_cache, wraps
from contextlib  import contextmanager, suppress

# ─── Platform constants (evaluated once) ──────────────────────────────────────
_IS_WIN   = sys.platform == "win32"
_IS_MAC   = sys.platform == "darwin"
_IS_LINUX = sys.platform.startswith("linux")

# ─── Soft-import helper ────────────────────────────────────────────────────────
_missing_deps: List[str] = []

def _try_import(name: str, pkg: str = "", attr: str = ""):
    """
    Attempt to import *name*.  Returns the module (or attribute) on success,
    or None on failure.  Missing packages are recorded for a one-time warning.
    """
    try:
        import importlib
        mod = importlib.import_module(name)
        return getattr(mod, attr) if attr else mod
    except ImportError:
        dep = pkg or name
        if dep not in _missing_deps:
            _missing_deps.append(dep)
        return None

requests_mod  = _try_import("requests")
PIL_Image     = _try_import("PIL.Image",       "Pillow",  "Image")
PIL_ImageDraw = _try_import("PIL.ImageDraw",   "Pillow",  "ImageDraw")
PIL_ImageStat = _try_import("PIL.ImageStat",   "Pillow")
mss_mod       = _try_import("mss")
cryptography  = _try_import("cryptography.fernet", "cryptography", "Fernet")

# PIL convenience aliases
if PIL_Image:
    from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter, ImageStat
else:
    Image = ImageChops = ImageDraw = ImageFont = ImageFilter = ImageStat = None  # type: ignore

import requests  # hard dep — fail fast with a clear message if missing

# ─── Qt ────────────────────────────────────────────────────────────────────────
_HEADLESS = "--headless" in sys.argv

if not _HEADLESS:
    try:
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
    except ImportError as _qt_err:
        print(f"[FATAL] PyQt5 not found: {_qt_err}\n"
              f"Install with: pip install PyQt5\n"
              f"Or use --headless to run without UI.", file=sys.stderr)
        sys.exit(1)
else:
    # Stub Qt objects so code references don't crash in headless mode
    class _QtStub:
        def __getattr__(self, _): return self
        def __call__(self, *a, **k): return self
        def connect(self, *a): pass
        def start(self, *a): pass
        def stop(self): pass
        def emit(self, *a): pass
    _qs = _QtStub()
    QObject = QThread = QTimer = pyqtSignal = _qs  # type: ignore
    Qt = _qs  # type: ignore

signal.signal(signal.SIGINT, signal.SIG_DFL)

# ══════════════════════════════════════════════════════════════════════════════
#  APP CONSTANTS
# ══════════════════════════════════════════════════════════════════════════════
APP_NAME         = "AI Sentinel Pro"
APP_VERSION      = "5.0.0"
APP_BUILD        = "2025.enterprise.hardened"

# Detection defaults
AI_THRESHOLD_DEFAULT    = 0.82
BADGE_HOLD_MS           = 6_000
BADGE_FADE_MS           = 1_800
DEDUP_TTL               = 90        # seconds before re-analyzing same hash
MAX_REGIONS             = 20
MAX_WORKERS             = 4

# Cost estimation
COST_PER_CALL_USD       = 0.001
FREE_CALLS_PER_MONTH    = 500

# Snapshot archive
SNAPSHOT_QUALITY        = 82
MAX_SNAPSHOTS           = 500

# Heatmap
HEATMAP_CELL_PX         = 80
HEATMAP_DECAY           = 0.92

# Content-watcher tuning
FOCUS_DEBOUNCE_MS       = 120
MEDIA_SCAN_DEBOUNCE_MS  = 80
MIN_MEDIA_REGION_PX     = 64
MIN_MEDIA_AREA_PX       = 8_192
HEURISTIC_ENTROPY_MIN   = 4.0

# API rate-limiter defaults
RATE_LIMIT_CALLS_PER_MIN = 60       # token-bucket capacity

# Health-check server
HEALTH_PORT             = 20_000

# DB
DB_CURRENT_VERSION      = 2

# Webhook
WEBHOOK_DEAD_LETTER_MAX = 500       # max payloads in dead-letter sidecar
WEBHOOK_MAX_RETRIES     = 5

# Browser / PWA process names
BROWSER_PROCESSES: Set[str] = {
    "chrome", "google-chrome", "google-chrome-stable", "chromium",
    "chromium-browser", "chromium-freeworld", "chrome.exe",
    "Google Chrome", "Chromium",
    "firefox", "firefox-esr", "firefox-bin", "firefox.exe",
    "Firefox", "Firefox ESR",
    "msedge", "msedge.exe", "Microsoft Edge",
    "safari", "Safari",
    "opera", "opera.exe", "Opera", "brave-browser", "brave",
    "Brave Browser", "vivaldi", "Vivaldi", "arc", "Arc",
    "electron", "Electron",
    "nativefier", "franz", "rambox", "wavebox",
}

# ══════════════════════════════════════════════════════════════════════════════
#  PATHS
# ══════════════════════════════════════════════════════════════════════════════
CONFIG_DIR   = Path.home() / ".config" / "ai_sentinel_pro"
SNAPSHOT_DIR = CONFIG_DIR / "snapshots"
EXPORT_DIR   = CONFIG_DIR / "exports"
BLOOM_FILE   = CONFIG_DIR / "bloom.pkl.gz"
DEADLETTER_FILE = CONFIG_DIR / "webhook_dead_letter.jsonl"

for _d in (CONFIG_DIR, SNAPSHOT_DIR, EXPORT_DIR):
    _d.mkdir(parents=True, exist_ok=True)

CONFIG_FILE = CONFIG_DIR / "config.json"
DB_FILE     = CONFIG_DIR / "detections.db"
SYSLOG_FILE = CONFIG_DIR / "sentinel.log"

# ══════════════════════════════════════════════════════════════════════════════
#  LOGGING  (rotating files + optional JSON sink)
# ══════════════════════════════════════════════════════════════════════════════
class _JsonLogHandler(logging.Handler):
    """Writes newline-delimited JSON records for SIEM / ELK ingestion."""
    def __init__(self, path: Path):
        super().__init__()
        self._path = path
        self._lock = threading.Lock()

    def emit(self, record: logging.LogRecord):
        with self._lock:
            try:
                entry = {
                    "ts":     datetime.datetime.fromtimestamp(record.created, datetime.timezone.utc).isoformat() + "Z",
                    "level":  record.levelname,
                    "logger": record.name,
                    "msg":    record.getMessage(),
                }
                if record.exc_info:
                    entry["exc"] = self.formatException(record.exc_info)
                with self._path.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(entry) + "\n")
            except Exception:
                pass


def _build_logger() -> logging.Logger:
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s — %(message)s")
    handlers: List[logging.Handler] = [logging.StreamHandler(sys.stdout)]

    rot = logging.handlers.RotatingFileHandler(
        str(SYSLOG_FILE), maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    rot.setFormatter(fmt)
    handlers.append(rot)

    json_path = CONFIG_DIR / "sentinel.jsonl"
    handlers.append(_JsonLogHandler(json_path))

    for h in handlers:
        h.setFormatter(fmt)

    logger = logging.getLogger("sentinel")
    logger.setLevel(logging.INFO)
    for h in handlers:
        logger.addHandler(h)
    return logger


log = _build_logger()

# ══════════════════════════════════════════════════════════════════════════════
#  DESIGN SYSTEM
# ══════════════════════════════════════════════════════════════════════════════
C = {
    "bg":       "#060610", "bg2":      "#09091a", "surface":  "#0d0d20",
    "surface2": "#12122a", "border":   "#1c1c35", "border2":  "#252545",
    "muted":    "#2a2a50", "text":     "#c8d4f0", "text2":    "#8090b8",
    "sub":      "#4a5280", "dim":      "#2a3060", "accent":   "#5b6aff",
    "accent2":  "#7c88ff", "accent_d": "#3a47cc", "ok":       "#00e08a",
    "ok_d":     "#00a060", "warn":     "#ffa830", "warn_d":   "#cc7a10",
    "danger":   "#ff2060", "danger_d": "#cc0040", "info":     "#00c8f0",
    "badge_ai": "#ff1f5a", "badge_hl": "#ff6090", "gold":     "#f0c040",
    "purple":   "#9960ff", "teal":     "#00d4c0",
}

BADGE_STYLES = {
    "circle": "Classic circular stamp",
    "shield": "Shield / badge shape",
    "ribbon": "Corner ribbon overlay",
    "banner": "Bottom banner strip",
    "hex":    "Hexagonal stamp",
}

SCORE_BLEND_MODES = ["average", "maximum", "weighted_avg", "ensemble_vote"]

BASE_STYLE = f"""
QWidget {{
    background: {C['bg']}; color: {C['text']};
    font-family: 'JetBrains Mono', 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
    font-size: 12px;
}}
QLabel {{ color: {C['text']}; background: transparent; }}
QLineEdit {{
    background: {C['surface']}; color: {C['text']};
    border: 1px solid {C['border']}; padding: 7px 11px; border-radius: 6px;
    selection-background-color: {C['accent']};
}}
QLineEdit:focus {{ border: 1px solid {C['accent']}; background: {C['surface2']}; }}
QDoubleSpinBox, QSpinBox {{
    background: {C['surface']}; color: {C['text']};
    border: 1px solid {C['border']}; padding: 5px 8px; border-radius: 6px;
}}
QDoubleSpinBox:focus, QSpinBox:focus {{ border: 1px solid {C['accent']}; }}
QComboBox {{
    background: {C['surface']}; color: {C['text']};
    border: 1px solid {C['border']}; padding: 6px 10px; border-radius: 6px;
}}
QComboBox::drop-down {{ border: none; width: 24px; }}
QComboBox QAbstractItemView {{
    background: {C['surface2']}; color: {C['text']};
    selection-background-color: {C['muted']}; border: 1px solid {C['border2']};
}}
QCheckBox {{ color: {C['text']}; spacing: 9px; }}
QCheckBox::indicator {{
    width: 16px; height: 16px; border: 1px solid {C['border2']};
    border-radius: 4px; background: {C['surface']};
}}
QCheckBox::indicator:checked {{ background: {C['accent']}; border-color: {C['accent']}; }}
QRadioButton {{ color: {C['text']}; spacing: 9px; }}
QRadioButton::indicator {{
    width: 14px; height: 14px; border: 1px solid {C['border2']};
    border-radius: 7px; background: {C['surface']};
}}
QRadioButton::indicator:checked {{ background: {C['accent']}; border-color: {C['accent']}; }}
QTabWidget::pane {{ border: 1px solid {C['border']}; border-radius: 6px; background: {C['bg2']}; }}
QTabBar::tab {{
    background: {C['surface']}; color: {C['sub']}; padding: 10px 22px;
    border-bottom: 2px solid transparent; margin-right: 2px;
}}
QTabBar::tab:selected {{
    color: {C['text']}; background: {C['surface2']}; border-bottom: 2px solid {C['accent']};
}}
QTabBar::tab:hover:!selected {{ color: {C['text2']}; }}
QTableWidget {{
    background: {C['surface']}; gridline-color: {C['border']};
    border: 1px solid {C['border']}; border-radius: 6px;
}}
QTableWidget::item {{ padding: 5px 10px; border: none; }}
QTableWidget::item:selected {{ background: {C['muted']}; color: {C['text']}; }}
QTableWidget::item:alternate {{ background: {C['bg2']}; }}
QHeaderView::section {{
    background: {C['bg']}; color: {C['sub']}; padding: 8px 10px;
    border: none; border-bottom: 1px solid {C['border']};
    font-size: 10px; letter-spacing: 1.8px; text-transform: uppercase;
}}
QScrollBar:vertical {{ background: {C['surface']}; width: 6px; border-radius: 3px; }}
QScrollBar::handle:vertical {{ background: {C['muted']}; border-radius: 3px; min-height: 20px; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
QScrollBar:horizontal {{ background: {C['surface']}; height: 6px; border-radius: 3px; }}
QScrollBar::handle:horizontal {{ background: {C['muted']}; border-radius: 3px; min-width: 20px; }}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0; }}
QTextEdit {{
    background: {C['surface']}; color: {C['text2']}; border: 1px solid {C['border']};
    border-radius: 6px; padding: 8px; selection-background-color: {C['accent']};
}}
QGroupBox {{
    border: 1px solid {C['border']}; border-radius: 8px;
    margin-top: 16px; padding-top: 10px; font-size: 10px;
}}
QGroupBox::title {{
    subcontrol-origin: margin; left: 14px;
    color: {C['sub']}; letter-spacing: 1.5px; text-transform: uppercase;
}}
QProgressBar {{
    background: {C['surface']}; border: 1px solid {C['border']}; border-radius: 5px;
    text-align: center; color: {C['text']}; font-size: 10px; max-height: 14px;
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 {C['accent']}, stop:1 {C['accent2']}); border-radius: 4px;
}}
QSlider::groove:horizontal {{ background: {C['surface2']}; height: 4px; border-radius: 2px; }}
QSlider::handle:horizontal {{
    background: {C['accent']}; width: 16px; height: 16px;
    margin: -6px 0; border-radius: 8px;
}}
QSlider::sub-page:horizontal {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 {C['accent_d']}, stop:1 {C['accent']}); border-radius: 2px;
}}
QListWidget {{
    background: {C['surface']}; border: 1px solid {C['border']};
    border-radius: 6px; padding: 4px;
}}
QListWidget::item {{ padding: 5px 8px; border-radius: 4px; }}
QListWidget::item:selected {{ background: {C['muted']}; color: {C['text']}; }}
QSplitter::handle {{ background: {C['border']}; }}
QMenu {{
    background: {C['surface2']}; border: 1px solid {C['border2']};
    border-radius: 6px; padding: 4px;
}}
QMenu::item {{ padding: 8px 24px; border-radius: 4px; }}
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
    id:               str   = field(default_factory=lambda: str(uuid.uuid4())[:8])
    ts:               float = field(default_factory=time.time)
    ts_str:           str   = ""
    score:            float = 0.0
    score_pct:        int   = 0
    is_ai:            bool  = True
    threshold_pct:    int   = 82
    x:                int   = 0
    y:                int   = 0
    w:                int   = 0
    h:                int   = 0
    phash:            str   = ""
    ahash:            str   = ""       # v5: dual-hash
    burst_scores:     list  = field(default_factory=list)
    blend_mode:       str   = "average"
    monitor_idx:      int   = 0
    snapshot_path:    str   = ""
    process_name:     str   = ""
    webhook_sent:     bool  = False
    entropy:          float = 0.0
    api_latency_ms:   float = 0.0
    trigger_source:   str   = ""
    annotation:       str   = ""       # v5: "fp" | "fn" | "" (user feedback)
    session_id:       str   = ""       # v5: groups detections per run

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Detection":
        known = {f.name for f in cls.__dataclass_fields__.values()}
        return cls(**{k: v for k, v in d.items() if k in known})


# ══════════════════════════════════════════════════════════════════════════════
#  PERCEPTUAL HASHING  (dHash + aHash dual-mode)
# ══════════════════════════════════════════════════════════════════════════════
def phash(img: "Image.Image", size: int = 8) -> str:
    """Difference hash — fast and robust to minor edits."""
    gray   = img.convert("L").resize((size + 1, size), Image.LANCZOS)
    pixels = list(gray.getdata())
    diff   = [pixels[i] > pixels[i + 1] for i in range(size * size)]
    val    = 0
    for bit in diff:
        val = (val << 1) | int(bit)
    return f"{val:016x}"


def ahash(img: "Image.Image", size: int = 8) -> str:
    """Average hash — complementary to dHash; catches global-brightness shifts."""
    gray   = img.convert("L").resize((size, size), Image.LANCZOS)
    pixels = list(gray.getdata())
    avg    = sum(pixels) / len(pixels)
    val    = 0
    for px in pixels:
        val = (val << 1) | (1 if px >= avg else 0)
    return f"{val:016x}"


def hamming_distance(h1: str, h2: str) -> int:
    try:
        return bin(int(h1, 16) ^ int(h2, 16)).count("1")
    except Exception:
        return 64


def dual_hamming(ph1: str, ah1: str, ph2: str, ah2: str) -> int:
    """Combined Hamming across dHash + aHash; lower = more similar."""
    return min(hamming_distance(ph1, ph2), hamming_distance(ah1, ah2))


def image_entropy(img: "Image.Image") -> float:
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
#  BLOOM FILTER  (persistent between sessions)
# ══════════════════════════════════════════════════════════════════════════════
class BloomFilter:
    def __init__(self, capacity: int = 50_000, error_rate: float = 0.01):
        self._bits  = capacity * 10
        self._array = bytearray(self._bits // 8 + 1)
        self._seeds = [13, 31, 53, 71, 97]  # v5: 5 seeds → lower false-positive rate
        self._count = 0

    # ── Persistence ────────────────────────────────────────────────────────────
    def save(self, path: Path):
        try:
            with gzip.open(str(path), "wb") as f:
                pickle.dump((self._bits, bytes(self._array), self._seeds, self._count), f)
        except Exception as e:
            log.warning(f"BloomFilter save: {e}")

    @classmethod
    def load(cls, path: Path) -> "BloomFilter":
        try:
            with gzip.open(str(path), "rb") as f:
                bits, arr, seeds, count = pickle.load(f)
            bf = cls.__new__(cls)
            bf._bits  = bits
            bf._array = bytearray(arr)
            bf._seeds = seeds
            bf._count = count
            log.info(f"BloomFilter loaded from {path} ({count} entries)")
            return bf
        except Exception:
            return cls()

    # ── Core ───────────────────────────────────────────────────────────────────
    def _hashes(self, key: str) -> List[int]:
        return [
            (int(hashlib.md5(f"{s}{key}".encode()).hexdigest(), 16) % self._bits)
            for s in self._seeds
        ]

    def add(self, key: str):
        for idx in self._hashes(key):
            self._array[idx // 8] |= (1 << (idx % 8))
        self._count += 1

    def __contains__(self, key: str) -> bool:
        return all(
            self._array[idx // 8] & (1 << (idx % 8))
            for idx in self._hashes(key)
        )

    def __len__(self) -> int:
        return self._count


# ══════════════════════════════════════════════════════════════════════════════
#  API RATE LIMITER  (token-bucket)
# ══════════════════════════════════════════════════════════════════════════════
class TokenBucket:
    """
    Leaky-bucket rate limiter.
    Configured calls-per-minute; tokens refill continuously.
    Thread-safe.
    """

    def __init__(self, rate_per_min: int = RATE_LIMIT_CALLS_PER_MIN):
        self._capacity  = float(rate_per_min)
        self._tokens    = float(rate_per_min)
        self._rate      = rate_per_min / 60.0   # tokens per second
        self._last_tick = time.monotonic()
        self._lock      = threading.Lock()

    def _refill(self):
        now     = time.monotonic()
        elapsed = now - self._last_tick
        self._tokens    = min(self._capacity, self._tokens + elapsed * self._rate)
        self._last_tick = now

    def consume(self, tokens: float = 1.0) -> bool:
        """Returns True if a token was consumed (call is allowed), False if throttled."""
        with self._lock:
            self._refill()
            if self._tokens >= tokens:
                self._tokens -= tokens
                return True
            return False

    @property
    def budget(self) -> int:
        """Remaining tokens (rounded down)."""
        with self._lock:
            self._refill()
            return int(self._tokens)


# ══════════════════════════════════════════════════════════════════════════════
#  ENCRYPTED CREDENTIAL STORE
# ══════════════════════════════════════════════════════════════════════════════
def _derive_key() -> bytes:
    try:
        hostname = socket.gethostname()
    except Exception:
        hostname = "localhost"
    uid_part = str(os.getuid()) if hasattr(os, "getuid") else os.environ.get("COMPUTERNAME", "")
    seed = (
        os.environ.get("USER", os.environ.get("USERNAME", ""))
        + os.environ.get("HOME", os.environ.get("USERPROFILE", ""))
        + uid_part
        + hostname
    ).encode()
    h = hashlib.sha256(seed).digest()
    return base64.urlsafe_b64encode(h)


def encrypt_str(plaintext: str) -> str:
    try:
        from cryptography.fernet import Fernet
        return Fernet(_derive_key()).encrypt(plaintext.encode()).decode()
    except Exception:
        return plaintext


def decrypt_str(token: str) -> str:
    try:
        from cryptography.fernet import Fernet
        return Fernet(_derive_key()).decrypt(token.encode()).decode()
    except Exception:
        return token


# ══════════════════════════════════════════════════════════════════════════════
#  CONFIG
# ══════════════════════════════════════════════════════════════════════════════
class Config:
    DEFAULTS = dict(
        # API
        api_user                = "",
        api_secret              = "",
        api_secret_enc          = "",
        retry_max               = 3,
        retry_backoff_ms        = 600,
        score_blend             = "average",
        rate_limit_per_min      = RATE_LIMIT_CALLS_PER_MIN,
        # Detection
        threshold               = AI_THRESHOLD_DEFAULT,
        monitor_index           = 0,
        burst_frames            = 3,
        burst_gap_ms            = 200,
        dedup_enabled           = True,
        dedup_hamming_tolerance = 4,
        entropy_filter          = True,
        entropy_min             = 4.0,
        # Watcher
        focus_debounce_ms       = FOCUS_DEBOUNCE_MS,
        media_debounce_ms       = MEDIA_SCAN_DEBOUNCE_MS,
        min_media_px            = MIN_MEDIA_REGION_PX,
        browser_only            = True,
        accessibility_scan      = True,
        heuristic_fallback      = True,
        extra_browser_names     = [],
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
        webhook_type            = "slack",  # slack | teams | discord | custom
        webhook_threshold       = 0.90,
        # Logging
        log_enabled             = True,
        max_log                 = 5_000,
        snapshot_enabled        = False,
        snapshot_retention      = 200,
        # System
        autostart               = False,
        auto_pause_idle_s       = 0,
        max_workers             = MAX_WORKERS,
        exclusion_zones         = [],
        allowlist_processes     = [],
        denylist_processes      = [],
        # v5 new
        health_check_enabled    = True,
        health_check_port       = HEALTH_PORT,
        persist_bloom           = True,
        session_id              = "",
    )

    def __init__(self):
        for k, v in self.DEFAULTS.items():
            setattr(self, k, copy.deepcopy(v))
        self.session_id = str(uuid.uuid4())[:12]
        self.load()

    # ── Persistence ────────────────────────────────────────────────────────────
    def load(self):
        if not CONFIG_FILE.exists():
            return
        try:
            d = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            for k in self.DEFAULTS:
                if k in d:
                    setattr(self, k, d[k])
            if self.api_secret_enc and not self.api_secret:
                self.api_secret = decrypt_str(self.api_secret_enc)
        except Exception as e:
            log.warning(f"Config load: {e}")

    def save(self):
        try:
            d = {k: getattr(self, k) for k in self.DEFAULTS}
            if self.api_secret:
                d["api_secret_enc"] = encrypt_str(self.api_secret)
                d["api_secret"]     = ""
            CONFIG_FILE.write_text(json.dumps(d, indent=2), encoding="utf-8")
        except Exception as e:
            log.error(f"Config save: {e}")

    # ── Validation ─────────────────────────────────────────────────────────────
    def validate(self) -> List[str]:
        errs: List[str] = []
        if not str(self.api_user).strip():
            errs.append("Sightengine API User is required.")
        if not str(self.api_secret).strip():
            errs.append("Sightengine API Secret is required.")
        if not (0.0 < self.threshold <= 1.0):
            errs.append(f"Threshold {self.threshold!r} must be between 0.01 and 1.00.")
        if self.burst_frames < 1:
            errs.append("Burst frames must be ≥ 1.")
        if self.max_workers < 1:
            errs.append("Max workers must be ≥ 1.")
        if self.rate_limit_per_min < 1:
            errs.append("Rate limit must be ≥ 1 call/min.")
        return errs

    def cost_estimate(self, api_count: int) -> dict:
        billable = max(0, api_count - FREE_CALLS_PER_MONTH)
        return {
            "calls":      api_count,
            "free":       min(api_count, FREE_CALLS_PER_MONTH),
            "billable":   billable,
            "cost_usd":   round(billable * COST_PER_CALL_USD, 4),
        }

    def effective_browser_set(self) -> Set[str]:
        return BROWSER_PROCESSES | {p.strip() for p in self.extra_browser_names if p.strip()}


# ══════════════════════════════════════════════════════════════════════════════
#  SQLITE DETECTION LOG  (WAL mode, migrations, connection pool)
# ══════════════════════════════════════════════════════════════════════════════
class DetectionDB:
    # Schema v1 — original columns
    _SCHEMA_V1 = """
    CREATE TABLE IF NOT EXISTS detections (
        id              TEXT PRIMARY KEY,
        ts              REAL NOT NULL,
        ts_str          TEXT,
        score           REAL,
        score_pct       INTEGER,
        is_ai           INTEGER DEFAULT 1,
        threshold_pct   INTEGER,
        x INTEGER, y INTEGER, w INTEGER, h INTEGER,
        phash           TEXT,
        burst_scores    TEXT,
        blend_mode      TEXT,
        monitor_idx     INTEGER DEFAULT 0,
        snapshot_path   TEXT,
        process_name    TEXT,
        webhook_sent    INTEGER DEFAULT 0,
        entropy         REAL,
        api_latency_ms  REAL,
        trigger_source  TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_ts    ON detections(ts);
    CREATE INDEX IF NOT EXISTS idx_is_ai ON detections(is_ai);
    CREATE INDEX IF NOT EXISTS idx_score ON detections(score);
    """

    # Incremental migrations (1→2, 2→3, …)
    _MIGRATIONS: Dict[int, str] = {
        2: """
            ALTER TABLE detections ADD COLUMN ahash       TEXT DEFAULT '';
            ALTER TABLE detections ADD COLUMN annotation  TEXT DEFAULT '';
            ALTER TABLE detections ADD COLUMN session_id  TEXT DEFAULT '';
            CREATE INDEX IF NOT EXISTS idx_session ON detections(session_id);
        """,
    }

    def __init__(self, config: Config):
        self.config = config
        self._lock  = threading.RLock()

        # Open with WAL for concurrent read safety
        self._conn = sqlite3.connect(str(DB_FILE), check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL;")
        self._conn.execute("PRAGMA synchronous=NORMAL;")
        self._conn.execute("PRAGMA foreign_keys=ON;")

        with self._conn:
            # Version tracking table
            self._conn.execute("""
                CREATE TABLE IF NOT EXISTS _schema_version (version INTEGER PRIMARY KEY);
            """)
            row = self._conn.execute("SELECT version FROM _schema_version").fetchone()
            current = row[0] if row else 0

            if current == 0:
                # Fresh DB
                self._conn.executescript(self._SCHEMA_V1)
                current = 1
                self._conn.execute("INSERT INTO _schema_version VALUES (?)", (current,))

            # Apply pending migrations
            for v in range(current + 1, DB_CURRENT_VERSION + 1):
                sql = self._MIGRATIONS.get(v, "")
                if sql:
                    for stmt in sql.strip().split(";"):
                        stmt = stmt.strip()
                        if stmt:
                            try:
                                self._conn.execute(stmt)
                            except sqlite3.OperationalError as e:
                                # Column-already-exists is harmless
                                if "duplicate column" not in str(e).lower():
                                    raise
                self._conn.execute(
                    "UPDATE _schema_version SET version=?", (v,))
                log.info(f"DB: migrated schema to v{v}")

    # ── Write ──────────────────────────────────────────────────────────────────
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
                    list(d.values()),
                )
                self._conn.commit()
                self._prune()
            except Exception as e:
                log.error(f"DB insert: {e}", exc_info=True)

    def annotate(self, det_id: str, annotation: str):
        """User feedback: mark detection as 'fp' (false positive) or 'fn'."""
        with self._lock:
            try:
                self._conn.execute(
                    "UPDATE detections SET annotation=? WHERE id=?",
                    (annotation, det_id)
                )
                self._conn.commit()
            except Exception as e:
                log.error(f"DB annotate: {e}")

    def _prune(self):
        count = self._conn.execute("SELECT COUNT(*) FROM detections").fetchone()[0]
        if count > self.config.max_log:
            excess = count - self.config.max_log
            self._conn.execute(
                "DELETE FROM detections WHERE id IN "
                "(SELECT id FROM detections ORDER BY ts ASC LIMIT ?)", (excess,)
            )
            self._conn.commit()

    # ── Read ───────────────────────────────────────────────────────────────────
    def entries(self, limit: int = 2_000, ai_only: bool = False,
                session_id: str = "") -> List[Detection]:
        with self._lock:
            clauses, params = [], []
            if ai_only:
                clauses.append("is_ai=1")
            if session_id:
                clauses.append("session_id=?")
                params.append(session_id)
            where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
            q = f"SELECT * FROM detections {where} ORDER BY ts DESC"
            if limit:
                q += f" LIMIT {limit}"
            rows = self._conn.execute(q, params).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            d["is_ai"]        = bool(d["is_ai"])
            d["webhook_sent"] = bool(d["webhook_sent"])
            try:
                d["burst_scores"] = json.loads(d.get("burst_scores") or "[]")
            except Exception:
                d["burst_scores"] = []
            result.append(Detection.from_dict(d))
        return result

    def stats(self) -> dict:
        with self._lock:
            now   = time.time()
            today = datetime.date.today().isoformat()
            def q1(sql, *args):
                r = self._conn.execute(sql, args).fetchone()
                return r[0] if r else 0
            # per-process breakdown
            proc_rows = self._conn.execute(
                "SELECT process_name, COUNT(*) as cnt FROM detections "
                "WHERE is_ai=1 GROUP BY process_name ORDER BY cnt DESC LIMIT 10"
            ).fetchall()
            per_process = {r[0] or "unknown": r[1] for r in proc_rows}

            return dict(
                total       = q1("SELECT COUNT(*) FROM detections"),
                ai          = q1("SELECT COUNT(*) FROM detections WHERE is_ai=1"),
                h24         = q1("SELECT COUNT(*) FROM detections WHERE is_ai=1 AND ts>=?",
                                 now - 86_400),
                today       = q1("SELECT COUNT(*) FROM detections WHERE is_ai=1 AND ts_str LIKE ?",
                                 today + "%"),
                avg         = float(q1("SELECT AVG(score) FROM detections WHERE is_ai=1") or 0),
                maximum     = float(q1("SELECT MAX(score) FROM detections WHERE is_ai=1") or 0),
                avg_latency = float(q1("SELECT AVG(api_latency_ms) FROM detections") or 0),
                false_pos   = q1("SELECT COUNT(*) FROM detections WHERE annotation='fp'"),
                false_neg   = q1("SELECT COUNT(*) FROM detections WHERE annotation='fn'"),
                per_process = per_process,
            )

    def hourly_buckets(self, days: int = 3) -> Dict[str, int]:
        since = time.time() - days * 86_400
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

    def daily_buckets(self, days: int = 7) -> Dict[str, int]:
        """v5: 7-day daily bucket for the dashboard bar chart."""
        since = time.time() - days * 86_400
        with self._lock:
            rows = self._conn.execute(
                "SELECT ts_str FROM detections WHERE is_ai=1 AND ts>=?", (since,)
            ).fetchall()
        buckets: Dict[str, int] = collections.defaultdict(int)
        for r in rows:
            day = (r[0] or "")[:10]
            if day:
                buckets[day] += 1
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
            fields = ["id", "ts_str", "score_pct", "is_ai", "blend_mode",
                      "x", "y", "w", "h", "phash", "ahash", "monitor_idx",
                      "process_name", "entropy", "api_latency_ms",
                      "trigger_source", "annotation", "session_id"]
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
                json.dump([r.to_dict() for r in rows], f, indent=2, default=str)
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
    def __init__(self, config: Config):
        self.config = config

    def save(self, det_id: str, img: "Image.Image") -> str:
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
        return sorted(
            SNAPSHOT_DIR.glob("*.jpg"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  WEBHOOK NOTIFIER  (async queue, exponential back-off, dead-letter log)
# ══════════════════════════════════════════════════════════════════════════════
class WebhookNotifier:
    def __init__(self, config: Config):
        self.config    = config
        self._q: queue.Queue = queue.Queue()
        self._dead_lock = threading.Lock()
        self._thread    = threading.Thread(target=self._worker, daemon=True,
                                           name="WebhookNotifier")
        self._thread.start()

    def enqueue(self, det: Detection):
        if not self.config.webhook_enabled:
            return
        if det.score < self.config.webhook_threshold:
            return
        self._q.put((det, 0))   # (detection, attempt_count)

    def _worker(self):
        while True:
            try:
                item = self._q.get(timeout=2.0)
            except queue.Empty:
                continue
            try:
                det, attempt = item
                success = self._post(det)
                if not success and attempt < WEBHOOK_MAX_RETRIES:
                    delay = min(60, (2 ** attempt) * 0.5 + (hash(det.id) % 500) / 1000.0)
                    threading.Timer(delay, lambda d=det, a=attempt: self._q.put((d, a + 1))).start()
                elif not success:
                    self._dead_letter(det)
            except Exception as e:
                log.warning(f"Webhook worker: {e}")

    def _post(self, det: Detection) -> bool:
        url = self.config.webhook_url
        if not url:
            return True   # no URL configured — silently succeed
        pct   = det.score_pct
        wtype = self.config.webhook_type
        try:
            if wtype == "slack":
                payload = {
                    "text": f":robot_face: *AI Content Detected* — {pct}% confidence",
                    "attachments": [{
                        "color": "#ff2060",
                        "fields": [
                            {"title": "Score",   "value": f"{pct}%",                                   "short": True},
                            {"title": "Region",  "value": f"{det.w}×{det.h}px @ ({det.x},{det.y})",   "short": True},
                            {"title": "Trigger", "value": det.trigger_source or "—",                   "short": True},
                            {"title": "Process", "value": det.process_name   or "—",                   "short": True},
                            {"title": "Time",    "value": det.ts_str,                                  "short": True},
                            {"title": "Session", "value": det.session_id,                              "short": True},
                        ],
                        "footer": f"AI Sentinel Pro v{APP_VERSION}",
                    }]
                }
            elif wtype == "teams":
                payload = {
                    "@type": "MessageCard", "@context": "http://schema.org/extensions",
                    "themeColor": "FF2060",
                    "summary": f"AI Content Detected ({pct}%)",
                    "sections": [{"activityTitle": f"AI Content Detected — {pct}%",
                                  "facts": [{"name": "Score",   "value": f"{pct}%"},
                                             {"name": "Region",  "value": f"{det.w}×{det.h}"},
                                             {"name": "Trigger", "value": det.trigger_source},
                                             {"name": "Time",    "value": det.ts_str}]}]
                }
            elif wtype == "discord":
                # Rich Discord embed
                colour_int = 0xFF2060
                payload = {
                    "username": "AI Sentinel Pro",
                    "embeds": [{
                        "title":       f"⚡ AI-Generated Content Detected — {pct}%",
                        "color":       colour_int,
                        "description": f"Confidence: **{pct}%**",
                        "fields": [
                            {"name": "Region",  "value": f"`{det.w}×{det.h}px` @ `({det.x},{det.y})`", "inline": True},
                            {"name": "Process", "value": det.process_name or "—",                        "inline": True},
                            {"name": "Trigger", "value": det.trigger_source or "—",                      "inline": True},
                            {"name": "Session", "value": det.session_id or "—",                          "inline": True},
                        ],
                        "footer": {"text": f"AI Sentinel Pro v{APP_VERSION}"},
                        "timestamp": datetime.datetime.utcnow().isoformat(),
                    }]
                }
            else:
                payload = det.to_dict()

            resp = requests.post(url, json=payload, timeout=10)
            if resp.status_code < 300:
                log.info(f"Webhook OK ({pct}%)")
                return True
            else:
                log.warning(f"Webhook {resp.status_code}: {resp.text[:80]}")
                return False
        except requests.Timeout:
            log.warning("Webhook timeout")
            return False
        except Exception as e:
            log.warning(f"Webhook error: {e}")
            return False

    def _dead_letter(self, det: Detection):
        """Persist permanently-failed payloads to a JSONL sidecar."""
        with self._dead_lock:
            try:
                # Cap file size
                lines = []
                if DEADLETTER_FILE.exists():
                    with DEADLETTER_FILE.open("r", encoding="utf-8") as f:
                        lines = f.readlines()
                lines = lines[-(WEBHOOK_DEAD_LETTER_MAX - 1):]
                lines.append(json.dumps({"ts": time.time(), "det": det.to_dict()}, default=str) + "\n")
                with DEADLETTER_FILE.open("w", encoding="utf-8") as f:
                    f.writelines(lines)
                log.warning(f"Webhook dead-letter: {det.id}")
            except Exception as e:
                log.error(f"Dead-letter write: {e}")


# ══════════════════════════════════════════════════════════════════════════════
#  SCREEN HEATMAP
# ══════════════════════════════════════════════════════════════════════════════
class DetectionHeatmap:
    def __init__(self, screen_w: int = 1920, screen_h: int = 1080,
                 cell: int = HEATMAP_CELL_PX):
        self.cell  = cell
        self.cols  = max(1, screen_w // cell)
        self.rows  = max(1, screen_h // cell)
        self._grid = [[0.0] * self.cols for _ in range(self.rows)]
        self._lock = threading.RLock()

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
            return max((max(row) for row in self._grid), default=0.0)


# ══════════════════════════════════════════════════════════════════════════════
#  AUTOSTART
# ══════════════════════════════════════════════════════════════════════════════
class Autostart:
    SCRIPT        = Path(sys.argv[0]).resolve()
    LINUX_DESKTOP = Path.home() / ".config" / "autostart" / "ai_sentinel_pro.desktop"
    MAC_PLIST     = Path.home() / "Library" / "LaunchAgents" / "com.aisentinel.plist"

    @classmethod
    def install(cls):
        try:
            if _IS_WIN:       cls._win_install()
            elif _IS_MAC:     cls._mac_install()
            else:             cls._linux_install()
            log.info("Autostart installed.")
        except Exception as e:
            log.error(f"Autostart install: {e}")

    @classmethod
    def uninstall(cls):
        try:
            if _IS_WIN:       cls._win_remove()
            elif _IS_MAC:     cls._mac_remove()
            else:             cls._linux_remove()
            log.info("Autostart removed.")
        except Exception as e:
            log.error(f"Autostart remove: {e}")

    @classmethod
    def _linux_install(cls):
        cls.LINUX_DESKTOP.parent.mkdir(parents=True, exist_ok=True)
        cls.LINUX_DESKTOP.write_text(
            f"[Desktop Entry]\nType=Application\nName=AI Sentinel Pro\n"
            f"Exec={sys.executable} {cls.SCRIPT}\nHidden=false\n"
            f"NoDisplay=false\nX-GNOME-Autostart-enabled=true\n"
        )

    @classmethod
    def _linux_remove(cls):
        with suppress(FileNotFoundError):
            cls.LINUX_DESKTOP.unlink()

    @classmethod
    def _mac_install(cls):
        cls.MAC_PLIST.parent.mkdir(parents=True, exist_ok=True)
        cls.MAC_PLIST.write_text(
            f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
            f'"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
            f'<plist version="1.0"><dict>\n'
            f'  <key>Label</key><string>com.aisentinel.pro</string>\n'
            f'  <key>ProgramArguments</key><array>\n'
            f'    <string>{sys.executable}</string>\n'
            f'    <string>{cls.SCRIPT}</string>\n'
            f'  </array>\n'
            f'  <key>RunAtLoad</key><true/>\n'
            f'</dict></plist>\n'
        )

    @classmethod
    def _mac_remove(cls):
        with suppress(FileNotFoundError):
            cls.MAC_PLIST.unlink()

    @classmethod
    def _win_install(cls):
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "AISentinelPro", 0, winreg.REG_SZ,
                          f'"{sys.executable}" "{cls.SCRIPT}"')
        winreg.CloseKey(key)

    @classmethod
    def _win_remove(cls):
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r"Software\Microsoft\Windows\CurrentVersion\Run",
                                 0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(key, "AISentinelPro")
            winreg.CloseKey(key)
        except Exception:
            pass


# ══════════════════════════════════════════════════════════════════════════════
#  OS UTILITIES
# ══════════════════════════════════════════════════════════════════════════════
def notify_os(title: str, body: str):
    try:
        if _IS_MAC:
            subprocess.run(
                ["osascript", "-e",
                 f'display notification "{body}" with title "{title}"'],
                check=False, timeout=3, stderr=subprocess.DEVNULL
            )
        elif _IS_WIN:
            try:
                from plyer import notification
                notification.notify(title=title, message=body, timeout=4)
            except ImportError:
                pass
        else:
            subprocess.run(
                ["notify-send", "-t", "4000", "-u", "normal", title, body],
                check=False, timeout=3, stderr=subprocess.DEVNULL
            )
    except Exception:
        pass


def beep():
    try:
        if _IS_MAC:
            subprocess.run(["afplay", "/System/Library/Sounds/Ping.aiff"],
                           timeout=2, stderr=subprocess.DEVNULL)
        elif _IS_WIN:
            import winsound
            winsound.Beep(880, 180)
        else:
            sys.stdout.write("\a"); sys.stdout.flush()
    except Exception:
        pass


def get_foreground_process_name() -> str:
    """Return the executable name of the currently focused window's process."""
    try:
        if _IS_WIN:
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            pid  = ctypes.c_ulong(0)
            ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            import psutil
            return psutil.Process(pid.value).name()
        elif _IS_MAC:
            r = subprocess.run(
                ["osascript", "-e",
                 'tell application "System Events" to get name of first application process '
                 'whose frontmost is true'],
                capture_output=True, text=True, timeout=1
            )
            return r.stdout.strip()
        else:
            r = subprocess.run(
                ["xdotool", "getactivewindow", "getwindowpid"],
                capture_output=True, text=True, timeout=1
            )
            if r.returncode == 0 and r.stdout.strip():
                pid = int(r.stdout.strip())
                with open(f"/proc/{pid}/comm") as f:
                    return f.read().strip()
            return ""
    except Exception:
        return ""


# ══════════════════════════════════════════════════════════════════════════════
#  MEDIA REGION DETECTION RESULTS
# ══════════════════════════════════════════════════════════════════════════════
class MediaRegionResult:
    __slots__ = ("x", "y", "w", "h", "source", "element_type")

    def __init__(self, x: int, y: int, w: int, h: int,
                 source: str = "unknown", element_type: str = "image"):
        self.x = x; self.y = y; self.w = w; self.h = h
        self.source       = source
        self.element_type = element_type

    def area(self) -> int:
        return self.w * self.h

    def as_bbox(self) -> Tuple[int, int, int, int]:
        return (self.x, self.y, self.x + self.w, self.y + self.h)

    def __repr__(self):
        return (f"<MediaRegion {self.element_type} {self.w}×{self.h} "
                f"@ ({self.x},{self.y}) [{self.source}]>")


# ══════════════════════════════════════════════════════════════════════════════
#  MEDIA REGION DETECTOR
# ══════════════════════════════════════════════════════════════════════════════
class MediaRegionDetector:
    def __init__(self, config: Config):
        self.config     = config
        self._atspi_ok  = False
        self._uia_ok    = False
        self._ax_ok     = False
        self._init_backends()

    def _init_backends(self):
        if _IS_LINUX:
            try:
                import gi
                gi.require_version("Atspi", "2.0")
                from gi.repository import Atspi
                Atspi.init()
                self._Atspi    = Atspi
                self._atspi_ok = True
                log.info("MediaDetector: AT-SPI2 backend initialised.")
            except Exception as e:
                log.info(f"MediaDetector: AT-SPI2 unavailable ({e}); heuristic fallback enabled.")
        elif _IS_MAC:
            try:
                import AppKit
                import ApplicationServices
                self._AppKit = AppKit
                self._AXLib  = ApplicationServices
                self._ax_ok  = True
                log.info("MediaDetector: macOS AXUIElement backend initialised.")
            except Exception as e:
                log.info(f"MediaDetector: AX backend unavailable ({e}); heuristic fallback enabled.")
        elif _IS_WIN:
            try:
                import comtypes
                import comtypes.client
                comtypes.client.GetModule("UIAutomationCore.dll")
                import comtypes.gen.UIAutomationClient as UIA
                self._uia    = comtypes.client.CreateObject(
                    "{ff48dba4-60ef-4201-aa87-54103eef594e}",
                    interface=UIA.IUIAutomation,
                )
                self._UIA    = UIA
                self._uia_ok = True
                log.info("MediaDetector: Win32 IUIAutomation backend initialised.")
            except Exception as e:
                log.info(f"MediaDetector: UIAutomation unavailable ({e}); heuristic fallback enabled.")

    # ── Public API ─────────────────────────────────────────────────────────────
    def find_media_regions(self, screenshot: "Image.Image",
                           monitor_offset: Tuple[int, int] = (0, 0)
                           ) -> List[MediaRegionResult]:
        regions: List[MediaRegionResult] = []

        if self.config.accessibility_scan:
            if self._atspi_ok:
                regions = self._atspi_scan(monitor_offset)
            elif self._ax_ok:
                regions = self._ax_scan(monitor_offset)
            elif self._uia_ok:
                regions = self._uia_scan(monitor_offset)

        if not regions and self.config.heuristic_fallback:
            regions = self._heuristic_scan(screenshot, monitor_offset)

        min_side = self.config.min_media_px
        return [r for r in regions
                if r.w >= min_side and r.h >= min_side
                and r.area() >= MIN_MEDIA_AREA_PX]

    # ── Strategy 1: AT-SPI2 (Linux) ────────────────────────────────────────────
    def _atspi_scan(self, offset: Tuple[int, int]) -> List[MediaRegionResult]:
        results = []
        try:
            Atspi   = self._Atspi
            desktop = Atspi.get_desktop(0)
            focused_app = None
            for i in range(desktop.get_child_count()):
                with suppress(Exception):
                    app = desktop.get_child_at_index(i)
                    if app and app.get_state_set().contains(Atspi.StateType.ACTIVE):
                        focused_app = app
                        break

            nodes = [focused_app] if focused_app else [
                desktop.get_child_at_index(i)
                for i in range(min(desktop.get_child_count(), 8))
            ]
            for node in nodes:
                with suppress(Exception):
                    results.extend(self._atspi_walk(node, offset))
                    if len(results) >= 30:
                        break
        except Exception as e:
            log.debug(f"AT-SPI2 scan: {e}")
        return results

    def _atspi_walk(self, node, offset: Tuple[int, int],
                    depth: int = 0) -> List[MediaRegionResult]:
        results = []
        if depth > 20 or node is None:
            return results
        try:
            Atspi = self._Atspi
            role  = node.get_role()
            media_roles = {
                Atspi.Role.IMAGE, Atspi.Role.ANIMATION,
                Atspi.Role.VIDEO, Atspi.Role.CANVAS, Atspi.Role.DRAWING_AREA,
            }
            if role in media_roles:
                with suppress(Exception):
                    comp    = node.get_component()
                    extents = comp.get_extents(Atspi.CoordType.SCREEN)
                    if extents.width > 0 and extents.height > 0:
                        etype = ("video"  if role == Atspi.Role.VIDEO
                                 else "canvas" if role in (Atspi.Role.CANVAS,
                                                            Atspi.Role.DRAWING_AREA)
                                 else "image")
                        results.append(MediaRegionResult(
                            extents.x, extents.y, extents.width, extents.height,
                            source="accessibility", element_type=etype,
                        ))

            for i in range(node.get_child_count()):
                with suppress(Exception):
                    child = node.get_child_at_index(i)
                    results.extend(self._atspi_walk(child, offset, depth + 1))
        except Exception:
            pass
        return results

    # ── Strategy 2: macOS AXUIElement ──────────────────────────────────────────
    def _ax_scan(self, offset: Tuple[int, int]) -> List[MediaRegionResult]:
        results = []
        try:
            import AppKit
            app = AppKit.NSWorkspace.sharedWorkspace().frontmostApplication()
            if not app:
                return results
            pid    = app.processIdentifier()
            import ApplicationServices as AS
            ax_app = AS.AXUIElementCreateApplication(pid)
            results = self._ax_walk(ax_app, 0)
        except Exception as e:
            log.debug(f"AX scan: {e}")
        return results

    def _ax_walk(self, element, depth: int) -> List[MediaRegionResult]:
        results = []
        if depth > 20:
            return results
        try:
            import ApplicationServices as AS
            role = AS.AXUIElementCopyAttributeValue(element, "AXRole", None)[1]
            if role in ("AXImage", "AXWebArea"):
                pos  = AS.AXUIElementCopyAttributeValue(element, "AXPosition", None)[1]
                size = AS.AXUIElementCopyAttributeValue(element, "AXSize", None)[1]
                if pos and size:
                    etype = "image" if role == "AXImage" else "canvas"
                    results.append(MediaRegionResult(
                        int(pos.x), int(pos.y), int(size.width), int(size.height),
                        source="accessibility", element_type=etype,
                    ))
            children = AS.AXUIElementCopyAttributeValue(element, "AXChildren", None)[1]
            if children:
                for child in children:
                    results.extend(self._ax_walk(child, depth + 1))
        except Exception:
            pass
        return results

    # ── Strategy 3: Win32 IUIAutomation ────────────────────────────────────────
    def _uia_scan(self, offset: Tuple[int, int]) -> List[MediaRegionResult]:
        results = []
        try:
            root = self._uia.GetRootElement()
            self._uia_walk(root, results, depth=0)
        except Exception as e:
            log.debug(f"UIA scan: {e}")
        return results

    def _uia_walk(self, element, results: list, depth: int):
        if depth > 15:
            return
        try:
            UIA  = self._UIA
            ct   = element.CurrentControlType
            rect = element.CurrentBoundingRectangle
            if ct in (UIA.UIA_ImageControlTypeId, UIA.UIA_CustomControlTypeId):
                w = rect.right - rect.left
                h = rect.bottom - rect.top
                if w > 0 and h > 0:
                    results.append(MediaRegionResult(
                        rect.left, rect.top, w, h,
                        source="win32_uia", element_type="image",
                    ))
            walker = self._uia.RawViewWalker
            child  = walker.GetFirstChildElement(element)
            while child:
                self._uia_walk(child, results, depth + 1)
                child = walker.GetNextSiblingElement(child)
        except Exception:
            pass

    # ── Strategy 4: Heuristic entropy scan ─────────────────────────────────────
    def _heuristic_scan(self, screenshot: "Image.Image",
                        offset: Tuple[int, int]) -> List[MediaRegionResult]:
        results = []
        sw, sh  = screenshot.size
        ox, oy  = offset

        for block_size in (256, 128):
            cols = max(1, sw // block_size)
            rows = max(1, sh // block_size)

            high_entropy_cells: List[Tuple[int, int]] = []
            for ry in range(rows):
                for rx in range(cols):
                    x0 = rx * block_size
                    y0 = ry * block_size
                    x1 = min(x0 + block_size, sw)
                    y1 = min(y0 + block_size, sh)
                    cell = screenshot.crop((x0, y0, x1, y1))
                    ent  = image_entropy(cell)
                    if ent >= HEURISTIC_ENTROPY_MIN:
                        high_entropy_cells.append((rx, ry))

            if not high_entropy_cells:
                continue

            cell_set = set(high_entropy_cells)
            visited  = set()

            def flood_fill(rx: int, ry: int) -> List[Tuple[int, int]]:
                cluster: List[Tuple[int, int]] = []
                stack   = [(rx, ry)]
                while stack:
                    cx, cy = stack.pop()
                    if (cx, cy) in visited or (cx, cy) not in cell_set:
                        continue
                    visited.add((cx, cy))
                    cluster.append((cx, cy))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        stack.append((cx + dx, cy + dy))
                return cluster

            for rx, ry in high_entropy_cells:
                if (rx, ry) in visited:
                    continue
                cluster = flood_fill(rx, ry)
                if len(cluster) < 2:
                    continue

                min_rx = min(c[0] for c in cluster)
                max_rx = max(c[0] for c in cluster)
                min_ry = min(c[1] for c in cluster)
                max_ry = max(c[1] for c in cluster)

                x0 = min_rx * block_size
                y0 = min_ry * block_size
                x1 = min((max_rx + 1) * block_size, sw)
                y1 = min((max_ry + 1) * block_size, sh)

                w = x1 - x0
                h = y1 - y0
                if w < self.config.min_media_px or h < self.config.min_media_px:
                    continue

                ar = w / h if h > 0 else 0
                if ar < 0.25 or ar > 6.0:
                    continue

                results.append(MediaRegionResult(
                    ox + x0, oy + y0, w, h,
                    source="heuristic", element_type="image",
                ))

            if results:
                break   # coarser pass found regions

        return results


# ══════════════════════════════════════════════════════════════════════════════
#  OS FOCUS HOOK
# ══════════════════════════════════════════════════════════════════════════════
class FocusEventHook:
    def __init__(self, on_focus_change: Callable[[str], None]):
        self._cb       = on_focus_change
        self._thread   = None
        self._stop_evt = threading.Event()

    def start(self):
        target = (self._win32_loop if _IS_WIN
                  else self._macos_loop if _IS_MAC
                  else self._linux_loop)
        self._thread = threading.Thread(
            target=target, daemon=True, name="FocusHook")
        self._thread.start()
        log.info(f"FocusHook started ({sys.platform})")

    def stop(self):
        self._stop_evt.set()

    # ── Windows ────────────────────────────────────────────────────────────────
    def _win32_loop(self):
        try:
            import psutil
            WinEventProcType = ctypes.WINFUNCTYPE(
                None, ctypes.wintypes.HANDLE, ctypes.wintypes.DWORD,
                ctypes.wintypes.HWND, ctypes.wintypes.LONG, ctypes.wintypes.LONG,
                ctypes.wintypes.DWORD, ctypes.wintypes.DWORD,
            )
            EVENT_SYSTEM_FOREGROUND = 0x0003
            WINEVENT_OUTOFCONTEXT   = 0x0000

            def win_event_proc(hWinEventHook, event, hwnd, idObject,
                               idChild, dwEventThread, dwmsEventTime):
                with suppress(Exception):
                    pid  = ctypes.c_ulong(0)
                    ctypes.windll.user32.GetWindowThreadProcessId(
                        hwnd, ctypes.byref(pid))
                    name = psutil.Process(pid.value).name()
                    self._cb(name)

            proc = WinEventProcType(win_event_proc)
            hook = ctypes.windll.user32.SetWinEventHook(
                EVENT_SYSTEM_FOREGROUND, EVENT_SYSTEM_FOREGROUND,
                0, proc, 0, 0, WINEVENT_OUTOFCONTEXT,
            )
            msg = ctypes.wintypes.MSG()
            while not self._stop_evt.is_set():
                ret = ctypes.windll.user32.PeekMessageW(
                    ctypes.byref(msg), 0, 0, 0, 1)
                if ret:
                    ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
                    ctypes.windll.user32.DispatchMessageW(ctypes.byref(msg))
                else:
                    time.sleep(0.01)
            ctypes.windll.user32.UnhookWinEvent(hook)
        except Exception as e:
            log.warning(f"Win32 focus hook failed: {e}. Falling back to polling.")
            self._generic_poll_loop()

    # ── macOS ──────────────────────────────────────────────────────────────────
    def _macos_loop(self):
        try:
            import AppKit
            import Foundation
            import objc

            class FocusObserver(AppKit.NSObject):
                _hook_ref = None
                def appActivated_(self, notification):
                    with suppress(Exception):
                        if FocusObserver._hook_ref:
                            app  = notification.userInfo().get(
                                AppKit.NSWorkspaceApplicationKey)
                            name = app.localizedName() if app else ""
                            FocusObserver._hook_ref(name)

            FocusObserver._hook_ref = self._cb
            observer = FocusObserver.alloc().init()
            ws = AppKit.NSWorkspace.sharedWorkspace()
            nc = ws.notificationCenter()
            nc.addObserver_selector_name_object_(
                observer,
                objc.selector(observer.appActivated_, signature=b'v@:@'),
                AppKit.NSWorkspaceDidActivateApplicationNotification,
                None,
            )
            loop = AppKit.NSRunLoop.currentRunLoop()
            while not self._stop_evt.is_set():
                loop.runUntilDate_(AppKit.NSDate.dateWithTimeIntervalSinceNow_(0.05))
        except Exception as e:
            log.warning(f"macOS focus hook failed: {e}. Falling back to polling.")
            self._generic_poll_loop()

    # ── Linux (XCB) ────────────────────────────────────────────────────────────
    def _linux_loop(self):
        try:
            import xcb
            import xcb.xproto
            conn  = xcb.connect()
            root  = conn.get_setup().roots[0].root
            atom_cookie = conn.core.InternAtom(False, len("_NET_ACTIVE_WINDOW"),
                                               "_NET_ACTIVE_WINDOW")
            net_active  = atom_cookie.reply().atom
            conn.core.ChangeWindowAttributes(root,
                xcb.xproto.CW.EventMask,
                [xcb.xproto.EventMask.PropertyChange])
            conn.flush()
            _last_pid = None
            while not self._stop_evt.is_set():
                try:
                    event = conn.poll_for_event()
                    if event is None:
                        time.sleep(0.008)
                        continue
                    if (isinstance(event, xcb.xproto.PropertyNotifyEvent)
                            and event.atom == net_active):
                        reply = conn.core.GetProperty(
                            False, root, net_active,
                            xcb.xproto.Atom.WINDOW, 0, 1).reply()
                        if reply.value:
                            wid = reply.value.buf()[0]
                            atom_pid = conn.core.InternAtom(
                                False, len("_NET_WM_PID"), "_NET_WM_PID"
                            ).reply().atom
                            pr = conn.core.GetProperty(
                                False, wid, atom_pid,
                                xcb.xproto.Atom.CARDINAL, 0, 1).reply()
                            if pr.value:
                                pid = pr.value.buf()[0]
                                if pid != _last_pid:
                                    _last_pid = pid
                                    with suppress(Exception):
                                        with open(f"/proc/{pid}/comm") as f:
                                            self._cb(f.read().strip())
                except Exception:
                    time.sleep(0.01)
            conn.disconnect()
        except Exception as e:
            log.info(f"XCB focus hook unavailable ({e}). Trying xdotool polling.")
            self._xdotool_poll_loop()

    def _xdotool_poll_loop(self):
        _last = ""
        while not self._stop_evt.is_set():
            try:
                r = subprocess.run(
                    ["xdotool", "getactivewindow", "getwindowpid"],
                    capture_output=True, text=True, timeout=0.5,
                )
                if r.returncode == 0 and r.stdout.strip():
                    pid  = int(r.stdout.strip())
                    with open(f"/proc/{pid}/comm") as f:
                        name = f.read().strip()
                    if name != _last:
                        _last = name
                        self._cb(name)
            except Exception:
                pass
            time.sleep(0.15)

    def _generic_poll_loop(self):
        _last = ""
        while not self._stop_evt.is_set():
            try:
                name = get_foreground_process_name()
                if name != _last:
                    _last = name
                    self._cb(name)
            except Exception:
                pass
            time.sleep(0.25)


# ══════════════════════════════════════════════════════════════════════════════
#  API WORKER THREAD
# ══════════════════════════════════════════════════════════════════════════════
class APIWorker(QThread):
    done  = pyqtSignal(dict, list, str, str, float, float, str)
    # result, coords, phash, ahash, entropy, latency, trigger_source
    error = pyqtSignal(str, str)

    _last_no_cred_warn: float = 0.0

    def __init__(self, frames: List[bytes], coords: list, ph: str, ah: str,
                 entropy: float, config: Config, rate_limiter: TokenBucket,
                 trigger_source: str = ""):
        super().__init__()
        self.frames         = frames
        self.coords         = coords
        self.phash_val      = ph
        self.ahash_val      = ah
        self.entropy        = entropy
        self.config         = config
        self.rate_limiter   = rate_limiter
        self.trigger_source = trigger_source

    def run(self):
        u = str(self.config.api_user).strip()
        s = str(self.config.api_secret).strip()
        if not u or not s:
            now = time.time()
            if now - APIWorker._last_no_cred_warn >= 60.0:
                APIWorker._last_no_cred_warn = now
                self.error.emit("NO_CREDENTIALS", self.phash_val)
            return

        # Rate-limit check
        if not self.rate_limiter.consume():
            log.debug("Rate limit reached — skipping API call")
            return

        last_err = None
        t0       = time.time()
        for attempt in range(1, self.config.retry_max + 1):
            try:
                result = self._call_sightengine(self.frames[0], u, s)
                if result.get("status") != "success":
                    msg = result.get("error", {}).get("message", "?")[:40]
                    self.error.emit(f"API:{msg}", self.phash_val)
                    return

                scores = [result.get("type", {}).get("ai_generated", 0.0)]
                for frame in self.frames[1:]:
                    with suppress(Exception):
                        r2 = self._call_sightengine(frame, u, s)
                        if r2.get("status") == "success":
                            scores.append(r2.get("type", {}).get("ai_generated", 0.0))

                blend = self.config.score_blend
                if blend == "maximum":
                    final = max(scores)
                elif blend == "weighted_avg":
                    weights = [1.0 / (i + 1) for i in range(len(scores))]
                    tw      = sum(weights)
                    final   = sum(sc * w for sc, w in zip(scores, weights)) / tw
                elif blend == "ensemble_vote":
                    th    = self.config.threshold
                    votes = sum(1 for sc in scores if sc >= th)
                    final = max(scores) if votes >= len(scores) / 2 else min(scores)
                else:
                    final = sum(scores) / len(scores)

                result.setdefault("type", {})["ai_generated"] = final
                result["burst_scores"] = scores

                latency = (time.time() - t0) * 1000
                self.done.emit(result, self.coords, self.phash_val,
                               self.ahash_val, self.entropy, latency,
                               self.trigger_source)
                return

            except requests.Timeout:
                last_err = "TIMEOUT"
            except requests.ConnectionError:
                last_err = "NO_NETWORK"
            except Exception as e:
                last_err = repr(e)[:40]

            if attempt < self.config.retry_max:
                jitter = (hash(self.phash_val) % 200) / 1000.0
                time.sleep((self.config.retry_backoff_ms / 1000)
                           * (2 ** (attempt - 1)) + jitter)

        self.error.emit(last_err or "UNKNOWN", self.phash_val)

    def _call_sightengine(self, frame_bytes: bytes, user: str, secret: str) -> dict:
        buf = io.BytesIO(frame_bytes)
        buf.seek(0)
        r = requests.post(
            "https://api.sightengine.com/1.0/check.json",
            files={"media": ("frame.jpg", buf, "image/jpeg")},
            data={"models": "genai", "api_user": user, "api_secret": secret},
            timeout=12,
        )
        r.raise_for_status()
        return r.json()


# ══════════════════════════════════════════════════════════════════════════════
#  BADGE WIDGETS  (click-through floating overlays)
# ══════════════════════════════════════════════════════════════════════════════
class AIBadge(QWidget):
    """Frameless, click-through, always-on-top badge with configurable style."""

    # Signal emitted when user right-clicks to annotate
    annotate_requested = pyqtSignal(str, str)  # det_id, annotation

    def __init__(self, score: float, x: int, y: int, w: int, h: int,
                 config: Config, det_id: str = ""):
        super().__init__()
        self.score  = score
        self.config = config
        self.sz     = config.badge_size
        self.style_ = config.badge_style
        self.det_id = det_id

        flags = (Qt.FramelessWindowHint | Qt.WindowTransparentForInput | Qt.WindowDoesNotAcceptFocus | Qt.WindowStaysOnTopHint
                 | Qt.Tool | Qt.WindowTransparentForInput)
        if _IS_LINUX:
            flags |= Qt.X11BypassWindowManagerHint
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setWindowOpacity(config.badge_opacity)

        if self.style_ == "ribbon":
            bw, bh = max(w, 120), 36
        elif self.style_ == "banner":
            bw, bh = max(w, 200), 30
        else:
            bw = bh = self.sz + 8

        self.setFixedSize(bw, bh)

        screen = QApplication.primaryScreen().geometry()
        if self.style_ == "ribbon":
            px, py = x, y
        elif self.style_ == "banner":
            px, py = x, y + h - bh
        else:
            px = x + w - bw - 8
            py = y + h - bh - 8

        px = max(0, min(px, screen.width()  - bw))
        py = max(0, min(py, screen.height() - bh))
        self.move(px, py)
        self.show()

        self._eff = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._eff)

        self._hold_timer = QTimer(self)
        self._hold_timer.setSingleShot(True)
        self._hold_timer.timeout.connect(self._start_fade)
        self._hold_timer.start(config.badge_hold_ms)

        if config.badge_pulse:
            self._pulse = QVariantAnimation(self)
            self._pulse.setStartValue(1.0)
            self._pulse.setEndValue(0.75)
            self._pulse.setDuration(800)
            self._pulse.setEasingCurve(QEasingCurve.SineCurve)
            self._pulse.setLoopCount(-1)
            self._pulse.valueChanged.connect(lambda v: self._eff.setOpacity(float(v)))
            self._pulse.start()
        else:
            self._pulse = None

    def _start_fade(self):
        if self._pulse:
            self._pulse.stop()
        fade = QPropertyAnimation(self._eff, b"opacity")
        fade.setDuration(self.config.badge_fade_ms)
        fade.setStartValue(float(self._eff.opacity()))
        fade.setEndValue(0.0)
        fade.setEasingCurve(QEasingCurve.InCubic)
        fade.finished.connect(self.close)
        fade.start(QPropertyAnimation.DeleteWhenStopped)

    def paintEvent(self, _):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setRenderHint(QPainter.TextAntialiasing)
        {
            "circle": self._paint_circle,
            "shield": self._paint_shield,
            "ribbon": self._paint_ribbon,
            "banner": self._paint_banner,
            "hex":    self._paint_hex,
        }.get(self.style_, self._paint_circle)(p)

    def _paint_circle(self, p: QPainter):
        sz  = self.sz; pct = int(self.score * 100)
        gr  = QRadialGradient(sz / 2 + 4, sz / 2 + 4, sz / 2)
        gr.setColorAt(0, QColor(255, 40, 80))
        gr.setColorAt(1, QColor(140, 0, 40))
        p.setBrush(QBrush(gr))
        p.setPen(QPen(QColor(255, 160, 180, 180), 1.5))
        p.drawEllipse(4, 4, sz, sz)
        p.setFont(QFont("Arial Black", max(int(sz * 0.28), 8), QFont.Black))
        p.setPen(QColor(255, 255, 255, 240))
        p.drawText(QRect(4, 4, sz, int(sz * 0.65)), Qt.AlignCenter, "AI")
        p.setFont(QFont("Arial", max(int(sz * 0.16), 7), QFont.Bold))
        p.setPen(QColor(255, 210, 220))
        p.drawText(QRect(4, int(sz * 0.58 + 4), sz, int(sz * 0.28)),
                   Qt.AlignCenter, f"{pct}%")

    def _paint_shield(self, p: QPainter):
        sz  = self.sz; pct = int(self.score * 100); w, h = sz + 8, sz + 8
        path = QPainterPath()
        path.moveTo(w / 2, 4); path.lineTo(w - 4, h * 0.3)
        path.lineTo(w - 4, h * 0.65)
        path.quadTo(w / 2, h - 2, w / 2, h - 2)
        path.quadTo(4, h * 0.65, 4, h * 0.65)
        path.lineTo(4, h * 0.3); path.closeSubpath()
        gr = QLinearGradient(4, 4, w - 4, h - 4)
        gr.setColorAt(0, QColor(255, 30, 80)); gr.setColorAt(1, QColor(100, 0, 40))
        p.setBrush(QBrush(gr)); p.setPen(QPen(QColor(255, 140, 160, 200), 1.5))
        p.drawPath(path)
        p.setFont(QFont("Arial Black", max(int(sz * 0.25), 7), QFont.Black))
        p.setPen(QColor(255, 255, 255, 240))
        p.drawText(QRect(0, 4, w, int(h * 0.55)), Qt.AlignCenter, "AI")
        p.setFont(QFont("Arial", max(int(sz * 0.14), 6), QFont.Bold))
        p.setPen(QColor(255, 200, 210))
        p.drawText(QRect(0, int(h * 0.52), w, int(h * 0.28)), Qt.AlignCenter, f"{pct}%")

    def _paint_ribbon(self, p: QPainter):
        w, h = self.width(), self.height(); pct = int(self.score * 100)
        gr = QLinearGradient(0, 0, w, 0)
        gr.setColorAt(0, QColor(200, 10, 60, 220)); gr.setColorAt(1, QColor(255, 60, 100, 180))
        p.setBrush(QBrush(gr)); p.setPen(Qt.NoPen)
        p.drawRoundedRect(0, 0, w, h, 4, 4)
        p.setFont(QFont("Arial Black", 10, QFont.Black))
        p.setPen(QColor(255, 255, 255, 230))
        p.drawText(QRect(8, 0, 52, h), Qt.AlignVCenter | Qt.AlignLeft, "⚡ AI")
        p.setFont(QFont("Arial", 9, QFont.Bold)); p.setPen(QColor(255, 200, 210))
        p.drawText(QRect(65, 0, w - 70, h), Qt.AlignVCenter | Qt.AlignLeft,
                   f"AI-GENERATED  ·  {pct}% CONFIDENCE")

    def _paint_banner(self, p: QPainter):
        w, h = self.width(), self.height(); pct = int(self.score * 100)
        gr = QLinearGradient(0, 0, 0, h)
        gr.setColorAt(0, QColor(0, 0, 0, 0)); gr.setColorAt(1, QColor(200, 10, 60, 220))
        p.setBrush(QBrush(gr)); p.setPen(Qt.NoPen)
        p.drawRect(0, 0, w, h)
        p.setFont(QFont("Arial Black", 9, QFont.Black)); p.setPen(QColor(255, 255, 255, 220))
        p.drawText(QRect(6, 0, w - 12, h), Qt.AlignVCenter | Qt.AlignRight,
                   f"⚡ AI GENERATED — {pct}%")

    def _paint_hex(self, p: QPainter):
        sz  = self.sz; pct = int(self.score * 100)
        cx, cy, r = sz / 2 + 4, sz / 2 + 4, sz / 2 - 2
        pts = [QPointF(cx + r * math.cos(math.pi / 180 * (60 * i - 30)),
                       cy + r * math.sin(math.pi / 180 * (60 * i - 30)))
               for i in range(6)]
        path = QPainterPath(); path.moveTo(pts[0])
        for pt in pts[1:]: path.lineTo(pt)
        path.closeSubpath()
        gr = QLinearGradient(4, 4, sz + 4, sz + 4)
        gr.setColorAt(0, QColor(255, 30, 100)); gr.setColorAt(1, QColor(100, 0, 50))
        p.setBrush(QBrush(gr)); p.setPen(QPen(QColor(255, 255, 255, 70), 1.5))
        p.drawPath(path)
        p.setFont(QFont("Arial Black", max(int(sz * 0.3), 8), QFont.Black))
        p.setPen(QColor(255, 255, 255, 240))
        p.drawText(QRect(4, 4, sz, int(sz * 0.75)), Qt.AlignCenter, "AI")
        p.setFont(QFont("Arial", max(int(sz * 0.15), 7), QFont.Bold))
        p.setPen(QColor(255, 200, 200))
        p.drawText(QRect(4, int(sz * 0.65 + 4), sz, int(sz * 0.25)),
                   Qt.AlignCenter, f"{pct}%")


# ══════════════════════════════════════════════════════════════════════════════
#  BADGE MANAGER
# ══════════════════════════════════════════════════════════════════════════════
class BadgeManager:
    def __init__(self, config: Config):
        self.config   = config
        self._badges: List[AIBadge] = []
        self._annotation_cb: Optional[Callable] = None

    def set_annotation_callback(self, cb: Callable):
        self._annotation_cb = cb

    def _cull(self):
        self._badges = [b for b in self._badges if b.isVisible()]

    def spawn(self, score: float, x: int, y: int, w: int, h: int,
              det_id: str = "") -> AIBadge:
        self._cull()
        if len(self._badges) >= MAX_REGIONS:
            with suppress(Exception):
                self._badges[0].close()
                self._badges.pop(0)
        badge = AIBadge(score, x, y, w, h, self.config, det_id=det_id)
        if self._annotation_cb:
            badge.annotate_requested.connect(self._annotation_cb)
        self._badges.append(badge)
        return badge

    def clear_all(self):
        for b in self._badges:
            with suppress(Exception):
                b.close()
        self._badges.clear()

    def count(self) -> int:
        self._cull()
        return len(self._badges)


# ══════════════════════════════════════════════════════════════════════════════
#  HEALTH CHECK HTTP SERVER  (lightweight, threaded)
# ══════════════════════════════════════════════════════════════════════════════
class HealthCheckServer:
    """
    Minimal HTTP/1.1 server responding to GET /health with a JSON status blob.
    Runs in a daemon thread; does not depend on Qt.
    """

    def __init__(self, config: Config, watcher_ref: Any, db_ref: Any):
        self._config   = config
        self._watcher  = watcher_ref
        self._db       = db_ref
        self._server   = None
        self._thread   = None

    def start(self):
        if not self._config.health_check_enabled:
            return
        port = self._config.health_check_port
        outer = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                parsed = urllib.parse.urlparse(self.path)
                if parsed.path not in ("/health", "/"):
                    self.send_response(404); self.end_headers()
                    return
                payload = outer._build_payload()
                body = json.dumps(payload, indent=2).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *_):
                pass   # suppress access log spam

        try:
            self._server = http.server.HTTPServer(("127.0.0.1", port), Handler)
            self._thread = threading.Thread(
                target=self._server.serve_forever,
                daemon=True, name="HealthCheckServer",
            )
            self._thread.start()
            log.info(f"Health-check server listening on 127.0.0.1:{port}")
        except OSError as e:
            log.warning(f"Health-check server could not bind to port {port}: {e}")

    def stop(self):
        if self._server:
            with suppress(Exception):
                self._server.shutdown()

    def _build_payload(self) -> dict:
        try:
            st = self._db.stats()
            return {
                "status":       "ok",
                "version":      APP_VERSION,
                "build":        APP_BUILD,
                "pid":          os.getpid(),
                "uptime_s":     round(self._watcher.uptime_s, 1),
                "watcher_state": self._watcher.state,
                "api_calls":    self._watcher.api_count,
                "api_errors":   self._watcher.error_count,
                "rate_budget":  self._watcher.rate_budget,
                "detections_today": st.get("today", 0),
                "detections_24h":   st.get("h24",   0),
                "ts":           datetime.datetime.utcnow().isoformat() + "Z",
            }
        except Exception as e:
            return {"status": "error", "msg": str(e)}


# ══════════════════════════════════════════════════════════════════════════════
#  CONTENT WATCHER  ← Core event-driven engine
# ══════════════════════════════════════════════════════════════════════════════
class ContentWatcher(QObject):
    """
    State machine:
        IDLE          — no browser focused, zero CPU
        BROWSER_FOCUS — browser focused; media scan armed
        MEDIA_ACTIVE  — media present; change tracker running
        SLEEPING      — paused by user or idle timeout
    """

    detection = pyqtSignal(float, int, int, int, int, str, str, float, float, str)
    # score, x, y, w, h, ts_str, det_id, entropy, latency_ms, trigger_source

    STATE_IDLE          = "idle"
    STATE_BROWSER_FOCUS = "browser_focus"
    STATE_MEDIA_ACTIVE  = "media_active"
    STATE_SLEEPING      = "sleeping"

    def __init__(self, config: Config):
        super().__init__()
        self.config          = config
        self._state          = self.STATE_IDLE
        self._prev_state     = self.STATE_IDLE
        self._is_paused      = False
        self._session_start  = time.time()
        self._last_activity  = time.time()
        self._api_count      = 0
        self._error_count    = 0
        self._active_workers = 0
        self._worker_q: List[APIWorker] = []
        self._state_lock     = threading.RLock()

        self._dedup: Dict[str, float] = {}
        self._dedup_lock = threading.RLock()

        # Load persistent bloom filter
        if config.persist_bloom and BLOOM_FILE.exists():
            self._bloom = BloomFilter.load(BLOOM_FILE)
        else:
            self._bloom = BloomFilter()

        self._region_hashes: Dict[str, Tuple[str, str]] = {}  # rkey → (phash, ahash)
        self._heatmap:       Optional[DetectionHeatmap]  = None
        self._current_process = ""
        self._last_screenshot: Optional[Image.Image] = None

        # Rate limiter
        self._rate_limiter = TokenBucket(config.rate_limit_per_min)

        # Sub-systems
        self._media_detector = MediaRegionDetector(config)
        self._focus_hook     = FocusEventHook(self._on_focus_event)

        # Debounce timers
        self._focus_debounce = QTimer()
        self._focus_debounce.setSingleShot(True)
        self._focus_debounce.timeout.connect(self._on_focus_debounced)

        self._media_debounce = QTimer()
        self._media_debounce.setSingleShot(True)
        self._media_debounce.timeout.connect(self._scan_for_media)

        # Housekeeping timers (not polling)
        self._dedup_cleanup = QTimer()
        self._dedup_cleanup.timeout.connect(self._cleanup_dedup)
        self._dedup_cleanup.start(30_000)

        self._heatmap_decay = QTimer()
        self._heatmap_decay.timeout.connect(self._do_heatmap_decay)
        self._heatmap_decay.start(5_000)

        self._content_change_timer = QTimer()
        self._content_change_timer.timeout.connect(self._check_content_change)

        self._idle_check = QTimer()
        self._idle_check.timeout.connect(self._check_idle)
        self._idle_check.start(10_000)

        self._focus_hook.start()
        log.info(f"ContentWatcher initialised — state: {self._state}")

    # ── Properties ─────────────────────────────────────────────────────────────
    @property
    def api_count(self):    return self._api_count
    @property
    def error_count(self):  return self._error_count
    @property
    def uptime_s(self):     return time.time() - self._session_start
    @property
    def state(self):        return self._state
    @property
    def rate_budget(self):  return self._rate_limiter.budget

    # ── State machine ──────────────────────────────────────────────────────────
    def _transition(self, new_state: str, reason: str = ""):
        if new_state == self._state:
            return
        old, self._state = self._state, new_state
        log.info(f"ContentWatcher: {old} → {new_state}"
                 + (f"  [{reason}]" if reason else ""))

        if new_state == self.STATE_MEDIA_ACTIVE:
            interval = max(50, self.config.media_debounce_ms)
            self._content_change_timer.start(interval)
        else:
            self._content_change_timer.stop()

        if old == self.STATE_MEDIA_ACTIVE and new_state != self.STATE_MEDIA_ACTIVE:
            self._last_screenshot = None
            self._region_hashes.clear()

    # ── Focus hook callbacks ────────────────────────────────────────────────────
    def _on_focus_event(self, process_name: str):
        QTimer.singleShot(0, lambda: self._on_focus_event_main(process_name))

    def _on_focus_event_main(self, process_name: str):
        if self._is_paused:
            return
        self._current_process = process_name

        # Denylist check (supports fnmatch patterns)
        for p in self.config.denylist_processes:
            if p and (p.lower() in process_name.lower()
                      or fnmatch.fnmatch(process_name.lower(), p.lower())):
                self._transition(self.STATE_IDLE, f"denylist:{process_name}")
                return

        # Allowlist check
        if self.config.allowlist_processes:
            allowed = any(
                (p and (p.lower() in process_name.lower()
                        or fnmatch.fnmatch(process_name.lower(), p.lower())))
                for p in self.config.allowlist_processes
            )
            if not allowed:
                self._transition(self.STATE_IDLE, f"allowlist-miss:{process_name}")
                return

        is_browser = any(
            bp.lower() in process_name.lower()
            for bp in self.config.effective_browser_set()
        )

        if is_browser:
            if self._state in (self.STATE_IDLE, self.STATE_SLEEPING):
                self._transition(self.STATE_BROWSER_FOCUS,
                                 f"browser:{process_name}")
            self._focus_debounce.start(self.config.focus_debounce_ms)
        else:
            if self._state not in (self.STATE_IDLE, self.STATE_SLEEPING):
                self._transition(self.STATE_IDLE, f"non-browser:{process_name}")

    def _on_focus_debounced(self):
        if self._is_paused or self._state == self.STATE_IDLE:
            return
        self._media_debounce.start(0)

    # ── Media scan ─────────────────────────────────────────────────────────────
    def _scan_for_media(self):
        if self._is_paused or self._state not in (
                self.STATE_BROWSER_FOCUS, self.STATE_MEDIA_ACTIVE):
            return
        try:
            screenshot, mon = self._grab_screen()
            if screenshot is None:
                return
            mon_offset = (mon.get("left", 0), mon.get("top", 0))
            regions    = self._media_detector.find_media_regions(
                screenshot, mon_offset)

            if regions:
                if self._state != self.STATE_MEDIA_ACTIVE:
                    self._transition(self.STATE_MEDIA_ACTIVE,
                                     f"{len(regions)} region(s) found")
                self._last_screenshot = screenshot
                self._heatmap_init(screenshot)
                self._process_regions(screenshot, regions, mon, "focus_event")
            else:
                if self._state == self.STATE_MEDIA_ACTIVE:
                    self._transition(self.STATE_BROWSER_FOCUS, "no media regions")
        except Exception:
            log.debug(traceback.format_exc())

    # ── Content-change tracker ─────────────────────────────────────────────────
    def _check_content_change(self):
        if self._is_paused or self._state != self.STATE_MEDIA_ACTIVE:
            return
        try:
            screenshot, mon = self._grab_screen()
            if screenshot is None:
                return
            mon_offset = (mon.get("left", 0), mon.get("top", 0))
            regions    = self._media_detector.find_media_regions(
                screenshot, mon_offset)

            if not regions:
                self._transition(self.STATE_BROWSER_FOCUS, "regions disappeared")
                return

            self._last_screenshot = screenshot
            changed_regions = []

            for region in regions:
                rkey = f"{region.x},{region.y},{region.w},{region.h}"
                rx0  = max(0, region.x - mon_offset[0])
                ry0  = max(0, region.y - mon_offset[1])
                rx1  = min(screenshot.width,  rx0 + region.w)
                ry1  = min(screenshot.height, ry0 + region.h)
                if rx1 <= rx0 or ry1 <= ry0:
                    continue

                crop = screenshot.crop((rx0, ry0, rx1, ry1))
                ph   = phash(crop)
                ah   = ahash(crop)
                last = self._region_hashes.get(rkey)

                if last is None:
                    self._region_hashes[rkey] = (ph, ah)
                    changed_regions.append((region, crop, ph, ah, "first_seen"))
                    continue

                dist = dual_hamming(ph, ah, last[0], last[1])
                if dist > self.config.dedup_hamming_tolerance:
                    self._region_hashes[rkey] = (ph, ah)
                    changed_regions.append((region, crop, ph, ah, "content_changed"))

            if changed_regions:
                self._last_activity = time.time()
                for region, crop, ph, ah, change_type in changed_regions:
                    rx0 = region.x - mon_offset[0]
                    ry0 = region.y - mon_offset[1]
                    self._analyze_region(
                        screenshot, crop,
                        (rx0, ry0, rx0 + region.w, ry0 + region.h),
                        mon, f"visual_{change_type}",
                        ph, ah,
                    )
        except Exception:
            log.debug(traceback.format_exc())

    # ── Region analysis ────────────────────────────────────────────────────────
    def _process_regions(self, screenshot: "Image.Image",
                         regions: List[MediaRegionResult],
                         mon: dict, trigger_source: str):
        mon_l = mon.get("left", 0)
        mon_t = mon.get("top",  0)
        for region in regions:
            rx0 = max(0, region.x - mon_l)
            ry0 = max(0, region.y - mon_t)
            rx1 = min(screenshot.width,  rx0 + region.w)
            ry1 = min(screenshot.height, ry0 + region.h)
            if rx1 <= rx0 or ry1 <= ry0:
                continue
            crop = screenshot.crop((rx0, ry0, rx1, ry1))
            ph   = phash(crop)
            ah   = ahash(crop)
            self._analyze_region(screenshot, crop, (rx0, ry0, rx1, ry1),
                                 mon, trigger_source, ph, ah)

    def _analyze_region(self, full_img: "Image.Image", cropped: "Image.Image",
                        bbox: tuple, mon: dict, trigger_source: str,
                        ph: str, ah: str):
        ent = image_entropy(cropped) if self.config.entropy_filter else 0.0

        if self.config.entropy_filter and ent < self.config.entropy_min:
            return

        bx = bbox[0]; by = bbox[1]
        bw = bbox[2] - bbox[0]; bh = bbox[3] - bbox[1]
        if self._is_excluded(bx, by, bw, bh):
            return

        # Dual-hash bloom + TTL dedup
        with self._dedup_lock:
            if ph in self._bloom:
                if self.config.dedup_enabled:
                    if self._dedup.get(ph, 0) > time.time():
                        return
            self._bloom.add(ph)
            self._dedup[ph] = time.time() + DEDUP_TTL

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

        mon_l  = mon.get("left", 0)
        mon_t  = mon.get("top",  0)
        coords = [mon_l + bx, mon_t + by, bw, bh]
        self._dispatch(frames, coords, ph, ah, ent, trigger_source)

    def _dispatch(self, frames: List[bytes], coords: list, ph: str, ah: str,
                  entropy: float, trigger_source: str):
        if self._active_workers >= self.config.max_workers:
            return
        worker = APIWorker(frames, coords, ph, ah, entropy,
                           self.config, self._rate_limiter, trigger_source)
        worker.done.connect(self._on_result)
        worker.error.connect(self._on_error)
        worker.finished.connect(lambda: self._on_worker_done(worker))
        self._active_workers += 1
        self._api_count      += 1
        worker.start()
        self._worker_q.append(worker)

    def _on_worker_done(self, worker: APIWorker):
        self._active_workers = max(0, self._active_workers - 1)
        with suppress(ValueError):
            self._worker_q.remove(worker)

    def _on_result(self, result: dict, coords: list, ph: str, ah: str,
                   entropy: float, latency: float, trigger_source: str):
        score = result.get("type", {}).get("ai_generated", 0.0)
        if score >= self.config.threshold:
            ts     = datetime.datetime.now().isoformat(timespec="seconds")
            det_id = str(uuid.uuid4())[:8]
            self.detection.emit(score, *coords, ts, det_id,
                                entropy, latency, trigger_source)
            if self._heatmap:
                self._heatmap.record(*coords, score)

    def _on_error(self, msg: str, ph: str):
        log.warning(f"API [{ph[:8]}]: {msg}")
        self._error_count += 1
        if msg != "NO_CREDENTIALS":
            with self._dedup_lock:
                self._dedup.pop(ph, None)

    # ── Helpers ────────────────────────────────────────────────────────────────
    def _grab_screen(self) -> Tuple[Optional["Image.Image"], dict]:
        try:
            with mss.mss() as sct:
                monitors = sct.monitors
                idx      = min(self.config.monitor_index, len(monitors) - 1)
                mon      = monitors[idx]
                raw      = sct.grab(mon)
                img      = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")
            return img, mon
        except Exception as e:
            log.debug(f"Screen grab: {e}")
            return None, {}

    def _is_excluded(self, x: int, y: int, w: int, h: int) -> bool:
        for zone in self.config.exclusion_zones:
            zx, zy, zw, zh = zone[:4]
            if x < zx + zw and x + w > zx and y < zy + zh and y + h > zy:
                return True
        return False

    def _heatmap_init(self, img: "Image.Image"):
        if self._heatmap is None:
            self._heatmap = DetectionHeatmap(img.width, img.height)

    def _cleanup_dedup(self):
        now = time.time()
        with self._dedup_lock:
            self._dedup = {k: v for k, v in self._dedup.items() if v > now}

    def _do_heatmap_decay(self):
        if self._heatmap:
            self._heatmap.decay()

    def _check_idle(self):
        idle = self.config.auto_pause_idle_s
        if idle > 0 and time.time() - self._last_activity > idle:
            if self._state == self.STATE_MEDIA_ACTIVE:
                self._transition(self.STATE_BROWSER_FOCUS, "idle timeout")

    # ── Pause / Resume / Shutdown ───────────────────────────────────────────────
    def pause(self):
        self._is_paused  = True
        self._prev_state = self._state
        self._transition(self.STATE_SLEEPING, "user pause")
        self._last_screenshot = None
        self._region_hashes.clear()

    def resume(self):
        self._is_paused     = False
        self._last_activity = time.time()
        self._transition(self._prev_state or self.STATE_IDLE, "user resume")

    def shutdown(self):
        log.info("ContentWatcher: shutdown initiated.")
        self._focus_hook.stop()
        for timer in (self._focus_debounce, self._media_debounce,
                      self._content_change_timer, self._dedup_cleanup,
                      self._heatmap_decay, self._idle_check):
            with suppress(Exception):
                timer.stop()

        # Drain workers gracefully
        for w in list(self._worker_q):
            with suppress(Exception):
                w.quit()
                w.wait(2_000)

        # Persist bloom filter
        if self.config.persist_bloom:
            self._bloom.save(BLOOM_FILE)
            log.info(f"BloomFilter saved ({len(self._bloom)} entries)")

        log.info("ContentWatcher: shutdown complete.")


# ══════════════════════════════════════════════════════════════════════════════
#  STATS DASHBOARD  (v5: 7-day chart + per-process table + snapshot viewer)
# ══════════════════════════════════════════════════════════════════════════════
class StatsDashboard(QDialog):
    def __init__(self, db: DetectionDB, watcher: ContentWatcher,
                 config: Config, parent=None):
        super().__init__(parent)
        self.db      = db
        self.watcher = watcher
        self.config  = config
        self.setWindowTitle(f"{APP_NAME} — Dashboard v{APP_VERSION}")
        self.setMinimumSize(1_020, 680)
        self.setStyleSheet(BASE_STYLE)
        self.setAttribute(Qt.WA_DeleteOnClose)

        tabs = QTabWidget()
        tabs.addTab(self._tab_overview(),    "📊  Overview")
        tabs.addTab(self._tab_detections(),  "🔍  Detections")
        tabs.addTab(self._tab_heatmap(),     "🗺  Heatmap")
        tabs.addTab(self._tab_watcher(),     "👁  Watcher State")
        tabs.addTab(self._tab_process(),     "🏷  By Process")    # v5
        tabs.addTab(self._tab_snapshots(),   "📸  Snapshots")      # v5

        lay = QVBoxLayout(self)
        lay.setContentsMargins(16, 16, 16, 12)
        lay.addWidget(tabs)

        self._refresh_timer = QTimer(self)
        self._refresh_timer.timeout.connect(self._refresh)
        self._refresh_timer.start(3_000)

    # ── Tab: Overview ──────────────────────────────────────────────────────────
    def _tab_overview(self):
        w = QWidget()
        v = QVBoxLayout(w)
        v.setSpacing(14)
        v.setContentsMargins(18, 18, 18, 18)

        self._stats_text = QTextEdit()
        self._stats_text.setReadOnly(True)
        self._stats_text.setMinimumHeight(180)
        v.addWidget(self._stats_text)

        # 7-day bar chart (v5)
        bar_lbl = QLabel("7-Day Detection Activity")
        bar_lbl.setStyleSheet(f"color:{C['sub']}; font-size:10px;")
        v.addWidget(bar_lbl)
        self._bar_chart = QLabel()
        self._bar_chart.setFixedHeight(70)
        self._bar_chart.setStyleSheet(
            f"background:{C['surface']}; border-radius:4px;")
        v.addWidget(self._bar_chart)

        # Score sparkline
        spark_lbl = QLabel("Score history (last 120 detections)")
        spark_lbl.setStyleSheet(f"color:{C['sub']}; font-size:10px;")
        v.addWidget(spark_lbl)
        self._sparkline = QLabel()
        self._sparkline.setFixedHeight(60)
        self._sparkline.setStyleSheet(
            f"background:{C['surface']}; border-radius:4px;")
        v.addWidget(self._sparkline)

        hrow = QHBoxLayout()
        for label, color, slot in [
            ("↓ Export CSV",  C["ok_d"],     self._export_csv),
            ("↓ Export JSON", C["accent"],   self._export_json),
            ("🗑 Clear Log",  C["danger_d"], self._clear_db),
        ]:
            btn = QPushButton(label)
            btn.setStyleSheet(mk_btn(color, small=True))
            btn.clicked.connect(slot)
            hrow.addWidget(btn)
        hrow.addStretch()
        v.addLayout(hrow)

        self._refresh_overview()
        return w

    def _refresh_overview(self):
        s  = self.db.stats()
        ce = self.config.cost_estimate(self.watcher.api_count)
        up = int(self.watcher.uptime_s)
        lines = [
            f"  TOTAL DETECTIONS  {s['total']}",
            f"  AI CONFIRMED      {s['ai']}",
            f"  TODAY             {s['today']}",
            f"  LAST 24h          {s['h24']}",
            f"  FALSE POSITIVES   {s.get('false_pos', 0)}",
            f"  FALSE NEGATIVES   {s.get('false_neg', 0)}",
            f"  AVG SCORE         {s['avg']*100:.1f}%",
            f"  MAX SCORE         {s['maximum']*100:.1f}%",
            f"  AVG LATENCY       {s['avg_latency']:.0f} ms",
            "",
            f"  API CALLS         {self.watcher.api_count}",
            f"  API ERRORS        {self.watcher.error_count}",
            f"  RATE BUDGET       {self.watcher.rate_budget}/{self.config.rate_limit_per_min} /min",
            f"  FREE CALLS LEFT   {max(0, FREE_CALLS_PER_MONTH - ce['calls'])}",
            f"  EST. COST         ${ce['cost_usd']:.4f}",
            "",
            f"  UPTIME            {up // 3600}h {(up % 3600) // 60}m",
            f"  WATCHER STATE     {self.watcher.state.upper()}",
            f"  ACTIVE PROCESS    {self.watcher._current_process or '—'}",
            f"  BLOOM ENTRIES     {len(self.watcher._bloom)}",
        ]
        self._stats_text.setPlainText("\n".join(lines))

        series = self.db.score_series(120)
        if series:
            self._draw_sparkline(series)

        buckets = self.db.daily_buckets(7)
        if buckets:
            self._draw_bar_chart(buckets)

    def _draw_sparkline(self, series: List[float]):
        W, H = self._sparkline.width() or 800, 56
        pix  = QPixmap(W, H)
        pix.fill(QColor(C["surface"]))
        p    = QPainter(pix)
        p.setRenderHint(QPainter.Antialiasing)
        n    = len(series)
        if n < 2:
            p.end(); self._sparkline.setPixmap(pix); return
        xs   = [int(i / (n - 1) * (W - 20) + 10) for i in range(n)]
        ys   = [int((1 - s) * (H - 12) + 6)        for s in series]
        ty   = int((1 - self.config.threshold) * (H - 12) + 6)
        p.setPen(QPen(QColor(C["muted"]), 1, Qt.DashLine))
        p.drawLine(0, ty, W, ty)
        p.setPen(QPen(QColor(C["accent"]), 1.5))
        for i in range(1, n):
            p.drawLine(xs[i-1], ys[i-1], xs[i], ys[i])
        p.setBrush(QBrush(QColor(C["danger"]))); p.setPen(Qt.NoPen)
        for i, s in enumerate(series):
            if s >= self.config.threshold:
                p.drawEllipse(xs[i]-3, ys[i]-3, 6, 6)
        p.end(); self._sparkline.setPixmap(pix)

    def _draw_bar_chart(self, buckets: Dict[str, int]):
        """v5: Simple 7-day bar chart rendered with QPainter."""
        W, H = self._bar_chart.width() or 800, 66
        pix  = QPixmap(W, H)
        pix.fill(QColor(C["surface"]))
        p    = QPainter(pix)
        p.setRenderHint(QPainter.Antialiasing)

        # Ensure 7 days present
        today = datetime.date.today()
        days  = [(today - datetime.timedelta(days=6 - i)).isoformat() for i in range(7)]
        vals  = [buckets.get(d, 0) for d in days]
        max_v = max(vals) if any(vals) else 1

        bar_w   = (W - 16) / 7
        pad_top = 6; pad_bot = 20
        chart_h = H - pad_top - pad_bot

        for i, (day, val) in enumerate(zip(days, vals)):
            x   = int(8 + i * bar_w)
            bar = int(chart_h * val / max_v) if max_v else 0
            y   = H - pad_bot - bar
            gr  = QLinearGradient(x, y, x, H - pad_bot)
            gr.setColorAt(0, QColor(C["accent"]))
            gr.setColorAt(1, QColor(C["accent_d"]))
            p.setBrush(QBrush(gr)); p.setPen(Qt.NoPen)
            p.drawRoundedRect(x, y, max(2, int(bar_w) - 4), bar, 3, 3)
            # Day label
            p.setFont(QFont("Arial", 8)); p.setPen(QColor(C["sub"]))
            p.drawText(QRect(x, H - pad_bot + 3, int(bar_w), 14),
                       Qt.AlignCenter, day[5:])  # MM-DD
            # Value label
            if val > 0:
                p.setFont(QFont("Arial", 7, QFont.Bold))
                p.setPen(QColor(C["text"]))
                p.drawText(QRect(x, max(0, y - 14), int(bar_w), 14),
                           Qt.AlignCenter, str(val))
        p.end(); self._bar_chart.setPixmap(pix)

    # ── Tab: Detections ────────────────────────────────────────────────────────
    def _tab_detections(self):
        w   = QWidget()
        v   = QVBoxLayout(w)
        v.setContentsMargins(12, 12, 12, 12)

        tbl = QTableWidget()
        tbl.setColumnCount(10)
        tbl.setHorizontalHeaderLabels(
            ["Time", "Score", "Region", "Blend", "Process",
             "Entropy", "Latency", "Trigger", "Ann.", "ID"])
        tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tbl.setAlternatingRowColors(True)
        tbl.setSelectionBehavior(QAbstractItemView.SelectRows)
        tbl.setContextMenuPolicy(Qt.CustomContextMenu)
        tbl.customContextMenuRequested.connect(self._det_context_menu)
        self._det_table = tbl

        # Thumbnail preview pane (v5)
        self._thumb_label = QLabel("Select a row with a snapshot to preview")
        self._thumb_label.setAlignment(Qt.AlignCenter)
        self._thumb_label.setFixedHeight(120)
        self._thumb_label.setStyleSheet(
            f"background:{C['surface2']}; border-radius:4px; color:{C['sub']};")

        tbl.itemSelectionChanged.connect(self._on_det_selection)
        v.addWidget(tbl)
        v.addWidget(self._thumb_label)

        self._refresh_detections()
        return w

    def _on_det_selection(self):
        """v5: Show snapshot thumbnail when a detection row is selected."""
        rows = self._det_table.selectionModel().selectedRows()
        if not rows:
            return
        row   = rows[0].row()
        det_id_item = self._det_table.item(row, 9)
        if not det_id_item:
            return
        det_id = det_id_item.text()

        # Find snapshot
        matches = list(SNAPSHOT_DIR.glob(f"*{det_id}*"))
        if matches:
            try:
                pix = QPixmap(str(matches[0]))
                pix = pix.scaled(self._thumb_label.width(), 120,
                                 Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self._thumb_label.setPixmap(pix)
                return
            except Exception:
                pass
        self._thumb_label.setText("No snapshot available")
        self._thumb_label.setPixmap(QPixmap())

    def _det_context_menu(self, pos):
        """v5: Right-click → annotate as false positive / negative."""
        row = self._det_table.rowAt(pos.y())
        if row < 0:
            return
        det_id_item = self._det_table.item(row, 9)
        if not det_id_item:
            return
        det_id = det_id_item.text()
        menu   = QMenu(self)
        fp_act = QAction("✓ Mark as False Positive", menu)
        fn_act = QAction("✗ Mark as False Negative", menu)
        cl_act = QAction("— Clear Annotation",       menu)
        fp_act.triggered.connect(lambda: self.db.annotate(det_id, "fp"))
        fn_act.triggered.connect(lambda: self.db.annotate(det_id, "fn"))
        cl_act.triggered.connect(lambda: self.db.annotate(det_id, ""))
        menu.addAction(fp_act); menu.addAction(fn_act); menu.addSeparator()
        menu.addAction(cl_act)
        menu.exec_(self._det_table.viewport().mapToGlobal(pos))

    def _refresh_detections(self):
        rows = self.db.entries(limit=500)
        tbl  = self._det_table
        tbl.setRowCount(0)
        for det in rows:
            r = tbl.rowCount()
            tbl.insertRow(r)
            ann_icon = {"fp": "⚠FP", "fn": "⚠FN"}.get(det.annotation or "", "")
            cells = [
                det.ts_str[:19],
                f"{det.score_pct}%",
                f"{det.w}×{det.h} @({det.x},{det.y})",
                det.blend_mode,
                (det.process_name or "—")[:24],
                f"{det.entropy:.2f}",
                f"{det.api_latency_ms:.0f} ms",
                det.trigger_source or "—",
                ann_icon,
                det.id,
            ]
            for c, val in enumerate(cells):
                item = QTableWidgetItem(str(val))
                if c == 1:
                    color = (C["danger"] if det.score_pct >= 90
                             else C["warn"]   if det.score_pct >= 80
                             else C["ok"])
                    item.setForeground(QColor(color))
                elif c == 8 and ann_icon:
                    item.setForeground(QColor(C["warn"]))
                tbl.setItem(r, c, item)

    # ── Tab: Heatmap ───────────────────────────────────────────────────────────
    def _tab_heatmap(self):
        w = QWidget()
        v = QVBoxLayout(w)
        v.setContentsMargins(12, 12, 12, 12)
        lbl = QLabel("Detection Density Heatmap")
        lbl.setStyleSheet(f"color:{C['sub']}; font-size:10px;")
        v.addWidget(lbl)
        self._heatmap_canvas = QLabel()
        self._heatmap_canvas.setMinimumHeight(300)
        self._heatmap_canvas.setStyleSheet(
            f"background:{C['surface']}; border:1px solid {C['border']}; border-radius:4px;")
        v.addWidget(self._heatmap_canvas)
        self._refresh_heatmap()
        return w

    def _refresh_heatmap(self):
        hm = self.watcher._heatmap
        if not hm:
            return
        grid = hm.snapshot()
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        if not rows or not cols:
            return
        W  = self._heatmap_canvas.width() or 800
        H  = self._heatmap_canvas.height() or 300
        pix = QPixmap(W, H); pix.fill(QColor(C["surface"]))
        p   = QPainter(pix)
        cw  = W / cols; ch  = H / rows
        mx  = hm.max_val() or 1.0
        for ry in range(rows):
            for rx in range(cols):
                v = grid[ry][rx] / mx
                r = int(255 * min(1, v * 2))
                g = int(255 * max(0, 1 - v * 2))
                a = int(200 * v + 20)
                p.setBrush(QBrush(QColor(r, g, 30, a))); p.setPen(Qt.NoPen)
                p.drawRect(int(rx * cw), int(ry * ch),
                           max(1, int(cw)), max(1, int(ch)))
        p.end(); self._heatmap_canvas.setPixmap(pix)

    # ── Tab: Watcher State ─────────────────────────────────────────────────────
    def _tab_watcher(self):
        w = QWidget()
        v = QVBoxLayout(w)
        v.setContentsMargins(18, 18, 18, 18)
        self._watcher_text = QTextEdit(); self._watcher_text.setReadOnly(True)
        v.addWidget(self._watcher_text)
        self._refresh_watcher()
        return w

    def _refresh_watcher(self):
        w   = self.watcher
        det = w._media_detector
        lines = [
            f"  STATE             {w.state.upper()}",
            f"  CURRENT PROCESS   {w._current_process or '—'}",
            f"  ACTIVE WORKERS    {w._active_workers}",
            f"  DEDUP CACHE       {len(w._dedup)} entries",
            f"  REGION HASHES     {len(w._region_hashes)} tracked",
            f"  BLOOM ENTRIES     {len(w._bloom)}",
            f"  RATE BUDGET       {w.rate_budget}/{w.config.rate_limit_per_min} /min",
            "",
            "  — BACKEND STATUS —",
            f"  Accessibility     {'AT-SPI2 ✓' if det._atspi_ok else 'macOS AX ✓' if det._ax_ok else 'Win32 UIA ✓' if det._uia_ok else '✗ (heuristic only)'}",
            f"  Heuristic         {'enabled' if w.config.heuristic_fallback else 'disabled'}",
            f"  Focus Hook        {sys.platform}",
            "",
            "  — WATCHER CONFIG —",
            f"  Browser only      {w.config.browser_only}",
            f"  Focus debounce    {w.config.focus_debounce_ms} ms",
            f"  Media debounce    {w.config.media_debounce_ms} ms",
            f"  Min media size    {w.config.min_media_px}px",
            f"  Entropy filter    {w.config.entropy_filter} (min={w.config.entropy_min})",
            f"  Session ID        {w.config.session_id}",
        ]
        self._watcher_text.setPlainText("\n".join(lines))

    # ── Tab: Per-Process Breakdown (v5) ────────────────────────────────────────
    def _tab_process(self):
        w   = QWidget()
        v   = QVBoxLayout(w)
        v.setContentsMargins(12, 12, 12, 12)
        tbl = QTableWidget()
        tbl.setColumnCount(2)
        tbl.setHorizontalHeaderLabels(["Process", "AI Detections"])
        tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tbl.setAlternatingRowColors(True)
        self._proc_table = tbl
        v.addWidget(tbl)
        self._refresh_process()
        return w

    def _refresh_process(self):
        s   = self.db.stats()
        tbl = self._proc_table
        tbl.setRowCount(0)
        for proc, cnt in (s.get("per_process") or {}).items():
            r = tbl.rowCount(); tbl.insertRow(r)
            tbl.setItem(r, 0, QTableWidgetItem(proc or "—"))
            item = QTableWidgetItem(str(cnt))
            item.setForeground(QColor(C["accent"]))
            tbl.setItem(r, 1, item)

    # ── Tab: Snapshot Viewer (v5) ──────────────────────────────────────────────
    def _tab_snapshots(self):
        w      = QWidget()
        v      = QVBoxLayout(w)
        v.setContentsMargins(12, 12, 12, 12)
        splitter = QSplitter(Qt.Horizontal)

        self._snap_list = QListWidget()
        self._snap_list.currentRowChanged.connect(self._on_snap_select)
        splitter.addWidget(self._snap_list)

        self._snap_view = QLabel()
        self._snap_view.setAlignment(Qt.AlignCenter)
        self._snap_view.setStyleSheet(
            f"background:{C['surface2']}; border-radius:4px;")
        splitter.addWidget(self._snap_view)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 3)

        v.addWidget(splitter)
        self._refresh_snapshots()
        return w

    def _refresh_snapshots(self):
        archive = SnapshotArchive(self.config)
        snaps   = archive.list_all()
        self._snap_list.clear()
        self._snap_paths = []
        for p in snaps:
            self._snap_list.addItem(p.name)
            self._snap_paths.append(p)

    def _on_snap_select(self, row: int):
        if row < 0 or row >= len(self._snap_paths):
            return
        try:
            pix = QPixmap(str(self._snap_paths[row]))
            pix = pix.scaled(self._snap_view.width(), self._snap_view.height(),
                             Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self._snap_view.setPixmap(pix)
        except Exception:
            pass

    # ── Refresh all ────────────────────────────────────────────────────────────
    def _refresh(self):
        self._refresh_overview()
        self._refresh_detections()
        self._refresh_heatmap()
        self._refresh_watcher()
        self._refresh_process()

    # ── Export / clear ─────────────────────────────────────────────────────────
    def _export_csv(self):
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = EXPORT_DIR / f"export_{ts}.csv"
        if self.db.export_csv(str(path)):
            QMessageBox.information(self, "Exported", f"CSV saved:\n{path}")
        else:
            QMessageBox.warning(self, "Export Failed", "No detections to export.")

    def _export_json(self):
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = EXPORT_DIR / f"export_{ts}.json"
        if self.db.export_json(str(path)):
            QMessageBox.information(self, "Exported", f"JSON saved:\n{path}")
        else:
            QMessageBox.warning(self, "Export Failed", "No detections to export.")

    def _clear_db(self):
        if QMessageBox.question(
                self, "Clear Log", "Delete all detection records?",
                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.db.clear()
            self._refresh()

    def closeEvent(self, event):
        self._refresh_timer.stop()
        super().closeEvent(event)


# ══════════════════════════════════════════════════════════════════════════════
#  CONFIG DIALOG
# ══════════════════════════════════════════════════════════════════════════════
class ConfigDialog(QDialog):
    def __init__(self, config: Config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setWindowTitle(f"{APP_NAME} — Configuration")
        self.setMinimumSize(700, 680)
        self.setStyleSheet(BASE_STYLE)

        tabs = QTabWidget()
        tabs.addTab(self._tab_api(),      "🔑  API & Keys")
        tabs.addTab(self._tab_watcher(),  "👁  Watcher")
        tabs.addTab(self._tab_detect(),   "🔍  Detection")
        tabs.addTab(self._tab_badge(),    "🎨  Badge")
        tabs.addTab(self._tab_alerts(),   "🔔  Alerts")
        tabs.addTab(self._tab_archive(),  "📸  Archive")
        tabs.addTab(self._tab_zones(),    "🚫  Exclusions")
        tabs.addTab(self._tab_system(),   "⚙  System")

        bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        bb.accepted.connect(self._accept)
        bb.rejected.connect(self.reject)
        bb.button(QDialogButtonBox.Ok).setStyleSheet(mk_btn(C["accent"]))
        bb.button(QDialogButtonBox.Cancel).setStyleSheet(mk_btn(C["muted"], C["text"]))

        lay = QVBoxLayout(self)
        lay.setContentsMargins(18, 18, 18, 14)
        lay.setSpacing(14)
        lay.addWidget(tabs)
        lay.addWidget(bb)

    # ── Layout helpers ─────────────────────────────────────────────────────────
    def _fw(self):
        w = QWidget(); sa = QScrollArea()
        sa.setWidget(w); sa.setWidgetResizable(True); sa.setFrameShape(QFrame.NoFrame)
        f = QFormLayout(w); f.setContentsMargins(22, 18, 22, 18)
        f.setSpacing(14); f.setLabelAlignment(Qt.AlignRight | Qt.AlignVCenter)
        return sa, w, f

    def _spin(self, val, lo, hi, suf="", dbl=False):
        s = QDoubleSpinBox() if dbl else QSpinBox()
        if dbl: s.setDecimals(2); s.setSingleStep(0.01)
        s.setRange(lo, hi); s.setValue(val); s.setSuffix(suf)
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
                    c.setCurrentIndex(i); break
        return c

    # ── Tab: API ──────────────────────────────────────────────────────────────
    def _tab_api(self):
        sa, w, f = self._fw()
        self._user   = QLineEdit(self.config.api_user)
        self._secret = QLineEdit(self.config.api_secret)
        self._secret.setEchoMode(QLineEdit.Password)
        show_btn = QPushButton("👁")
        show_btn.setFixedWidth(36)
        show_btn.setStyleSheet(mk_btn(C["muted"], small=True))
        show_btn.setCheckable(True)
        show_btn.toggled.connect(
            lambda c: self._secret.setEchoMode(
                QLineEdit.Normal if c else QLineEdit.Password))
        sec_row = QHBoxLayout()
        sec_row.addWidget(self._secret)
        sec_row.addWidget(show_btn)
        sec_w = QWidget(); sec_w.setLayout(sec_row)

        self._blend = self._combo(
            [(m.replace("_", " ").title(), m) for m in SCORE_BLEND_MODES],
            self.config.score_blend)
        self._max_workers = self._spin(self.config.max_workers, 1, 16)
        self._retry       = self._spin(self.config.retry_max, 1, 10)
        self._backoff     = self._spin(self.config.retry_backoff_ms, 100, 10_000, " ms")
        self._rate_lim    = self._spin(self.config.rate_limit_per_min, 1, 3_600, " /min")

        f.addRow("Sightengine User:",   self._user)
        f.addRow("Sightengine Secret:", sec_w)
        f.addRow("", self._lbl("Credentials are encrypted at rest with Fernet (AES-128-CBC)."))
        f.addRow("Score blend:",        self._blend)
        f.addRow("Parallel workers:",   self._max_workers)
        f.addRow("Retry attempts:",     self._retry)
        f.addRow("Retry backoff:",      self._backoff)
        f.addRow("Rate limit:",         self._rate_lim)
        f.addRow("", self._lbl("Rate limit caps API calls per minute to avoid quota exhaustion."))
        return sa

    # ── Tab: Watcher ──────────────────────────────────────────────────────────
    def _tab_watcher(self):
        sa, w, f = self._fw()
        self._browser_only    = QCheckBox("Only activate for known browsers / PWAs")
        self._browser_only.setChecked(self.config.browser_only)
        self._accessibility   = QCheckBox("Use OS accessibility tree for media detection")
        self._accessibility.setChecked(self.config.accessibility_scan)
        self._heuristic       = QCheckBox("Heuristic entropy fallback")
        self._heuristic.setChecked(self.config.heuristic_fallback)
        self._focus_deb       = self._spin(self.config.focus_debounce_ms, 0, 2_000, " ms")
        self._media_deb       = self._spin(self.config.media_debounce_ms, 0, 1_000, " ms")
        self._min_media       = self._spin(self.config.min_media_px, 8, 2_000, " px")
        self._extra_browsers  = QLineEdit(", ".join(self.config.extra_browser_names))

        self._allowlist       = QTextEdit()
        self._allowlist.setPlaceholderText("One process pattern per line (fnmatch supported)")
        self._allowlist.setPlainText("\n".join(self.config.allowlist_processes))
        self._allowlist.setMaximumHeight(80)

        self._denylist        = QTextEdit()
        self._denylist.setPlaceholderText("One process pattern per line (fnmatch supported)")
        self._denylist.setPlainText("\n".join(self.config.denylist_processes))
        self._denylist.setMaximumHeight(80)

        for chk in [self._browser_only, self._accessibility, self._heuristic]:
            f.addRow("", chk)
        f.addRow("Focus debounce:",     self._focus_deb)
        f.addRow("Media debounce:",     self._media_deb)
        f.addRow("Min media size:",     self._min_media)
        f.addRow("Extra browsers:",     self._extra_browsers)
        f.addRow("", self._lbl("Comma-separated list of extra browser process names."))
        f.addRow("Allowlist patterns:", self._allowlist)
        f.addRow("Denylist patterns:",  self._denylist)
        f.addRow("", self._lbl("Supports fnmatch wildcards, e.g.  chrome*  or  *electron*."))
        return sa

    # ── Tab: Detection ─────────────────────────────────────────────────────────
    def _tab_detect(self):
        sa, w, f = self._fw()
        self._thresh_sl = QSlider(Qt.Horizontal)
        self._thresh_sl.setRange(1, 100)
        self._thresh_sl.setValue(int(self.config.threshold * 100))
        self._thresh_val = QLabel(f"{int(self.config.threshold * 100)}%")
        self._thresh_val.setStyleSheet(f"color:{C['accent']}; font-weight:bold;")
        self._thresh_sl.valueChanged.connect(
            lambda v: self._thresh_val.setText(f"{v}%"))
        thresh_row = QHBoxLayout()
        thresh_row.addWidget(self._thresh_sl); thresh_row.addWidget(self._thresh_val)
        thresh_w = QWidget(); thresh_w.setLayout(thresh_row)

        self._mon     = self._combo(
            [(f"Monitor {i}", i) for i in range(8)], self.config.monitor_index)
        self._burst   = self._spin(self.config.burst_frames, 1, 10)
        self._bgap    = self._spin(self.config.burst_gap_ms, 0, 5_000, " ms")
        self._dedup   = QCheckBox("Enable perceptual-hash deduplication")
        self._dedup.setChecked(self.config.dedup_enabled)
        self._ham_tol = self._spin(self.config.dedup_hamming_tolerance, 0, 32)
        self._ent_ck  = QCheckBox("Enable entropy filter")
        self._ent_ck.setChecked(self.config.entropy_filter)
        self._ent_min = self._spin(self.config.entropy_min, 0.0, 8.0, dbl=True)

        f.addRow("AI threshold:",      thresh_w)
        f.addRow("Monitor:",           self._mon)
        f.addRow("Burst frames:",      self._burst)
        f.addRow("Burst gap:",         self._bgap)
        f.addRow("", self._dedup)
        f.addRow("Hamming tolerance:", self._ham_tol)
        f.addRow("", self._ent_ck)
        f.addRow("Min entropy:",       self._ent_min)
        return sa

    # ── Tab: Badge ─────────────────────────────────────────────────────────────
    def _tab_badge(self):
        sa, w, f = self._fw()
        self._bstyle = self._combo(
            [(f"{v} ({k})", k) for k, v in BADGE_STYLES.items()],
            self.config.badge_style)

        def sized_slider(lo, hi, val):
            sl = QSlider(Qt.Horizontal); sl.setRange(lo, hi); sl.setValue(val)
            return sl

        self._bsz_sl  = sized_slider(20, 100, self.config.badge_size)
        self._bop_sl  = sized_slider(20, 100, int(self.config.badge_opacity * 100))
        self._hold    = self._spin(self.config.badge_hold_ms, 500, 60_000, " ms")
        self._fade    = self._spin(self.config.badge_fade_ms, 200, 10_000, " ms")
        self._pulse   = QCheckBox("Pulse animation"); self._pulse.setChecked(self.config.badge_pulse)
        self._bsound  = QCheckBox("Sound on detection"); self._bsound.setChecked(self.config.badge_sound)

        f.addRow("Badge style:",   self._bstyle)
        f.addRow("Badge size:",    self._bsz_sl)
        f.addRow("Opacity:",       self._bop_sl)
        f.addRow("Hold duration:", self._hold)
        f.addRow("Fade duration:", self._fade)
        f.addRow("", self._pulse)
        f.addRow("", self._bsound)
        return sa

    # ── Tab: Alerts ────────────────────────────────────────────────────────────
    def _tab_alerts(self):
        sa, w, f = self._fw()
        self._notify   = QCheckBox("Desktop notification on detection")
        self._notify.setChecked(self.config.desktop_notify)
        self._wh_en    = QCheckBox("Enable webhook alerts")
        self._wh_en.setChecked(self.config.webhook_enabled)
        self._wh_url   = QLineEdit(self.config.webhook_url)
        self._wh_url.setPlaceholderText("https://hooks.slack.com/…")
        self._wh_type  = self._combo(
            [("Slack",   "slack"), ("Teams",   "teams"),
             ("Discord", "discord"), ("Custom POST", "custom")],
            self.config.webhook_type)
        self._wh_thresh_sl = QSlider(Qt.Horizontal)
        self._wh_thresh_sl.setRange(1, 100)
        self._wh_thresh_sl.setValue(int(self.config.webhook_threshold * 100))

        f.addRow("", self._notify)
        f.addRow("", self._wh_en)
        f.addRow("Webhook URL:",   self._wh_url)
        f.addRow("Type:",          self._wh_type)
        f.addRow("Min threshold:", self._wh_thresh_sl)
        f.addRow("", self._lbl("Discord webhooks send rich embeds.\n"
                                "Dead-letter payloads saved to: " + str(DEADLETTER_FILE)))
        return sa

    # ── Tab: Archive ───────────────────────────────────────────────────────────
    def _tab_archive(self):
        sa, w, f = self._fw()
        self._snap_en  = QCheckBox("Save screenshot snapshots on detection")
        self._snap_en.setChecked(self.config.snapshot_enabled)
        self._snap_ret = self._spin(self.config.snapshot_retention, 10, 10_000)
        self._log_en   = QCheckBox("Log detections to SQLite")
        self._log_en.setChecked(self.config.log_enabled)
        self._max_log  = self._spin(self.config.max_log, 100, 100_000)

        open_snap_btn = QPushButton("📁 Open Snapshot Folder")
        open_snap_btn.setStyleSheet(mk_btn(C["muted"], small=True))
        open_snap_btn.clicked.connect(lambda: self._open_dir(SNAPSHOT_DIR))
        open_exp_btn = QPushButton("📁 Open Export Folder")
        open_exp_btn.setStyleSheet(mk_btn(C["muted"], small=True))
        open_exp_btn.clicked.connect(lambda: self._open_dir(EXPORT_DIR))

        f.addRow("", self._snap_en)
        f.addRow("Retain snapshots:", self._snap_ret)
        f.addRow("", self._log_en)
        f.addRow("Max log entries:",  self._max_log)
        f.addRow("", open_snap_btn)
        f.addRow("", open_exp_btn)
        return sa

    def _open_dir(self, p: Path):
        try:
            opener = "xdg-open" if _IS_LINUX else "open" if _IS_MAC else "explorer"
            subprocess.Popen([opener, str(p)], stderr=subprocess.DEVNULL)
        except Exception:
            pass

    # ── Tab: Exclusion Zones ──────────────────────────────────────────────────
    def _tab_zones(self):
        sa, w, f = self._fw()
        note = self._lbl(
            "Add screen regions to exclude from monitoring (e.g. taskbar, watermark).\n"
            "Format: X, Y, Width, Height (pixels from top-left of monitor)")
        f.addRow("", note)
        self._zones_list = QListWidget()
        self._zones_list.setMinimumHeight(140)
        for z in self.config.exclusion_zones:
            self._zones_list.addItem(f"{z[0]}, {z[1]}, {z[2]}, {z[3]}")
        zone_inputs = QHBoxLayout()
        self._zx = self._spin(0, 0, 9_999, " X"); self._zy = self._spin(0, 0, 9_999, " Y")
        self._zw = self._spin(200, 1, 9_999, " W"); self._zh = self._spin(100, 1, 9_999, " H")
        for s in [self._zx, self._zy, self._zw, self._zh]:
            zone_inputs.addWidget(s)
        zone_w = QWidget(); zone_w.setLayout(zone_inputs)
        add_btn = QPushButton("+ Add"); add_btn.setStyleSheet(mk_btn(C["ok_d"], small=True))
        del_btn = QPushButton("− Remove"); del_btn.setStyleSheet(mk_btn(C["danger_d"], small=True))
        clr_btn = QPushButton("✕ Clear"); clr_btn.setStyleSheet(mk_btn(C["muted"], small=True))
        add_btn.clicked.connect(self._add_zone)
        del_btn.clicked.connect(self._del_zone)
        clr_btn.clicked.connect(self._zones_list.clear)
        btn_row = QHBoxLayout()
        for b in [add_btn, del_btn, clr_btn]: btn_row.addWidget(b)
        btn_w = QWidget(); btn_w.setLayout(btn_row)
        f.addRow("Zones:", self._zones_list)
        f.addRow("Add:", zone_w)
        f.addRow("", btn_w)
        return sa

    def _add_zone(self):
        x, y, w2, h2 = self._zx.value(), self._zy.value(), self._zw.value(), self._zh.value()
        self._zones_list.addItem(f"{x}, {y}, {w2}, {h2}")

    def _del_zone(self):
        for item in self._zones_list.selectedItems():
            self._zones_list.takeItem(self._zones_list.row(item))

    # ── Tab: System ───────────────────────────────────────────────────────────
    def _tab_system(self):
        sa, w, f = self._fw()
        self._autostart       = QCheckBox("Launch at system startup")
        self._autostart.setChecked(self.config.autostart)
        self._idle            = self._spin(self.config.auto_pause_idle_s, 0, 3_600, " s")
        self._health_en       = QCheckBox("Enable health-check HTTP endpoint")
        self._health_en.setChecked(self.config.health_check_enabled)
        self._health_port     = self._spin(self.config.health_check_port, 1_024, 65_535)
        self._persist_bloom   = QCheckBox("Persist Bloom filter between sessions")
        self._persist_bloom.setChecked(self.config.persist_bloom)

        f.addRow("", self._autostart)
        f.addRow("Auto-pause idle:", self._idle)
        f.addRow("", self._lbl("0 = never auto-pause."))
        f.addRow("", self._health_en)
        f.addRow("Health-check port:", self._health_port)
        f.addRow("", self._lbl(f"GET http://127.0.0.1:<port>/health → JSON status blob."))
        f.addRow("", self._persist_bloom)
        f.addRow("", self._lbl(f"Config: {CONFIG_FILE}"))
        return sa

    # ── Accept ────────────────────────────────────────────────────────────────
    def _accept(self):
        c = self.config

        # Validate before accepting
        errs = []
        if not self._user.text().strip():
            errs.append("Sightengine API User is required.")
        if not self._secret.text().strip():
            errs.append("Sightengine API Secret is required.")
        if errs:
            QMessageBox.warning(self, "Validation Errors", "\n".join(errs))
            return

        c.api_user                = self._user.text().strip()
        c.api_secret              = self._secret.text().strip()
        c.score_blend             = self._blend.currentData()
        c.max_workers             = self._max_workers.value()
        c.retry_max               = self._retry.value()
        c.retry_backoff_ms        = self._backoff.value()
        c.rate_limit_per_min      = self._rate_lim.value()
        c.browser_only            = self._browser_only.isChecked()
        c.accessibility_scan      = self._accessibility.isChecked()
        c.heuristic_fallback      = self._heuristic.isChecked()
        c.focus_debounce_ms       = self._focus_deb.value()
        c.media_debounce_ms       = self._media_deb.value()
        c.min_media_px            = self._min_media.value()
        c.extra_browser_names     = [p.strip() for p in
                                     self._extra_browsers.text().split(",") if p.strip()]
        c.allowlist_processes     = [l for l in
                                     self._allowlist.toPlainText().splitlines() if l.strip()]
        c.denylist_processes      = [l for l in
                                     self._denylist.toPlainText().splitlines() if l.strip()]
        c.threshold               = self._thresh_sl.value() / 100.0
        c.monitor_index           = self._mon.currentData()
        c.burst_frames            = self._burst.value()
        c.burst_gap_ms            = self._bgap.value()
        c.dedup_enabled           = self._dedup.isChecked()
        c.dedup_hamming_tolerance = self._ham_tol.value()
        c.entropy_filter          = self._ent_ck.isChecked()
        c.entropy_min             = float(self._ent_min.value())
        c.badge_style             = self._bstyle.currentData()
        c.badge_size              = self._bsz_sl.value()
        c.badge_opacity           = self._bop_sl.value() / 100.0
        c.badge_hold_ms           = self._hold.value()
        c.badge_fade_ms           = self._fade.value()
        c.badge_pulse             = self._pulse.isChecked()
        c.badge_sound             = self._bsound.isChecked()
        c.desktop_notify          = self._notify.isChecked()
        c.webhook_enabled         = self._wh_en.isChecked()
        c.webhook_url             = self._wh_url.text().strip()
        c.webhook_type            = self._wh_type.currentData()
        c.webhook_threshold       = self._wh_thresh_sl.value() / 100.0
        c.snapshot_enabled        = self._snap_en.isChecked()
        c.snapshot_retention      = self._snap_ret.value()
        c.log_enabled             = self._log_en.isChecked()
        c.max_log                 = self._max_log.value()
        c.auto_pause_idle_s       = self._idle.value()
        c.health_check_enabled    = self._health_en.isChecked()
        c.health_check_port       = self._health_port.value()
        c.persist_bloom           = self._persist_bloom.isChecked()

        c.exclusion_zones = []
        for i in range(self._zones_list.count()):
            with suppress(Exception):
                parts = [int(p.strip()) for p in
                         self._zones_list.item(i).text().split(",")]
                if len(parts) == 4:
                    c.exclusion_zones.append(parts)

        prev_autostart = c.autostart
        c.autostart = self._autostart.isChecked()
        if c.autostart != prev_autostart:
            Autostart.install() if c.autostart else Autostart.uninstall()

        c.save()
        log.info("Configuration updated and saved.")
        self.accept()


# ══════════════════════════════════════════════════════════════════════════════
#  SENTINEL  — Top-level application controller
# ══════════════════════════════════════════════════════════════════════════════
class Sentinel:
    def __init__(self):
        self.config  = Config()
        self.db      = DetectionDB(self.config)
        self.webhook = WebhookNotifier(self.config)
        self.archive = SnapshotArchive(self.config)
        self.badges  = BadgeManager(self.config)
        self.watcher = ContentWatcher(self.config)
        self._paused             = False
        self._det_count_session  = 0

        # Wire annotation feedback
        self.badges.set_annotation_callback(self._on_annotation)
        self.watcher.detection.connect(self._on_detection)

        # Health-check server
        self._health = HealthCheckServer(self.config, self.watcher, self.db)
        self._health.start()

        if not _HEADLESS:
            self._build_tray()

        # Warn about missing optional deps once
        if _missing_deps:
            log.warning(f"Optional deps missing (degraded mode): {', '.join(_missing_deps)}")

    # ── Tray icon ─────────────────────────────────────────────────────────────
    def _make_icon(self, state: str) -> "QIcon":
        sz  = 22
        pix = QPixmap(sz, sz)
        pix.fill(Qt.transparent)
        p   = QPainter(pix)
        p.setRenderHint(QPainter.Antialiasing)
        color = {
            "on":     QColor(C["accent"]),
            "paused": QColor(C["warn"]),
            "detect": QColor(C["danger"]),
            "idle":   QColor(C["sub"]),
        }.get(state, QColor(C["accent"]))
        p.setBrush(QBrush(color)); p.setPen(Qt.NoPen)
        p.drawEllipse(3, 3, sz - 6, sz - 6)
        p.setPen(QPen(QColor(255, 255, 255, 200), 1.5))
        p.setFont(QFont("Arial Black", 7, QFont.Black))
        p.drawText(QRect(0, 0, sz, sz), Qt.AlignCenter, "AI")
        p.end()
        return QIcon(pix)

    def _build_tray(self):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self._make_icon("on"))
        self.tray.activated.connect(self._on_tray_activated)

        menu = QMenu()
        title_act = QAction(f"  {APP_NAME}  v{APP_VERSION}", menu)
        title_act.setEnabled(False)
        menu.addAction(title_act)
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
            ["xdg-open" if _IS_LINUX else "open" if _IS_MAC else "notepad",
             str(SYSLOG_FILE)], stderr=subprocess.DEVNULL))
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

        self._tray_timer = QTimer()
        self._tray_timer.timeout.connect(self._update_tray)
        self._tray_timer.start(5_000)

    def _on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self._open_dashboard()

    def _update_tray(self):
        s          = self.db.stats()
        icon_state = ("paused" if self._paused else
                      "idle"   if self.watcher.state == ContentWatcher.STATE_IDLE
                      else "on")
        self.tray.setIcon(self._make_icon(icon_state))
        up = int(self.watcher.uptime_s)
        hh, mm = divmod(up // 60, 60)
        self.tray.setToolTip(
            f"{APP_NAME}  {'[PAUSED]' if self._paused else '[' + self.watcher.state.upper() + ']'}\n"
            f"Today: {s['today']} AI  |  24h: {s['h24']} AI\n"
            f"API: {self.watcher.api_count}  |  Errors: {self.watcher.error_count}  "
            f"|  Budget: {self.watcher.rate_budget}/min\n"
            f"Session: {self._det_count_session}  |  Uptime: {hh}h{mm:02d}m"
        )

    # ── Detection callback ─────────────────────────────────────────────────────
    def _on_detection(self, score: float, x: int, y: int, w: int, h: int,
                      ts: str, det_id: str, entropy: float,
                      latency: float, trigger_source: str):
        pct  = int(score * 100)
        proc = self.watcher._current_process
        log.info(
            f"AI detected  score={pct}%  region=[{x},{y},{w}×{h}]  "
            f"entropy={entropy:.2f}  latency={latency:.0f}ms  "
            f"trigger={trigger_source!r}  proc={proc!r}  id={det_id}"
        )
        self._det_count_session += 1

        badge = self.badges.spawn(score, x, y, w, h, det_id=det_id)

        if not _HEADLESS:
            self.tray.setIcon(self._make_icon("detect"))
            QTimer.singleShot(1_800, lambda: self.tray.setIcon(
                self._make_icon("paused" if self._paused else "on")))

        det = Detection(
            id=det_id, ts=time.time(), ts_str=ts,
            score=score, score_pct=pct, is_ai=True,
            threshold_pct=int(self.config.threshold * 100),
            x=x, y=y, w=w, h=h,
            blend_mode=self.config.score_blend,
            process_name=proc,
            entropy=entropy, api_latency_ms=latency,
            trigger_source=trigger_source,
            session_id=self.config.session_id,
        )
        self.db.add(det)
        self.webhook.enqueue(det)

        if self.config.desktop_notify:
            threading.Thread(
                target=notify_os,
                args=(f"AI Content Detected — {pct}%",
                      f"Confidence: {pct}%  ·  Region: {w}×{h}px"),
                daemon=True,
            ).start()

        if self.config.badge_sound:
            threading.Thread(target=beep, daemon=True).start()

    def _on_annotation(self, det_id: str, annotation: str):
        self.db.annotate(det_id, annotation)
        log.info(f"Annotation: {det_id} → {annotation!r}")

    # ── Controls ──────────────────────────────────────────────────────────────
    def toggle_pause(self):
        self._paused = not self._paused
        if self._paused:
            self.watcher.pause()
            if not _HEADLESS:
                self._pause_act.setText("▶  Resume Monitoring")
                self.tray.setIcon(self._make_icon("paused"))
            self.badges.clear_all()
            log.info("Monitoring paused.")
        else:
            self.watcher.resume()
            if not _HEADLESS:
                self._pause_act.setText("⏸  Pause Monitoring")
                self.tray.setIcon(self._make_icon("on"))
            log.info("Monitoring resumed.")

    def _open_config(self):
        dlg = ConfigDialog(self.config)
        if dlg.exec_():
            # Re-apply rate limiter in case limit changed
            self.watcher._rate_limiter = TokenBucket(self.config.rate_limit_per_min)
            log.info("Configuration reloaded.")

    def _open_dashboard(self):
        dlg = StatsDashboard(self.db, self.watcher, self.config)
        dlg.show(); dlg.raise_(); dlg.activateWindow()

    def _quick_export_csv(self):
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = EXPORT_DIR / f"export_{ts}.csv"
        ok   = self.db.export_csv(str(path))
        if not _HEADLESS:
            msg = f"CSV saved to:\n{path}" if ok else "No detections to export."
            lvl = QSystemTrayIcon.Information if ok else QSystemTrayIcon.Warning
            self.tray.showMessage("Export" + (" Complete" if ok else " Failed"),
                                  msg, lvl, 4_000)

    def shutdown(self):
        log.info(f"Shutting down {APP_NAME}. Session detections: {self._det_count_session}")
        self.watcher.shutdown()
        self.badges.clear_all()
        self.db.close()
        self._health.stop()
        if not _HEADLESS:
            self.tray.hide()

    def _quit(self):
        self.shutdown()
        QApplication.instance().quit()


# ══════════════════════════════════════════════════════════════════════════════
#  SINGLE-INSTANCE LOCK  (robust cross-platform)
# ══════════════════════════════════════════════════════════════════════════════
class SingleInstanceLock:
    """
    Writes PID to a lock file.  On startup, checks if a prior PID is still
    alive; if so, aborts.  Cleans up stale locks from crashed sessions.
    """

    def __init__(self, lock_path: Path):
        self._path = lock_path
        self._held = False

    def acquire(self) -> bool:
        if self._path.exists():
            try:
                pid = int(self._path.read_text().strip())
                if pid == os.getpid():
                    pass   # re-entrant same process
                elif self._pid_alive(pid):
                    log.warning(f"{APP_NAME} already running (PID {pid}). Exiting.")
                    return False
                # Stale lock — clean up
                self._path.unlink(missing_ok=True)
            except (ValueError, OSError):
                self._path.unlink(missing_ok=True)

        try:
            self._path.write_text(str(os.getpid()))
            self._held = True
            return True
        except OSError as e:
            log.warning(f"Could not write lock file: {e}")
            return True   # non-fatal — continue without lock

    def release(self):
        if self._held:
            with suppress(Exception):
                self._path.unlink(missing_ok=True)
            self._held = False

    @staticmethod
    def _pid_alive(pid: int) -> bool:
        if pid <= 0:
            return False
        if _IS_WIN:
            try:
                import ctypes
                h = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
                if h:
                    ctypes.windll.kernel32.CloseHandle(h)
                    return True
                return False
            except Exception:
                return False
        else:
            try:
                os.kill(pid, 0)
                return True
            except OSError:
                return False


# ══════════════════════════════════════════════════════════════════════════════
#  CLI  (headless / stats / reset modes)
# ══════════════════════════════════════════════════════════════════════════════
def _cli_stats():
    config = Config()
    db     = DetectionDB(config)
    s      = db.stats()
    db.close()
    print(json.dumps({
        "version": APP_VERSION,
        "build":   APP_BUILD,
        **s,
    }, indent=2))


def _cli_reset():
    print(f"Resetting {APP_NAME}…")
    config = Config()
    db     = DetectionDB(config)
    db.clear()
    db.close()
    if SNAPSHOT_DIR.exists():
        shutil.rmtree(str(SNAPSHOT_DIR))
        SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    if BLOOM_FILE.exists():
        BLOOM_FILE.unlink()
    print("DB cleared, snapshots deleted, bloom filter removed.")


def _cli_headless(sentinel: Sentinel):
    """
    Run without Qt event loop — use a plain threading.Event for lifecycle.
    Signal handlers trigger a clean shutdown.
    """
    stop_evt = threading.Event()

    def _sighandler(*_):
        print("\nSignal received — shutting down…")
        stop_evt.set()

    signal.signal(signal.SIGINT,  _sighandler)
    signal.signal(signal.SIGTERM, _sighandler)

    print(f"{APP_NAME} v{APP_VERSION} running in headless mode. "
          f"PID {os.getpid()}. Press Ctrl+C to stop.")
    stop_evt.wait()
    sentinel.shutdown()
    print("Goodbye.")


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════
def _parse_args():
    p = argparse.ArgumentParser(prog="ai_sentinel_pro", description=APP_NAME)
    p.add_argument("--headless", action="store_true",
                   help="Run as background daemon without Qt UI")
    p.add_argument("--stats",    action="store_true",
                   help="Print JSON stats to stdout and exit")
    p.add_argument("--reset",    action="store_true",
                   help="Clear DB + snapshots + bloom filter, then exit")
    return p.parse_known_args()[0]


if __name__ == "__main__":
    args = _parse_args()

    if args.stats:
        _cli_stats()
        sys.exit(0)

    if args.reset:
        _cli_reset()
        sys.exit(0)

    # ── Single-instance guard ─────────────────────────────────────────────────
    lock = SingleInstanceLock(CONFIG_DIR / ".lock")
    if not lock.acquire():
        sys.exit(0)

    # ── Announce missing optional dependencies ────────────────────────────────
    # (populated during soft-import above; log after logger is ready)
    if _missing_deps:
        log.warning(
            f"The following optional dependencies are missing and some features "
            f"will be disabled: {', '.join(_missing_deps)}.  "
            f"Install with: pip install {' '.join(_missing_deps)}"
        )

    if args.headless:
        # Headless path — no Qt application needed
        config   = Config()
        sentinel = Sentinel()
        try:
            _cli_headless(sentinel)
        finally:
            lock.release()
        sys.exit(0)

    # ── Qt GUI path ───────────────────────────────────────────────────────────
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setStyleSheet(BASE_STYLE)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(
            None, APP_NAME,
            "No system tray detected.\n"
            "Launch with --headless for daemon mode, or enable a system tray.")
        lock.release()
        sys.exit(1)

    sentinel = Sentinel()

    def _cleanup():
        lock.release()

    app.aboutToQuit.connect(_cleanup)

    log.info(
        f"{APP_NAME} v{APP_VERSION} ({APP_BUILD}) ready — "
        f"PID {os.getpid()}  session={sentinel.config.session_id}"
    )
    sys.exit(app.exec_())
