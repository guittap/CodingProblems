m=input()
a=""
if len(m)%2:a=m[0];m=m[1:]
n=""
for i in range(len(m)//2):n+=m[i*2+1]+m[i*2]
print(n+a)