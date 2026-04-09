#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# AI Sentinel — Launch Script
# Activates venv if present, then runs the app.
# Usage: bash scripts/launch.sh [--debug]
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
VENV="$REPO_DIR/.venv"
MAIN="$REPO_DIR/ai_sentinel.py"

# Activate venv if it exists
if [[ -f "$VENV/bin/activate" ]]; then
    source "$VENV/bin/activate"
fi

# Pass --debug flag through to Python if requested
if [[ "${1:-}" == "--debug" ]]; then
    exec python3 "$MAIN" --debug
else
    exec python3 "$MAIN"
fi
