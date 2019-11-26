import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n_1 = input()
n_2 = input()

for i in range(len(n_1)):
    if n_1[i]=="1" and n_2[i]=="1":
        print(1, end="")
    else:
        print(0, end="")