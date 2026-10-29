#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    while len(string) < 8:
        string += 'Z'
    print(string)

if len(sys.argv) < 2:
    print("none")
else:
    for m8 in sys.argv[1:]:
        if len (m8) > 8:
            shrink(m8)
        elif len (m8) < 8:
            enlarge(m8)
        else:
            print(m8)
