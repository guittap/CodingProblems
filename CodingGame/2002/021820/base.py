# my code
x = input()
for i in range(max(2, max(int(i, 16)for i in x)+1), 17):
    print(i, int(x, i))

# bigbraincode
s = input()
for b in range(2, 17):
    try:
        print(b, int(s, b))
    except:
        pass
