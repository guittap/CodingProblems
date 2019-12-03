
def distance (a,b):
    d = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dist = 0
    aPlace = 0
    for i in range(26):
        if d[i]==a:
            aPlace = i
            break
    i = aPlace    
    while d[i] != b:
        i+=1
        if i > 25:
            i=0
        dist+=1
    return dist

a = input()
b = input()
bool = True
dist = distance(a[0],b[0])

for i in range(len(a)):
    if distance(a[i],b[i]) != dist:
        bool = False

print(str(bool).lower())