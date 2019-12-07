import math
c=int(input())
e=int(input())
s=c
if e>1:
    while e<=c:c/=e;s+=c
print(math.ceil(s) if e>1 else c if e<1 else "IMPOSSIBLE")