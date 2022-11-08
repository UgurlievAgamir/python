N = int(input())
answer = ''
i = 1
while i ** 2 <= N:
    answer += str(i ** 2) + ' '
    i += 1

print(answer)
