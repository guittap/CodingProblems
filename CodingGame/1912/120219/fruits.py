import sys
import math

dict1 = dict()
dict2 = dict()

n = int(input())
for i in range(n):
    fruits, number= input().split()
    dict1[fruits]=number
line = input()
for i in line:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1
        
sum = 0
for i in dict1:
    if i in dict2:
        sum+=int(dict2[i])//int(dict1[i])


print(sum)