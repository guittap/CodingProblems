n = int(input())
for i in range(n):
    if i==n-1:print(("*"*n)+" *"*(n*2-1))
    else:print((" "*(n))+(" *"*(i+1))+" "*((n-i-2)*4+2)+(" *"*(i+1)))