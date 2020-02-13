import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a = 0
for i in s:
    if i.isalpha():
        if i.islower():
            a+=1

print(a)