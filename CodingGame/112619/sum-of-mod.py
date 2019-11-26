import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m = int(input())
n = int(input())
s = 0
for i in input().split():
    e = int(i)
    s += int(e%m)
    
print(s)