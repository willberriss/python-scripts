#! /usr/bin/env python

from glob import glob
from os import rename

for fname in glob('*txt*'):
    # Replace all occurrences of txt with md
    rename(fname, fname.replace('txt', 'md'))

