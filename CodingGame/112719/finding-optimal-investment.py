#my code
n=int(input())
a=dict()
for i in range(n):c=input().split();a[1-float(c[1])/float(c[2])]=c[0]
print(a[max(a)]if n>0else"NONE")

#austins code
q=[input().split() for x in range(int(input()))]
print(min(q,key=lambda x:float(x[1])/float(x[2]))[0] if q else"NONE")