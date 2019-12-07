import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
a = set()
for i in w:
    a.add(i.upper())


print(len(a))