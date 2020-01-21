import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = input().split()
li = []
se = set(l)

for i in se:
    if l.count(i) % 2: print(i); exit()
   

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
