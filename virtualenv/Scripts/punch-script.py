#!C:\Users\maddu\Dropbox\programming\git\pixella\virtualenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'punch.py==1.5.0','console_scripts','punch'
__requires__ = 'punch.py==1.5.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('punch.py==1.5.0', 'console_scripts', 'punch')()
    )
