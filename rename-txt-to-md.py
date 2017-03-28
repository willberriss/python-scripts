#! /usr/bin/env python3

import glob
import os

# e.g. replace fred.txt.bak with fred.md.bak
for filename in glob.glob('*txt*'):
    os.rename(filename, filename.replace('txt', 'md'))

