# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for KeyboardSounder (macOS + Windows).

- Windows: single-file KeyboardSounder.exe
- macOS: KeyboardSounder.app bundle
"""

import sys
from pathlib import Path

block_cipher = None
root = Path(SPECPATH)
sounds = root / "sounds"
icon_ico = root / "assets" / "app_icon.ico"

datas = [(str(sounds), "sounds")]
icon = str(icon_ico) if sys.platform.startswith("win") and icon_ico.exists() else None

a = Analysis(
    ["main.py"],
    pathex=[str(root)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

if sys.platform == "darwin":
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name="KeyboardSounder",
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=icon,
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name="KeyboardSounder",
    )
    app = BUNDLE(
        coll,
        name="KeyboardSounder.app",
        icon=None,
        bundle_identifier="com.joeyycho.keyboard-sounder",
        info_plist={
            "CFBundleName": "KeyboardSounder",
            "CFBundleDisplayName": "KeyboardSounder",
            "NSHighResolutionCapable": True,
        },
    )
else:
    # Windows (and Linux smoke builds): one-file executable
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name="KeyboardSounder",
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=icon,
    )
