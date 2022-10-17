list_1 = [s for s in input().split()]
list_2 = [s for s in input().split()]
list_ans = []

for i in range(0, len(list_1)):
    for j in range(0, len(list_2)):
        if list_1[i] == (list_2[j]):
            list_ans.append(list_1[i])

print(" ".join(list_ans))
