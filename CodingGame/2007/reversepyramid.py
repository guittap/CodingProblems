n = int(input())
print("".join((str(n)*(n-i))+'\n'for i in range(n))[:-1])
