#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os

# activate virutalenv
activate_this_file = "/home/b/boocomp/.local/bin/activate_this.py"
execfile(activate_this_file, dict(__file__=activate_this_file))

# Add a custom Python path.
sys.path.insert(0, "/home/b/boocomp/f1new/public_html")

# Switch to the directory of your project. (Optional.)
os.chdir("/home/b/boocomp/f1new/public_html/f1new")

# WSGI expects application variable
from agart import app as application

# Not nessesarry
if __name__ == '__main__':
   application.run()