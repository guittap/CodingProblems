s=input()
count=0
if len(s)%2:count+=1
for i in s:
    if count%2: print(i.lower(),end="")
    else: print(i.upper(),end="")
    count+=1