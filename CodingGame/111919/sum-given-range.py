import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
x=[]
for i in input().split():
    x.append(int(i))

m = int(input())
for i in range(m):
    start_range, end_range = [int(j) for j in input().split()]
    a=sum(x[start_range: end_range+1])
    print(a)