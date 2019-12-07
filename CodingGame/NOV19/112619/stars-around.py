#my code
p=print
a=input()
p('*'*len(a)+'*'*4)
p('*',a,'*')
p('*'*len(a)+'*'*4)

#best code
a=input()
b='*'*len(a)+'*'*4
c='\n* '
print(b+c+a+c+b)