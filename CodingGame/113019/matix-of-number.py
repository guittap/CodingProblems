r=int(input())
c=int(input())
for i in range(r):
    a=""
    for j in range(c):b=str(i*c+j);a+=" "*(len(str(r*c-1))-len(b)+1)+b
    print(a)