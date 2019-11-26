import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
w = int(input())
a = []
q=""
for i in input().split():
    s = int(i)
    a.append(s)
if w<l:
    for i in range(l-w+1):
        sum = 0
        for j in range(w):
            sum+=a[i+j]
        q+=str(sum/w)+" "
    print(q[:-1])
else:
    sum=0
    for i in range(l):
        sum+=a[i]
    print(round(sum/l,1))