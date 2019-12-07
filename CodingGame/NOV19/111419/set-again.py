import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = set()
for i in range(n):
    x = int(input())
    if x not in a:
        print (x)
    a.add(x)