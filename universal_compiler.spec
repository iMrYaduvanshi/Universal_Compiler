# -*- mode: python ; coding: utf-8 -*-

import os

icon_path = os.path.join("assets", "icon.ico")
splash_path = os.path.join("assets", "splash.png")

block_cipher = None

a = Analysis(
    ['gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config/compilers.json', 'config'),
        ('assets/splash.png', 'assets'),
        ('assets/icon.ico', 'assets'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

# ---- Proper Splash Initialization ----
splash = Splash(
    splash_path,
    binaries=a.binaries,
    datas=a.datas,
    timeout=2500,   # Auto-close after 2.5 sec
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    splash,                     # MUST be right before name=
    name='UniversalCompiler',
    icon=icon_path,
    debug=False,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    a.zipfiles,
    a.scripts,
    name='UniversalCompiler'
)
