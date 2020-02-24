r, c, v, h = map(int, input().split())
currLetter = True
heightList = []
widthList = []

for i in range(v):
    heightList.append(int(input()))

for i in range(h):
    widthList.append(int(input()))

rowLetter = True
colLetter = True
for i in range(v):
    for x in range(heightList[i]):
        colLetter = rowLetter
        for j in range(h):
            print('B'*widthList[j] if colLetter else 'W'*widthList[j], end="")
            colLetter = not colLetter
        print()
    rowLetter = not rowLetter
