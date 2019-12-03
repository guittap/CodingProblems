def ackermann(m,n):
    if n<0 or m<0:
        return -1
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1)) 
          

m, n = [int(i) for i in input().split()]

print (ackermann(m, n)) 