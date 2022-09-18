year = int(input())
if year % 10 or (year % 100) % 10 or (year % 100) // 10 > 0:
    if (year % 100) // 10 == 9:
        print((((year // 1000) + 1) * 1000) // 100)
    else:
        print((year // 1000) * 10 + ((year % 1000) // 100) + 1)
else:
    print(year // 100)
