import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    t = input().split(":")
    l = []
    for i in t:
        l.append(int(i))
    if l[2]>59:
        a = l[2]//60
        b = a*60
        l[1] += a
        l[2] -= b
    if l[1]>59:
        a = l[1]//60
        b = a*60
        l[0] += a
        l[1] -= b
    print(l[0] if len(str(l[0]))>1 else "0"+str(l[0]),l[1] if len(str(l[1]))==2 else "0"+str(l[1]),l[2] if len(str(l[2]))==2 else "0"+str(l[2]),sep=":")