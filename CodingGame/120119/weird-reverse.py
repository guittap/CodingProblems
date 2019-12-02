import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# if len(s)%2==0:
a = ""
b = ""
for i in range(len(s)//2+1):
    if i*2<len(s):
        a+=s[i*2]
    if i*2+1 < len(s):
        b+=s[i*2+1]
print(b[::-1],a,sep="")