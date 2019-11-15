import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = ""
b = bin(n)

x=0
for i in b:
    if x > 1:
        if i == '0':
            a+="1"
        else:
            a+="0"
    x+=1
print(int(a,2))