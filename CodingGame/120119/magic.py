import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
a = []

x = input()
while x!='0':
    lessThanCount = 0
    for i in range(len(x)-1):
        sumLoop = sum(int(j) for j in x[i+1:])
        if int(x[i])>sumLoop:
            lessThanCount+=1
    if lessThanCount==len(x)-1:
        a.append(int(x))
    x = input()
print(max(a) if len(a)>0 else "NONE")