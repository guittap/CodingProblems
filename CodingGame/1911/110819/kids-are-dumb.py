import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a = []
b = ""

for char in s:
    if char.isnumeric():
        a.append(char)
        
a.sort()
for i in range(len(a)-1):
    b += str(a[i]) + "+"
    
if len(a) > 1:
    print(b + str(a[i+1]))
else:
    print(a[0])