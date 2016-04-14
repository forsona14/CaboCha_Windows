# CaboCha_Windows
How to install Cabocha on Windows and use in Python


1.  Download MeCab-0.996.exe and install (Use UTF-8) 

    See http://taku910.github.io/mecab/
    
2.  Download CaboCha-0.69.exe and install (Use UTF-8)

    See https://taku910.github.io/cabocha/
    
3.  Add ...\MeCab\bin and ...\CaboCha\bin to PATH
4.  Install Cabocha in python

    Download Cabocha-0.69.tar.bz2, cd ...\cabocha-0.69\python, run: python setup.py install
    
    For cabocha-config issues ('list index out of range') , see http://qiita.com/mima_ita/items/161cd869648edb30627b . Change the version 0.68 -> 0.69
    `
    #!/usr/bin/env python

    from distutils.core import setup,Extension,os
    import string
    
    def cmd1(str):
        return os.popen(str).readlines()[0][:-1]
    
    def cmd2(str):
        return string.split (cmd1(str))
    
    setup(name = "cabocha-python",
        version = "0.68",
        py_modules=["CaboCha"],
        ext_modules = [
            Extension("_CaboCha",
                ["CaboCha_wrap.cxx",],
                include_dirs=[r"C:\Program Files (x86)\CaboCha\sdk"],
                library_dirs=[r"C:\Program Files (x86)\CaboCha\sdk"],
                libraries=['libcabocha'])
    ])
    `
    
    For VC2008 issue('Unable to find vcvarsall.bat'), run: SET VS90COMNTOOLS=%VS140COMNTOOLS% .  You can runSET to see current VSCOMNTOOLS path.
