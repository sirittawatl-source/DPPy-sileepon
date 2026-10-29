#!/usr/bin/env python3

def c8(family):
    cm9 = list(filter(lambda name : family[name] == "red", family.keys()))
    return cm9

cm9_family = {
    "florian" : "red",
    "marie" : "blond",
    "virginie" : "brunette",
    "david" : "red",
    "franck" : "red",
}

print (c8(cm9_family))
