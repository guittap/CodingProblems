import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = []
a.append(n)
while n>1:
    if n%2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    a.append(n)
print(*a)