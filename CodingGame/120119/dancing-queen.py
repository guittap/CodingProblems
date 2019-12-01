import sys
import math

a = {"boom": 1, "ts": -1}
b = {"bing": 1, "ding": -1}
x = 0
y = 0

s = input().split()
for i in s:
    if i in a:
        x+=a[i]
        if x<0:
            x=0
        elif x>=31:
            x=30
    else:
        y+=b[i]
        if y<0:
            y=0
        elif y>=11:
            y=10
print(x,y)