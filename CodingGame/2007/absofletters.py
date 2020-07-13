a = 0
for i in input():
    a += 1if i.isupper()else -1if i.islower()else 0
print(abs(a))
