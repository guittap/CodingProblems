import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = 0
a = set()
for i in range(n):
    path = input()[1:]
    b=""
    for i in path:
        if i == "/":
            a.add(b)
        b+=i
    a.add(b)
print(len(a))