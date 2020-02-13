import math
n=int(input())
a=2**int(math.log(n,2))
b=2**math.ceil(math.log(n,2))
print(b if n-a>b-n else a)