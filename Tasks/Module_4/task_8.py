month = int(input())

if month == 2:
    print(28)
else:
    if month % 2 == 0:
        print(30)
    else:
        print(31)
