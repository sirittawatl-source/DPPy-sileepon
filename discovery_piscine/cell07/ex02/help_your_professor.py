#!/usr/bin/env python3

def st(students):
    return sum(students.values()) / len(students)

class_3B = {
    "marine" : 18,
    "jean" : 15,
    "coline" : 8,
    "luc" : 9
}

class_3C = {
    "quentin" : 17,
    "julie" : 15,
    "marc" : 8,
    "stephanie" : 13
}

print (f"Average for class 3B : {st(class_3B)}.")
print (f"Average for class 3C : {st(class_3C)},")
