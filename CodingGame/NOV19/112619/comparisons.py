q=range
w=input
p=print
n=int(w())
a=""
b=""
for i in q(n):a+=w()
e=w()
for i in q(n):b+=w()
for i in q(n):
    for j in q(n):
        if a[i*n+j]==b[i*n+j]:p(a[i*n+j],end="")
        elif a[i*n+j]==".":p(b[i*n+j],end="")
        elif b[i*n+j]==".":p(a[i*n+j],end="")
        else:p('X',end="")
    p("")