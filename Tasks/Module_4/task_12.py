month = int(input())
day = int(input())

if month == 2:
    if day == 28:
        month += 1
        day = 1
    else:
        day += 1
else:
    if month % 2 == 0:
        if day == 30:
            month += 1
            day = 1
        else:
            day += 1
    else:
        if day == 31:
            month += 1
            day = 1
        else:
            day += 1

print(f'{day}-{month}-2022')
