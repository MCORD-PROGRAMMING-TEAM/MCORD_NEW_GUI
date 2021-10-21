import sys
import os 
from cx_Freeze import  setup, Executable

files = ['resources/mcord_icon.ico']

target = Executable(
    script="app.py",
    base = "WIN32GUI",
    icon="resources/mcord_icon.ico"
)


setup(
    name='MCORD GUI',
    version="0.5",
    description = 'GUI for AFE Hubs',
    author = "MK",
    options = {'build.exe': {'include_files':files}},
    executables = [target]
)