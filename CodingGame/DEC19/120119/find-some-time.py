import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

c, s = input().split()
a=c.split(":")
b=s.split(":")

x=int(b[1])-int(a[1])
y=int(b[0])-int(a[0])
if x<0:
    x+=60
    y-=1

print(y,x if len(str(x)) == 2 else "0"+str(x),sep=":")