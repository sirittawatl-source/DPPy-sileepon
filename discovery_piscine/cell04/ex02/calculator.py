#!/usr/bin/env python3

fnum = float(input("Give me the first number : "))
snum = float(input("Give me the second number : "))

print("Thank you!")
print(f"{fnum:g} + {snum:g} = {fnum + snum:g}")
print(f"{fnum} - {snum} = {fnum - snum}")

if snum != 0:
    print(f"{fnum} / {snum} = {fnum / snum}")
else:
    print("Division by zero is not possible.")

print(f"{fnum} * {snum} = {fnum * snum}")