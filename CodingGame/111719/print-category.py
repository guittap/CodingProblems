import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())
n = int(input())
for i in range(n):
    f, t, category = input().split()
    f = int(f)
    t = int(t)
    
    if x>=f and x<=t:
        print(category)