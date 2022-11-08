N = int(input())
hour = N // 60
minutes = N % 60

if minutes < 10:
    print(f'{hour}:{minutes}0')
else:
    print(f'{hour}:{minutes}')
