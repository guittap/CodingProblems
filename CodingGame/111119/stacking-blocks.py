import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

hello = 0
n, m = [int(i) for i in input().split()]
s = int(input())
for i in range(n):
    row = input()
    for x in row:
        if x == 'o':
            hello += 1
            
print(hello * s)