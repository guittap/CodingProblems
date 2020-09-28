import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = [0,0,0,0,0,0,0]

for i in input().split():
    for j in i:
        a[6-int(j)]=1

    c=""
    for b in a:
        c+=str(b)
    print(chr(int(c,2)),end="")
    a = [0,0,0,0,0,0,0]