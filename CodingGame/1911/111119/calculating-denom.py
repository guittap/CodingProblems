a,b=[int(i) for i in input().split()]
s,e=[int(i) for i in input().split()]
w=x=y=z=0
for i in range(s,e+1,1):
    if i%a==0 and i%b!=0:
        w+=1
    elif i%a!=0 and i%b==0:
        x+=1
    elif i%a==0 and i%b==0:
        y+=1
    else:
        z+=1
print(w,x,y,z)