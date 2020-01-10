import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


n = int(input())
list = input().split()
for i in list:
    if list.count(i) == 1:
        print(i)
    

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)