#!/usr/bin/env python

import pickle
import sys

output = pickle.load(open('banner.p', 'r'))

for r in output:
    for c in r:
        sys.stdout.write(c[0]*c[1])
print("\n")


