X = int(input())
Y = int(input())

count = 1

while X <= Y:
    X += X / 10
    count += 1

print(count)
