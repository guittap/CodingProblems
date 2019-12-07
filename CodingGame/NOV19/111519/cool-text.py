message = input()

if len(message) % 2 == 1:
    for i in range(len(message)//2+1):
        print(" "*i, end="")
        for y in range(len(message)-(2*i)):
            print(message[y+i], end="")
        print("")
    for i in range(len(message)//2-1,-1,-1):
        print(" "*i, end="")
        for y in range(len(message)-(2*i)):
            print(message[y+i], end="")
        print("")
else:
    print("Error")