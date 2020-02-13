import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, g = [int(i) for i in input().split()]
m = int(input())
listOfKids = []
for i in range(n):
    listOfKids.append(int(input()))

listOfKids.sort()

print(1 if m >= listOfKids[n-g] or g > n else 0)