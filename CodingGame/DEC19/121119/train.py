import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
listofvals = []
n = int(input())  # The numbers of paths the train can take
for i in range(n):
    # q: The number of persons on the path
    # v: The individual value of each person on the path
    q, v = [int(j) for j in input().split()]
    listofvals.append(q*v)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(listofvals.index(min(listofvals))+1)