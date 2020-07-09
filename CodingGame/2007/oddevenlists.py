import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input().split()

oddList = []
evenList = []

for i in s:
    i = int(i)
    if i%2: oddList.append(i)
    else: evenList.append(i)

print(*sorted(set(oddList)), *sorted(set(evenList), reverse = True))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

