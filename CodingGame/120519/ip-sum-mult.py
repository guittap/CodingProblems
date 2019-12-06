import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

ip = input()
sum = 0
first = int(ip[0])
for i in ip:
    if i.isdigit():
        sum+=int(i)

print(first*sum)