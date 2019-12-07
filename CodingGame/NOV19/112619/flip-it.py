q=input
w=range
l=int(q())
h=int(q())
a=[]
for i in w(l):a.append(q().split())
for i in w(h):
    s=""
    for j in w(l):s+=a[l-j-1][i]+" "
    print(s[:-1])