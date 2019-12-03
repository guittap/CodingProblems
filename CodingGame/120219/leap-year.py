import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

year = int(input())
a = False
if year%4==0:
    if year%100==0:
        if year%400==0:
            a=True
    else:
        a = True
        

print(str(a).lower())