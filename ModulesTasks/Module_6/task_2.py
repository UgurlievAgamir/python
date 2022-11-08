list = [s for s in input().split()]
list_ans = []
for i in range(0, len(list) - 1):
    if int(list[i]) < int(list[i + 1]):
        list_ans.append(list[i + 1])

print(" ".join(list_ans))
