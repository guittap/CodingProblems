import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
scr = input().lower()
for i in range(n):
    ans = input()
    acc = ans.lower()
    correct = 0
    for i in acc:
        if acc.count(i) == scr.count(i): correct+=1
    if correct == len(scr): print(ans); exit()