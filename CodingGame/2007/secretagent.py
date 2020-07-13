n, m = [int(i) for i in input().split()]
for i in range(n):
    v = input()
    if int(v[m-2:m]) != sum([int(i)for i in v[:m-2]]):
        print("Agent "+str(i+1))
        exit()
print("No traitors")
