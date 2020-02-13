import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = int(input())
n = int(input())
a = dict()
s = 0

for i in range(n):
    car_id, tip = [int(j) for j in input().split()]
    a[car_id]=tip
car_ids = input().split()

for i in car_ids:
    if int(i) < 0:
        s+=a.get(abs(int(i)))

print(s)