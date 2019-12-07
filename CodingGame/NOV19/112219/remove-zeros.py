import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    row = input()
    for i in row:
        if i=="0":
            print("-",end="")
        else:
            print(i,end="")
    print("")