t=input().split()
n=int(input())
a=[]
for i in range(len(t),0,-1):
    m=n//int(t[i-1])
    if m>0:n-=int(t[i-1])*m;a.append(str(m)+"x"+str(int(t[i-1])))
print(*a)