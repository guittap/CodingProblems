import sys
import math

d={"0":"HO","1":"HA","2":"HE","3":"HI","4":"BO","5":"BA","6":"BE","7":"BI","8":"KO","9":"KA","a":"KE","b":"KI","c":"DO","d":"DA","e":"DE","f":"DI"}

n = int(input())
a = str(hex(n))[2:]
for i in a:
    print(d[i],end="")