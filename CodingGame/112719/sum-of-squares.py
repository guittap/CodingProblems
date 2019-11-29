import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = 0
for i in input().split():
    xi = int(i)
    s+=xi**2


print(s)