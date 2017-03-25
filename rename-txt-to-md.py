#! /usr/bin/env python

import glob, os

for fname in glob.glob('*txt*'):
    # Replace all occurrences of txt with md
    os.rename(fname, fname.replace('txt', 'md'))

