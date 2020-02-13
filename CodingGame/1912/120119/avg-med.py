# my code
import math
x=list(map(int,input().split()))
y=len(x)
print(sorted(x)[y//2]if y%2else math.ceil(sum(x)/y))

#best code
*q,=sorted(map(int,input().split()))
print(q[len(q)//2]if len(q)%2else 1+sum(q)//len(q))