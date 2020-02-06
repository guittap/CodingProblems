n = int(input())
s = set()
for i in range(n):
    for j in range(n):
        if i**2+j**2 == n**2 and i not in s:
            print(i, j)
            s.add(i)
            s.add(j)
if len(s) < 1:
    print("...")
