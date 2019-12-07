import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = []
for i in input().split():
    x = int(i)
    a.append(x)

a.sort()
print(sum(a)/len(a) if sum(a)%len(a) else sum(a)//len(a))