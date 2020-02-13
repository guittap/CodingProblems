import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = 0

for i in range(n):
    x=0
    for j in input().split():
        val = int(j)
        if i==x or n-i-1==x:
            s+=val
            
        x+=1

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(s)