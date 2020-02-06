import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())
y = int(input())

for i in range(99):
    if x * (i+1) % 10 == y or x * (i+1) % 10 == 0:
        print(i+1)
        exit()
