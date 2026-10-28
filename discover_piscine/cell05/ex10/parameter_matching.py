#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    ans = input("What was the parameter? ")
    if ans == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")