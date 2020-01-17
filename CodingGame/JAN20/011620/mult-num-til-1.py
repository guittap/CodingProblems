import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
count = 0

while len(str(n)) > 1:
    temp = 1
    for i in str(n):
        temp *= int(i)
    n = temp
    count +=1

print(count)