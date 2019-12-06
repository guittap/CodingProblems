set = set()
for i in input().split():
    set.add(int(i)**2)
set = list(set)
set.sort()
print(set)