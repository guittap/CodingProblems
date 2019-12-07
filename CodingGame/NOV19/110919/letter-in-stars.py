import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

c = input()
l = int(input())

if l%2 == 0:
    print("CAN'T")
else:
    for i in range(l):
        if i != l//2:
            print("*", end="")
        else: 
            print(c, end="")
        
