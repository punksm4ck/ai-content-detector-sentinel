# Changelog

All notable changes to AI Sentinel are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased] — AI Sentinel Pro v3.0.0

### Added
- SQLite-backed detection log replacing flat JSON (indexed queries, fast aggregation)
- 5 badge styles: Circle, Shield, Ribbon, Banner, Hexagonal
- Bloom filter dedup pre-screening for hash acceleration
- Shannon entropy pre-filter to skip low-complexity screen regions
- Dual-trigger scanning: motion-based + interval full-frame scan
- 4 score blending modes: Average, Maximum, Weighted Average, Ensemble Vote
- Per-monitor exclusion zones (define screen rects to never analyze)
- Real-time detection density heatmap (color-coded grid overlay in dashboard)
- Score sparkline (last 120 detections trend) in dashboard
- Webhook alerts: Slack, MS Teams, custom HTTP POST
- Screenshot snapshot archive with configurable retention
- Encrypted credential storage (Fernet, machine-derived key)
- Cost tracker tab (Sightengine API spend estimation)
- 7-tab configuration dialog with scrollable form layout
- Snapshot browser tab in dashboard
- PyQt6 migration (build target)
- `Detection` dataclass with UUID per record, entropy + latency fields
- Configurable worker concurrency (was hardcoded)
- Windows Toast notifications via PowerShell (no third-party dep)

---

## [2.0.0] — 2026-04-08

### Added
- Complete rewrite from v1 proof-of-concept
- Multi-tab ConfigDialog (API, Detection, Badge, Alerts, System)
- StatsDashboard with stat cards, log table, hourly timeline chart
- Burst frame analysis with configurable count and gap
- Exponential backoff retry on API failures
- Autostart: Linux XDG `.desktop`, macOS LaunchAgent, Windows Registry
- Auto-pause on idle (configurable timeout)
- Multi-monitor support with offset-aware badge positioning
- CSV export from dashboard
- `DetectionLog` class with thread-safe JSON persistence and FIFO pruning
- `BadgeManager` with max overlay cap and culling
- `ScreenMonitor` with dedup dict, cleanup timer, worker queue cap
- Sound alert (cross-platform beep)
- OS desktop notifications (osascript / notify-send / Win32 MessageBox)
- Perceptual dHash deduplication with configurable TTL

### Changed
- Badge fade animation now uses `QPropertyAnimation` on `QGraphicsOpacityEffect`
- Tray icon renders programmatically (no external icon file required)
- Config validation with user-facing error messages

---

## [1.0.0] — 2026-03-15

### Added
- Initial proof-of-concept
- Basic Sightengine API integration
- Single floating badge widget
- System tray icon
- Single-file JSON config
