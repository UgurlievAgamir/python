num = int(input())
fibonachi_list = [1, 1]

i = 0
while True:
    i += 1
    fibonachi_list.append(fibonachi_list[i - 1] + fibonachi_list[i])

    if num == fibonachi_list[i]:
        print(i+1)
        break
    elif num < fibonachi_list[i]:
        print(-1)
        break