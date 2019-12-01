import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

e,a = input().split("=")
if '+' in e:
    b,c=e.split("+")
    a=int(a)-int(c)
    
else:
    b,c=e.split("-")
    a=int(a)+int(c)

d=b.split("N")
if d[0]!='':
    a/=int(d[0])

print(round(a))