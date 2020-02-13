d=float(input())
l,w=input().split(":")
l,w=float(l),float(w)
a=(l**2+w**2)**(1/2)
b=d/a
print(round(l*b,2),"x",round(w*b,2))