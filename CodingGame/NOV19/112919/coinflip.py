import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, q = [int(i) for i in input().split()]
a = dict()
for i in range(n):
    a[i]=0
    
for i in range(q):
    l, r = [int(j) for j in input().split()]
    for x in range(l,r+1,1):
        if a[x]==0:
            a[x]=1
        else:
            a[x]=0

s=0
for i in range(n):
    if a[i] ==1:
        s+=1

print(s)