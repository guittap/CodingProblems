import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = input()
a = 0
for i in s:
    a += int(i)
    if i == "0":
        a = 0
    
print(a)