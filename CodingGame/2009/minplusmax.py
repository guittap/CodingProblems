import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
list = []
for i in input().split():
    list.append(int(i))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(max(list)+min(list))