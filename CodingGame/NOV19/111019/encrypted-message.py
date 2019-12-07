import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    e = int(input())
    if e < 0:
        print (" ", end="")
    else:
        e = 122 - e
        print(chr(e), end="")