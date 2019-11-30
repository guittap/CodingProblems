import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
b=""
n = int(input())
for i in range(n):
    b=""
    a = dict()
    s = input()
    for i in s:
        if i.isalpha():
            if i in a:
                a[i]=1
            else:
                a[i]=0
    for i in a:
        if a[i]>0:
            b+=i
    print(b if len(b)>0 else "NONE",sep="")