a=k=""
x=0
n=int(input())
for i in input().split():
    if x==0:
        k=str(i)
        x+=1
    else:
        a+=str(i)+" "
print(a+k)