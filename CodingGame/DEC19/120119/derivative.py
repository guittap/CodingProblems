a,b=input().split("x")
if"^"in b:m=int(b[1:]);x=int(a)if a>''else 1;print(x*m,'x','^'+str(m-1)if m>3else'',sep="")
else:print(a)