import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x = int(input())
    a = bin(x)
    a = str(a)[2:]
    print(*a,sep="")