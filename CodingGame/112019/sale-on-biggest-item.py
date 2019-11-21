#my solution
import math
s,a=1-int(input())/100,[]
for i in range(int(input())):a.append(int(input()))
b=max(i for i in a)
print(math.ceil(sum(i for i in a)+b*s-b))

# better solution
a=lambda:int(input())
l,p=[],a()
for i in[1]*(a()):l+=[a()]
print((sum(l)-int(max(l)*p/100)))