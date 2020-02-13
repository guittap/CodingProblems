import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()
t2 = input()
for i in range(len(t)):
    if t[i]=="1" or t2[i]=="1":
        print(1,end="")
    else:
        print(0,end="")