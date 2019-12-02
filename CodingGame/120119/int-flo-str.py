string = input()

a=0
c=0
d=True
for i in string:
    if i.isdigit():a+=1
    elif i=='.':c+=1
    else:d=False
print("integer" if a==len(string) else "float" if a==len(string)-1 and c==1 else "string")