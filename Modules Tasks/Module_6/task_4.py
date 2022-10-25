list = [s for s in input().split()]
max_num = -100000
min_num = 100000
max_index = 0
min_index = 0

for i in range(0, len(list)):
    if int(list[i]) > int(max_num):
        max_num = list[i]
        max_index = i
    if int(list[i]) < int(min_num):
        min_num = list[i]
        min_index = i

list[max_index] = min_num
list[min_index] = max_num

print(" ".join(list))
