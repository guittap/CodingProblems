m=int(input())
l=list(map(int,input().split()))
answer = [(i+1)**2 for i in range (int(m**.5)) if (i+1)**2 not in l]
if len(answer)>0:
    print(*answer)
else:
    print("None")
