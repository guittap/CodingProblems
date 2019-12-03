import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
count = 0
for i in s:
    if i in '690':
        count+=1
    elif i=='8':
        count+=2

print(count)