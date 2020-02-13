def H(n):
    if n<3:return 1
    return (H(H(n-1))+H(n-H(n-1)))   
a=""
for i in range(int(input())):a+=str(H(i+1))+" "
print(a[:-1])