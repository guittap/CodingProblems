import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = 0

while n!=1:
    if n%2 == 0:
        n//=2
    else:
        n =3*n+1
    c+=1

print(c)