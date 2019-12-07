import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()
e=0
o=0

for i in range(len(n)):
    if (i+1)%2==0:
        e+=int(n[i])
    else:
        o+=int(n[i])

print(o-e)