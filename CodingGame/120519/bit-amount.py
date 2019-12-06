import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x = int(input())
    x = str(bin(x))[2:]
    print(len(x))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)