#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# AI Sentinel — Nuitka Build Script
# Produces a standalone binary in dist/
#
# Requirements:
#   pip install nuitka ordered-set zstandard
#   apt install patchelf ccache (Linux)
#
# Usage:
#   bash scripts/build_nuitka.sh [--onefile]
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
MAIN="$REPO_DIR/ai_sentinel.py"
OUT="$REPO_DIR/dist"
ONEFILE=0

if [[ "${1:-}" == "--onefile" ]]; then
    ONEFILE=1
fi

mkdir -p "$OUT"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  AI Sentinel — Nuitka Build"
echo "  Mode: $([ $ONEFILE -eq 1 ] && echo 'onefile' || echo 'standalone')"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

COMMON_FLAGS=(
    --standalone
    --enable-plugin=pyqt5
    --include-package=PIL
    --include-package=mss
    --include-package=requests
    --include-package=cryptography
    --assume-yes-for-downloads
    --show-progress
    --show-memory
    --output-dir="$OUT"
    --output-filename=ai_sentinel
)

if [[ $ONEFILE -eq 1 ]]; then
    COMMON_FLAGS+=(--onefile)
fi

# Use ccache if available
if command -v ccache &>/dev/null; then
    COMMON_FLAGS+=(--clang --jobs="$(nproc)")
fi

python3 -m nuitka "${COMMON_FLAGS[@]}" "$MAIN"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Build complete → $OUT/"
ls -lh "$OUT/"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
