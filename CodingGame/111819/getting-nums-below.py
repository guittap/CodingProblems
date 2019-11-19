import sys
import math

s = input()
for i in s:
    if 0 <= ord(i)-ord("A") <= 27:
        for i in range(ord(i)-ord("A")+1):
            print(chr(i+ord("A")), end="")
    elif 0 <= ord(i)-ord("a") <= 27:
        for i in range(ord(i)-ord("a")+1):
            print(chr(i+ord("a")), end="")
    else:
        for i in range(int(i)+1):
            print(i, end="")