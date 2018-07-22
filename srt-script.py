#!c:\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pysrt==1.1.1','console_scripts','srt'
__requires__ = 'pysrt==1.1.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pysrt==1.1.1', 'console_scripts', 'srt')()
    )
