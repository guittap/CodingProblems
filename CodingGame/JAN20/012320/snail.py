import math
a=input
i=int
d=i(a())
x=i(a())
y=i(a())
print(1if d<=x else"Impossible"if x<=y else math.ceil(d/(x-y))-((x//(x-y))-1))