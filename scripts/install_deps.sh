#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# AI Sentinel — System Dependency Installer
# Handles Debian/Ubuntu (apt) and Arch (pacman)
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

echo "Detecting system..."

if command -v apt &>/dev/null; then
    echo "→ Debian/Ubuntu detected"
    sudo apt update
    sudo apt install -y \
        python3 python3-pip python3-venv \
        python3-pyqt5 python3-pyqt5.qtsvg \
        libxcb-cursor0 libxcb-icccm4 libxcb-xinerama0 \
        libnotify-bin libdbus-1-3 \
        ccache patchelf
elif command -v pacman &>/dev/null; then
    echo "→ Arch/AnduinOS detected"
    sudo pacman -Sy --needed \
        python python-pip python-pyqt5 \
        python-pillow python-requests \
        ccache patchelf libnotify
else
    echo "⚠  Unknown package manager. Install manually:"
    echo "   PyQt5, Pillow, mss, requests, cryptography"
fi

echo ""
echo "Installing Python packages..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo ""
echo "✓ Dependencies installed."
