import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
x = []
y = []
for i in input().split():
    x.append(int(i))
for i in input().split():
    y.append(int(i))
    
x.sort()
y.sort()
for i in range(len(x)-1):
    print("(", end="")
    print(x[i], end="")
    print(", ", end="")
    print(y[i], end="")
    print("), ", end="")
 
i+=1   
print("(", end="")
print(x[i], end="")
print(", ", end="")
print(y[i], end="")
print(")", end="")