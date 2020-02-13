import sys
import math

dict = {}
n = int(input())

for i in range(n):
    value = set()
    key = i+1
    for j in range(key):
        if key%(j+1)==0: value.add(j+1)
    dict[key]=len(value)

for i in dict:
    if dict[i] == max(dict.values()): print(i,dict[i]);exit()