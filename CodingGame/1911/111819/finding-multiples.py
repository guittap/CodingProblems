import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a,b = 1,n
c,d = 1,n

for i in range(math.ceil(n**(1/2))):
    if n%(i+1) == 0:
        a = i+1
        b = n//a
        if b-a < d-c:
            c=a
            d=b

if d < c:
    print(d,c,sep="*")

else:
    print(c,d,sep="*")