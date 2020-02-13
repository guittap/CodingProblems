n=int(input())
b=[]
for i in range(n):
    s=input()
    if 'A' in s:
        a=s
    b.append(s)
for i in b:
    for i in b:
        if i[0]==a[-1]:
            a+=i[1:]
print(a)