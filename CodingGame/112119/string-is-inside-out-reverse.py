import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
c=""
for i in range(len(s)//2):
    c += s[i] + s[len(s)-i-1]
    if len(s)%2==1 and i==len(s)//2-1:
        c += s[i+1]

print(c+c[::-1])