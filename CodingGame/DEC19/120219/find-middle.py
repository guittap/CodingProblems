import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x, y, z = [int(j) for j in input().split()]
    l = [x,y,z]
    l.sort()
    print(l[1])