import sys
import math

max = 0
sum = 0
last = ""
n = input()

for i in n:
    if last == i:
        sum += 1
    else:
        sum = 1
    if sum > max:
        max = sum
    last = i
print(max)