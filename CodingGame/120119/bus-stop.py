import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

c = int(input())
n = int(input())
p = []
for i in range(n):
    p.append(int(input()))

count = 0
while sum(p)!=0:
    a = 0
    for i in range(n):
        count+=1
        a+=p[i]
        p[i] = 0
        if a>c:
            p[i]=a-c
            a=c
    count+=1
print(count)