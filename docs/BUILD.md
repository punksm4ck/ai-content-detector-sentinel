# Building AI Sentinel

## Quick Build (Nuitka Standalone)

```bash
bash scripts/build_nuitka.sh
```

Output: `dist/ai_sentinel.dist/ai_sentinel`

## Single-File Binary

```bash
bash scripts/build_nuitka.sh --onefile
```

Output: `dist/ai_sentinel` (single executable, extracts on first run)

## Manual Nuitka Flags

```bash
python3 -m nuitka \
    --standalone \
    --enable-plugin=pyqt5 \
    --include-package=PIL \
    --include-package=mss \
    --include-package=requests \
    --include-package=cryptography \
    --assume-yes-for-downloads \
    --output-dir=dist \
    --output-filename=ai_sentinel \
    ai_sentinel.py
```

## System Prerequisites (Linux)

```bash
sudo apt install ccache patchelf libxcb-cursor0
pip install nuitka ordered-set zstandard
```

## Notes

- The `.build/` directory (220MB+) is Nuitka's intermediate C source cache — safe to delete after a successful build, regenerated on next build.
- The `.dist/` directory is the final output — contains the binary and all shared libraries needed to run without Python installed.
- Build time: ~8–15 minutes on first run (all C compilation). Subsequent builds with ccache are significantly faster.
- Secure Boot (MOK): If running on a system with Secure Boot and custom kernel modules (e.g. MT7902 driver), the Nuitka binary itself does not require signing — only kernel modules do.

## Known Issues

- **PyQt5 + Nuitka**: Always use `--enable-plugin=pyqt5`. Without it, Qt platform plugins will not be included and the app will fail to start.
- **`mss` on Wayland**: mss requires XWayland. Set `QT_QPA_PLATFORM=xcb` before running if on a pure Wayland session.
