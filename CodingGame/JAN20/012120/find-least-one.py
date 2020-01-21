import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dictionary = set()

n = int(input())
for i in range(n):
    start, end = [int(j) for j in input().split()]
    for j in range(start,end):
        dictionary.add(j)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(len(dictionary))