#!/usr/bin/env python

# disk_usage.py -- Calculates the file sizes of each file under the
# starting directory

import os
from os.path import join, getsize

for root, dirs, filenames in os.walk("."):
    print root, "consumes",
    print sum(getsize(join(root, name)) for name in filenames),
    print "bytes in", len(filenames), "non-directory files"
    if '.git' in dirs:
        dirs.remove('.git')  # don't visit git directories