n = int(input())
a = []
b = ""

for i in range(n):
    x = int(input())
    a.append(x)

a.sort(reverse=True)
for y in range(len(a) - 1):
    b += str(a[y]) + " "
b+=str(a[y+1])

print(b)