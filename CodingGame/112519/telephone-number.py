a,b="",0
for i in input():
    if i.isdigit():
        i=int(i)
        if 0<i<6:
            a+='.'*i+'-'*(5-i)+" "
        elif i>5:
            a+='-'*(i-5)+'.'*(5-(i-5))+" "
        elif i==0:
            a+='-'*5+" "
    else:
        b=1
if len(a) > 60:
    b=1
print(a[:-1] if b<1 else "Untransformable")