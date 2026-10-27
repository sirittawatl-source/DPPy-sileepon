#!/usr/bin/env python3

import sys
i=0
j=0

while len(sys.argv) !=1:
    print("none")
    sys.exit(0)

    while i <= 10:
        print("Table de " + str(i) + ":", end ="")
        j=0
        while j <= 10:
            print (i*j, end ="" if j < 10 else "\n")
            j += 1
        i +=1 