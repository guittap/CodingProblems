s=input()
a=sum(1 for i in s if i.lower() in 'aeiou')
print((s+'\n')*a if a>0 else "NONE",end="")