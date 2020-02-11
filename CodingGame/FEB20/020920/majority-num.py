def x(): return int(input())


n = [x()for i in range(x())]
for i in n:
    if n.count(i) >= len(n)//2+1:
        print(i)
        exit()
print("N")
