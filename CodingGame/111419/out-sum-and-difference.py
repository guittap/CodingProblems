import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sum = int(input())
difference = int(input())

a = [int((sum/2)-(difference/2)), int((sum/2)+(difference/2))]
a.sort()

print(a[0])
print(a[1])
