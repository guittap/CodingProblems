import sys
import math

n = int(input())

a=""
for i in range(n):
    if i==0:
        a+=" _ "
    else:
        a+="  _ "
print(a)
a=""
for i in range(n):
    if i==0:
        a+='/ \\'
    else:
        a+='_/ \\'
print(a)
for i in range(n):
    a=" "*(2*i)+"\\_/ "*(n-i)
    print(a[:-1])