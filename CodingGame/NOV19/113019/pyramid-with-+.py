import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n,0,-1):
    print("+"*(n-i),end="")
    for j in range(i):
        print(j+1,end="")
    print("")
