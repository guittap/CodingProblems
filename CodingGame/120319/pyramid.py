n = int(input())
number = 1
for i in range(n):
    a=""
    for j in range(n-(n - (i + 1))):
        a+=str(number)+" "
        number+=1
    print(a[:-1])