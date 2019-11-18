import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    p0, p1 = [int(j) for j in input().split()]
    a = str(bin(p0))
    b = str(bin(p1))
    a = a[2::]
    b = b[2::]
    print(int(a) + int(b))