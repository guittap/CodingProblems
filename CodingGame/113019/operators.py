a,b,c,d=map(int,input().split())
x={a+b:'+',a*b:'*',a/b:'/',a-b:'-'}
y={c+d:'+',c*d:'*',c/d:'/',c-d:'-'}
for i in x:
    if i in y:print(x[i],y[i]);exit()
print(-1)