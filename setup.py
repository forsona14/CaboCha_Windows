#!/usr/bin/env python

from distutils.core import setup,Extension,os
import string

def cmd1(str):
    return os.popen(str).readlines()[0][:-1]

def cmd2(str):
    return string.split (cmd1(str))

setup(name = "cabocha-python",
    version = "0.69",
    py_modules=["CaboCha"],
    ext_modules = [
        Extension("_CaboCha",
            ["CaboCha_wrap.cxx",],
            include_dirs=[r"C:\Program Files (x86)\CaboCha\sdk"],
            library_dirs=[r"C:\Program Files (x86)\CaboCha\sdk"],
            libraries=['libcabocha'])
])
