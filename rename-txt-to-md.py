#! /usr/bin/env python3

import glob, os

for fname in glob.glob('*txt*'):
    # e.g. replace fred.txt.bak with fred.md.bak
    os.rename(fname, fname.replace('txt', 'md'))

