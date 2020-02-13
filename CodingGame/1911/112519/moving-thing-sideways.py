import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, h = [int(i) for i in input().split()]
a=[]
for i in range(h):
    a.append(input())

for i in range(l):
    for j in range(h-1,-1,-1):
        print(a[j][i],end="")
    print("")