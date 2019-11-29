import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
a = dict()
i = input()
for x in i:
    if x in a:
        a[x] +=1
    else:
        a[x]=1


for i in sorted(a):
    print(a[i],i,sep="",end="")