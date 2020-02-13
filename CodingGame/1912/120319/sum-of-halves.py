for i in range(int(input())):
    t=input()
    print(str(sum(int(i)for i in t[0:3])==sum(int(i)for i in t[3:6])).lower())