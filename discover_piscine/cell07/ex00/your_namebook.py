#!/usr/bin/env python3

def karr(persons):
    d8=[]
    for first_name, last_name in persons.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        name.append(full_name)
    return d8

persons = {
    "jean" : "valjean",
    "grace" : "hopper",
    "xavier" : "niel",
    "fifi" : "brindacier"
}

print(karr(persons))

