import sys
import math

a=[]
for i in range(9):
    a.append(set())

for i in range(9):
    w = input()
    j=0
    for x in w:
        if x.isdigit():
            a[j].add(int(x))
        j+=1
            
for i in range(9):
    for x in range(9):
        if x+1 not in a[i]:
            print (x+1,end="")