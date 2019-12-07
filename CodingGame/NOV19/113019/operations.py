i=int
p=print
o,x,n=input().split()
x=i(x)
a=i(n[:x])if x>0 else 0
b=i(n[x:])
if o=='-':p(a-b)
elif o=='*':p(a*b)
elif o=='+':p(a+b)
else:p(a//b)