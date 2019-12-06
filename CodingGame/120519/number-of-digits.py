import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
for i in range(n):
    sum = 0
    row = input()
    for i in row:
        if i.isdigit():
            sum+=1
    print(sum)