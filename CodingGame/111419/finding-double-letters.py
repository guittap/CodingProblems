import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input().split()
a,b = 0,0
for i in s:
    for j in range(len(i)-1):
        if i[j].upper() == i[j+1].upper():
            b=1
    if b==1:
        a+=1

print(a)