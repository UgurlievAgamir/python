num = int(input())

if num == int(str(num)[::-1]):
    print('Да')
else:
    print('Нет')
