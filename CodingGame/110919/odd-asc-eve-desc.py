import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input().split()
a = set()
b = set()

for i in range(len(s)):
    if int(s[i])%2 == 1:
        a.add(int(s[i]))
    else:
        b.add(int(s[i]))
  
a = list(a)
b = list(b)

a.sort()
b.sort(reverse = True)
print(*a, *b)