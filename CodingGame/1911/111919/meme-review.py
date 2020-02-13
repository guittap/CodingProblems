import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

meme = input()
a = set()
for i in meme:
    if i.isalpha():
        a.add(i)


s= 0

for i in a:
    s+=(ord(i))
    
a = s%len(meme)
print(a if a<=10 else 10,"/10",sep="")