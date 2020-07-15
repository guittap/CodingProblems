import math
s = input()
a = math.ceil(len(s)/2)
for x, y in zip(s[:a], s[a:]):
    print(x, y, sep="", end="")
if len(s) % 2:
    print(s[a-1])
