import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
s=0
for i in n:
    if int(i)%2==0:
        s+=(int(i))

print(s)

#shortest mode

print(sum(int(i)for i in input()if int(i)%2==0))