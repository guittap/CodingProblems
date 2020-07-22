import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

left = []
right = []

for i in range(3):
    line = input()
    if line[0].isdigit():
        left.append(int(line[0])-i)
    if line[1].isdigit():
        right.append(int(line[1])-i)

    for i in left:
        if i in right:
            print("false")
            exit()

print("true")
