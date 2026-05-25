#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════════════════════
#  AI Sentinel — GitHub Repo Init & Push
#  Run this once from Konsole on Osiris-KubuntuCB.
#  Prerequisites: git installed, GitHub SSH key configured (or use HTTPS token)
# ══════════════════════════════════════════════════════════════════════════════

set -euo pipefail

# ── CONFIG — edit these before running ───────────────────────────────────────
GITHUB_USER="tsann"
REPO_NAME="ai-sentinel"
REPO_DESC="Enterprise background AI content detector with zero-UI floating badge overlay"
BRANCH="main"
# ─────────────────────────────────────────────────────────────────────────────

REPO_DIR="/home/tsann/Scripts/ai-sentinel"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  AI Sentinel — GitHub Push"
echo "  Target: github.com/$GITHUB_USER/$REPO_NAME"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. Create repo dir and copy all files into place
mkdir -p "$REPO_DIR"/{scripts,assets,.github/workflows,.github/ISSUE_TEMPLATE,docs}

# Copy files (adjust source paths to wherever Claude's output landed)
# If you downloaded from Claude's output panel, files are at ~/Downloads/ai-sentinel/
# or copy directly from the Scripts folder if you've already placed them.

# 2. Init git
cd "$REPO_DIR"
git init
git checkout -b "$BRANCH"

# 3. Stage everything
git add .

# 4. Initial commit
git commit -m "feat: initial release — AI Sentinel v2.0.0

Enterprise background AI content detector.

- Zero-UI system tray app with floating click-through badge overlay
- Sightengine genai API integration with burst analysis + exponential backoff
- Perceptual hash deduplication (dHash, configurable TTL)
- Multi-monitor support with offset-aware badge placement
- Motion-diff screen scanning with configurable region extraction
- Persistent JSON + CSV audit log with stats dashboard
- 5-tab configuration dialog (API, Detection, Badge, Alerts, System)
- Hourly timeline chart in detection dashboard
- Cross-platform autostart: XDG desktop / LaunchAgent / Registry
- OS notifications: notify-send / osascript / Win32
- Nuitka build scripts for standalone native binary
- GitHub Actions CI: ruff lint + mypy + Nuitka build on tag

Part of the PUNKS / OSIRIS ecosystem.
Built on Osiris-KubuntuCB."

# 5. Create GitHub repo via CLI (requires gh installed: sudo apt install gh)
#    Authenticate first if needed: gh auth login
gh repo create "$GITHUB_USER/$REPO_NAME" \
    --public \
    --description "$REPO_DESC" \
    --source=. \
    --remote=origin \
    --push

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✓ Pushed to github.com/$GITHUB_USER/$REPO_NAME"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
