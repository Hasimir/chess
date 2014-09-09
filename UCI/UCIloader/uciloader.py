#!/usr/bin/env python

# Run this in the directory with the Win32 UCI .exe or a parent
# directory of it.
#
# Command: uciloader[.py] <win32_uci_exe_filename>

from distutils.spawn import find_executable
import os
import os.path
import subprocess
import sys

name = sys.argv[1]
curdir = os.path.abspath(".")

winexec = find_executable("wine")
winepath = os.path.abspath(winexec)

def uciengine(name, curdir):
    for root, dirs, files in os.walk(curdir):
        if name in files:
            return os.path.join(root, name)

# For testing purposes:
#
#uciloader = subprocess.check_call("{0} {1}".format(winepath, uciengine))
#print("{0} {1}".format(winepath, uciengine(name, curdir)))
os.system("{0} {1}".format(winepath, uciengine(name, curdir)))

# This should load the win32 UCI engine with Wine:

#subprocess.call("{0} {1}".format(winepath, uciengine(name, curdir)))

