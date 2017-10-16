# -*- mode: python -*-

block_cipher = None


a = Analysis(['electrum'],
             pathex=['C:\\Users\\cmandracchia\\Desktop\\projects\\electrum'],
             binaries=[],
             datas=[],
             hiddenimports=['electrum_gui', 'electrum_gui.qt'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='electrum',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='icons\\electrum.ico')
