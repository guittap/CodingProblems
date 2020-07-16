import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
list = []
for i in input().split():
    list.append(int(i))

pr = ""
for i in range(n):
    running = 1
    for j in range(n):
        if i != j:
            running *= list[j]
    pr += str(running)+" "

print(pr[:-1])
