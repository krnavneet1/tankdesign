# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:56:08 2019

@author: NaVnEeT
"""

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("TankDesign.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Area",
    options = options,
    version = "1.0",
    description = 'triangle',
    executables = executables
)