import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a = 1
m = 1
mc = s[0]
l = ""
for i in s:
    if l==i:
        a+=1
        if a>m:
            m=a
            mc = i
            
    else:
        a=1
    l=i

print(mc,m)