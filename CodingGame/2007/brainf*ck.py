s = 0
a = ""
for i in input().split("."):
    s += i.count("+")-i.count("-")
    a += chr(s)
print(a[:-1])
