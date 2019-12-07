import sys
import math

dict = dict()
n1 = int(input())
for i in range(n1):
    w1,w3 = input().split(";")
    if w1 not in dict:
        dict[w1]=[w3]
    else:
        dict[w1].append(w3)
n2 = int(input())
for i in range(n2):
    w2,w4 = input().split(";")
    if w2 not in dict:
        dict[w2]=[w4]
    else:
        dict[w2].append(w4)

for i in dict:
    a = i + ": "
    for j in dict[i]:
        a+=j+" and "
    print(a[:-5])