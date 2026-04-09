<div align="center">

```
 █████╗ ██╗    ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗
██╔══██╗██║    ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║
███████║██║    ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║
██╔══██║██║    ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║
██║  ██║██║    ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗
╚═╝  ╚═╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
```

**Enterprise Background AI Content Detector**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://python.org)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15%2B-green?style=flat-square)](https://pypi.org/project/PyQt5/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=flat-square)](https://github.com/tsann/ai-sentinel)
[![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)](LICENSE)
[![PUNKS](https://img.shields.io/badge/PUNKS-Ecosystem-ff2060?style=flat-square)](https://github.com/tsann)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange?style=flat-square)](CHANGELOG.md)

*Invisible. Always watching. Zero UI footprint.*

</div>

---

## Overview

**AI Sentinel** is a zero-UI, full-screen background monitor that detects AI-generated images and video frames on your screen in real time — and stamps a floating, click-through watermark badge directly onto them. No window. No popups. Lives entirely in the system tray.

It hooks into [Sightengine's GenAI API](https://sightengine.com/detect-ai-generated-content) for detection, uses perceptual hashing to eliminate duplicate analysis, and supports multi-monitor setups, autostart, desktop notifications, and persistent JSON/CSV audit logs.

Part of the **PUNKS / OSIRIS** ecosystem.

---

## Features

| Feature | Details |
|---|---|
| 🔍 **Real-time screen monitoring** | Motion-diff detection with configurable region extraction |
| 🏷 **Floating AI badge** | Click-through, frameless overlay stamped at detected region |
| 🔁 **Burst frame analysis** | Multiple frames averaged to reduce false positives |
| ♻️ **Perceptual hash deduplication** | Skips re-analyzing identical content (configurable TTL) |
| 🖥 **Multi-monitor support** | Per-monitor targeting with offset-aware badge placement |
| 📋 **Persistent audit log** | JSON + CSV detection history with stats |
| 🔔 **Desktop notifications** | OS-native alerts on detection |
| 🔊 **Sound alerts** | Optional system beep on detection |
| ⚙️ **Full configuration UI** | 5-tab config dialog via tray icon |
| 📊 **Detection dashboard** | Stats, log table, hourly timeline |
| 🚀 **Autostart** | Self-installs to OS startup (XDG / LaunchAgent / Registry) |
| 🌐 **Cross-platform** | Linux (KDE/GNOME/X11), macOS, Windows 11 |

---

## Screenshots

> *AI Sentinel runs invisibly — no main window exists. All interaction is through the tray icon.*

| Tray Menu | Config Dialog | Detection Dashboard |
|---|---|---|
| *(right-click tray icon)* | *(⚙ Configuration…)* | *(📊 View Dashboard…)* |

---

## Requirements

- Python **3.10+**
- A free [Sightengine](https://sightengine.com/signup) account (500 free API calls/month)
- A running X11 or Wayland display (Linux), or standard desktop (macOS/Windows)

### System Dependencies (Linux)

```bash
sudo apt install python3-pyqt5 python3-pyqt5.qtsvg libxcb-cursor0 notify-send
```

---

## Installation

### 1. Clone

```bash
git clone https://github.com/punksm4ck/ai-content-detector-sentinel.git
cd ai-sentinel
```

### 2. Create virtualenv and install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure

Launch the app — it will appear in your system tray. Right-click → **⚙ Configuration** → enter your Sightengine API credentials.

Or pre-populate `~/.config/ai_sentinel/config.json` (see [Configuration Reference](#configuration-reference)).

### 4. Run

```bash
python3 ai_sentinel.py
```

Or use the provided launch script:

```bash
bash scripts/launch.sh
```

---

## Build (Nuitka — Native Binary)

AI Sentinel supports compilation to a standalone native binary via [Nuitka](https://nuitka.net).

```bash
bash scripts/build_nuitka.sh
```

Output will be placed in `dist/ai_sentinel` (Linux/macOS) or `dist/ai_sentinel.exe` (Windows).

See [docs/BUILD.md](docs/BUILD.md) for full build instructions and flags.

---

## Configuration Reference

Config is stored at `~/.config/ai_sentinel/config.json`.

| Key | Default | Description |
|---|---|---|
| `api_user` | `""` | Sightengine API user |
| `api_secret` | `""` | Sightengine API secret |
| `threshold` | `0.85` | AI confidence threshold (0.0–1.0) |
| `interval_ms` | `4000` | Screen poll interval in ms |
| `monitor_index` | `0` | Target monitor (0 = all) |
| `burst_frames` | `3` | Frames per API burst |
| `burst_gap_ms` | `200` | Gap between burst frames |
| `motion_min_px` | `120` | Minimum changed region size (px) |
| `dedup_enabled` | `true` | Skip re-analyzing same content |
| `dedup_ttl` | `120` | Seconds before re-analyzing same hash |
| `badge_size` | `48` | Badge diameter in pixels |
| `badge_opacity` | `0.88` | Badge opacity (0.0–1.0) |
| `sound_alert` | `false` | System beep on detection |
| `desktop_notify` | `true` | OS desktop notification |
| `log_enabled` | `true` | Write detection log |
| `max_log` | `1000` | Max log entries (FIFO) |
| `autostart` | `false` | Launch on OS startup |
| `auto_pause_idle_s` | `0` | Pause after N seconds idle (0 = off) |
| `retry_max` | `3` | API retry attempts |
| `retry_backoff_ms` | `600` | Base backoff between retries |

---

## File Structure

```
ai-sentinel/
├── ai_sentinel.py              # Main application
├── requirements.txt            # Python dependencies
├── requirements-dev.txt        # Dev/build dependencies
├── setup.py                    # Package setup
├── pyproject.toml              # Build system config
├── CHANGELOG.md                # Version history
├── LICENSE                     # MIT License
├── .gitignore
├── scripts/
│   ├── launch.sh               # Launch wrapper
│   ├── build_nuitka.sh         # Nuitka build script
│   └── install_deps.sh         # System dependency installer
├── docs/
│   ├── BUILD.md                # Build documentation
│   ├── CONFIGURATION.md        # Full config reference
│   └── SIGHTENGINE.md          # API setup guide
├── assets/
│   └── icon.svg                # App icon source
└── .github/
    ├── workflows/
    │   ├── lint.yml            # Ruff + mypy CI
    │   └── build.yml           # Nuitka build CI
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        └── feature_request.md
```

---

## Logs & Data

| Path | Contents |
|---|---|
| `~/.config/ai_sentinel/config.json` | User configuration |
| `~/.config/ai_sentinel/detections.json` | Detection log (JSON) |
| `~/.config/ai_sentinel/detections.csv` | Detection log (CSV) |
| `~/.config/ai_sentinel/sentinel.log` | System/debug log |

---

## Roadmap

- [x] AI Sentinel Pro v3.0 — SQLite log, 5 badge styles, heatmap, webhook alerts, Bloom filter dedup, encrypted credential store
- [x] AI Sentinel Pro v4.0 — event-driven architecture, OS focus hooks, accessibility tree media detection, zero CPU at idle
- [ ] PyQt6 migration
- [ ] Wayland native support
- [ ] `--onefile` Nuitka distribution
- [ ] GitHub Actions automated release builds

---

## Related Projects

| Repo | Description |
|---|---|
| [ai-content-detector-sentinel-diag-suite](https://github.com/punksm4ck/ai-content-detector-sentinel-diag-suite) | Companion diagnostic suite — live motion emulator, system health reporter, batch scanner |

---

## Contributing

Pull requests welcome. Please open an issue first for significant changes.

```bash
pip install -r requirements-dev.txt
ruff check .
mypy ai_sentinel.py
```

---

## License

MIT © [tsann / PUNKS Ecosystem](https://github.com/tsann)

---

<div align="center">
<sub>Built under the OSIRIS / PUNKS ecosystem · Osiris-KubuntuCB</sub>
</div>
