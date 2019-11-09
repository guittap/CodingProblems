import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = n = int(input())

while a > 1:
    if a > 1:
        print(a, end = " ")
    if a % 2 == 1:
        a = a * 3 + 1
    else:
        a //= 2

print(a)