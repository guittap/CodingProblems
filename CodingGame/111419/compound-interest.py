import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, i, m = [int(i) for i in input().split()]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for x in range(m):
    n = n * (1 + (i * .01))

print(int(n))