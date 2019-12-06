s=int(input())//1000
m=s//60
s-=m*60
h=m//60
m-=h*60
d=h//24
h-=d*24
a=""
if d>0:a=str(d)+"d "
if h>0:a+=str(h)+"h "
if m>0:a+=str(m)+"m "
if s>0:a+=str(s)+"s "
print(a[:-1]if a>""else"0s")