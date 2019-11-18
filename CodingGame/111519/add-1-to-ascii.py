import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = input()
x = 0
for i in l:
    a = ord(i) + x
    print(chr(a), end="")
    x+=1