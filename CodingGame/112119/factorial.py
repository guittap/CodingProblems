import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = 1
for i in range(1,n+1,1):
    a*=i

print(a)