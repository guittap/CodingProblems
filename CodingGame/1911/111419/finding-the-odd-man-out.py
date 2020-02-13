import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a = set()

for i in s:
    a.add(i)

a = list(a)
for i in range(9):
    if str(i+1) not in a:
        print(i+1)