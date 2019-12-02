import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = input().split()
y = input().split()

sum = 0
for i in range(len(x)):
    sum += int(y[i]) - int(x[i]) 

print(sum)