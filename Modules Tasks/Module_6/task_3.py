list = [s for s in input().split()]
list_ans = []
for i in range(0, len(list) - 1):
    if not list_ans.__contains__(list[i]) and not list_ans.__contains__(list[i + 1]):
        list_ans.append(list[i + 1])
        list_ans.append(list[i])

if len(list) % 2 != 0:
    list_ans.append(list[len(list) - 1])

print(" ".join(list_ans))
