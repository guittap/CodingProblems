n=int(input())
for i in range(n):
 if i**i+i==n:print(True);exit()
 if i**i+i>n:break
print(False)

#best code
print(int(input())in[i**i+i for i in range(99)])