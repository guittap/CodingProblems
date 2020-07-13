months = input()

if months[-1] == "D":
    print("J")
    exit()

if months[-1] == "J" and months[-2] == "D":
    print("F")
    exit()

if months[-1] == "F":
    print("M")
    exit()

if months[-1] == "M" and months[-2] == "F":
    print("A")
    exit()

if months[-1] == "A" and months[-2] == "M":
    print("M")
    exit()

if months[-1] == "M" and months[-2] == "A":
    print("J")
    exit()

if months[-1] == "J" and months[-2] == "M":
    print("J")
    exit()

if months[-1] == "J" and months[-2] == "J":
    print("A")
    exit()

if months[-1] == "A" and months[-2] == "J":
    print("S")
    exit()

if months[-1] == "S":
    print("O")
    exit()

if months[-1] == "O":
    print("N")
    exit()

if months[-1] == "N":
    print("D")
    exit()
