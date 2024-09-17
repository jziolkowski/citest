# -*- mode: python ; coding: utf-8 -*-

# import setuptools_scm
import sys

# _version = setuptools_scm.get_version(local_scheme='no-local-version')

# os.name='nt'
# sys.platform='win32'
# platform.mac_ver()=('', ('', '', ''), '')
# platform.system()='Windows'
# platform.architecture()=('32bit', 'WindowsPE')

# os.name='nt'
# sys.platform='win32'
# platform.mac_ver()=('', ('', '', ''), '')
# platform.system()='Windows'
# platform.architecture()=('64bit', 'WindowsPE')

# os.name='posix'
# sys.platform='darwin'
# platform.mac_ver()=('13.6.9', ('', '', ''), 'x86_64')
# platform.system()='Darwin'
# platform.architecture()=('64bit', '')

_suffix = f"_x64" if sys.maxsize > 2**32 else ""
filename = f"tdmgr_{_suffix}"

block_cipher = None

a = Analysis(['app.py'],
             binaries=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=filename,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)