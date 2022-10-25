list = [s for s in input().split()]

for i in list:
    if int(i) % 2 == 0:
        list.remove(i)

print(" ".join(list))
