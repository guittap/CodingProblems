import sys
import math

n = int(input())
m = int(input())
a = 0
b = []

for i in range(m):
    b.append(0)

print("ROWS:")
for i in range(n):
    a=0
    s = input()
    x = 0
    for i in s:
        if i=='*':
            a+=1
            b[x] = b[x] + 1
        x+=1
    print(a)
    
print("COLUMNS:")
for i in range(m):
    print(b[i])