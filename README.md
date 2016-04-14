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
 
    For VC2008 issue('Unable to find vcvarsall.bat'), run: SET VS90COMNTOOLS=%VS140COMNTOOLS% (or just set system environment.  You can runSET to see current VSCOMNTOOLS path. (MAKE SURE 'Common Tools for Visual C++' are is installed in Visual Studio.)
    
    OR
    
    Donwload Microsoft Visual C++ Compiler for Python 2.7: https://www.microsoft.com/en-us/download/details.aspx?id=44266
    and hardcode Python27\Lib\distutils\msvc9compiler.py: http://www.cnblogs.com/lazyboy/p/4017567.html
