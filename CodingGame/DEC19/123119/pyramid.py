number = int(input())
reverse = False

for i in range(number):
    list = [i+1 for i in range(number-i)]
    print(*list[::-1] if reverse else list,sep="")
    reverse = not reverse