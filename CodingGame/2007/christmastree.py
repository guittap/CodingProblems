import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

size = int(input())

for i in range(size):
    for j in range(i+2):
        print(" "*(size-j) + "*"*(j*2+1))
print(" "*size + "|")
print("="*size + "V" + "="*size)
