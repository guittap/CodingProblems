import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()
l = list()
for i in n:
    l.append(int(i))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
org = list(l)
l.sort()
inc = list(l)
l.sort(reverse = True)
dec = list(l)

print("false" if org == inc or org == dec else "true")