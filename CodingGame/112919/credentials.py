import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
b=""
for i in range(a):
    name = input()
    b=""
    for i in range(len(name)):
        if name[i]==',':
            b=name[i+2:]
    print(b if b>"" else "N/A")