list = [s for s in input().split()]
list_gen = []

for i in range(0, len(list)):
    if list_gen.__contains__(list[i]):
        print("ДА")
    else:
        print("НЕТ")

    list_gen.append(list[i])
