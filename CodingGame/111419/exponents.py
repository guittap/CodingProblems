import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, r = [int(i) for i in input().split()]

for i in range(n-1):
    print(r**i, end=" ")
print(r**(i+1))