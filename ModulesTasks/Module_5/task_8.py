numbers = []
endNum = 1

max_count = 1
current_count = 1

while True:
    endNum = int(input())
    numbers.append(endNum)

    if endNum == 0:
        break

i = 1

while i < len(numbers):
    if numbers[i - 1] == numbers[i]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        max_count = max(max_count, current_count)
        current_count = 1
    i += 1

print(max_count)
