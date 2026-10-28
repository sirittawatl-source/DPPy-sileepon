#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    for a in sys.argv[1:]:
        print(a.lower())
else:
    print("none")
