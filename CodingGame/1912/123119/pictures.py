d={}
for i in range(int(input())):i,f=input().split();d[i]=float(f)
print(*sorted(d,key=d.get,reverse=True))