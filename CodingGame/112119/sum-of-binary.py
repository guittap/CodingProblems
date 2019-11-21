import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x = int(input())
    x = bin(x)
    x = str(x)[2:]
    print(sum(int(i) for i in x))