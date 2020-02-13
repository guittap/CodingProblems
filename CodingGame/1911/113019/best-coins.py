s=input()[1:].split(".")
i=int(s[1])
b=i//25
e=i-b*25
c=e//10
f=e-c*10
d=f//5
print(int(s[0]),b,c,d,f-d*5)