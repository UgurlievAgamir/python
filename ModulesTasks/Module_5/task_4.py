numbers = []
endNum = 1
count = 0

while True:
    num = int(input())
    endNum = num
    numbers.append(num)

    if endNum == 0:
        break

i = 0
while i < len(numbers) - 1:
    if numbers[i] < numbers[i + 1]:
        count += 1
    i += 1
print(count)
