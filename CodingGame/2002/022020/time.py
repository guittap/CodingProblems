n = int(input())
h = str(n//3600000)
n -= int(h)*3600000
m = str(n//60000)
n -= int(m)*60000
s = str(n//1000)
n = str(n-int(s)*1000)
print(h if len(h) > 1 else "0"+h, m if len(m) == 2 else "0"+m, s if len(s)
      == 2 else "0"+s, n if len(n) == 3 else "0"+n if len(n) == 2 else "00"+n)
