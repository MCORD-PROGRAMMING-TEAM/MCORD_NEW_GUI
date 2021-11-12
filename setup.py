import sys
import os 
from cx_Freeze import  setup, Executable



target = Executable(
    script="app.py",
    base = "WIN32GUI",
    icon="resources/mcord_icon.ico"
)

options = {
    'build_exe': {
        'include_files':[
           'resources/mcord_icon.ico' 
        ],
    'includes': [
        'importlib-metadata', 'notify2', 'plyer', 'pyserial', 'PySide6', 'shiboken6' , 'zipp'
    ],
        
    }
}


setup(
    name='MCORD GUI',
    version="0.5",
    description = 'GUI for AFE Hubs',
    author = "MK",
    options = {'build.exe': options},
    executables = [target]
)