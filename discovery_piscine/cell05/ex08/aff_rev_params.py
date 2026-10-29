#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("none")
else:
    for t8 in reversed(sys.argv[1:]):
        print(t8)
