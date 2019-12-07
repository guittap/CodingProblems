import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())



print('#'*n)
for i in range(n-2):
    print('#'+' '*(n-2)+'#')
if n>1:
    print('#'*n)