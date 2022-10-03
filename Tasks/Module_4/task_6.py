num = int(input())
num_str = str(num)

if int(num_str[2]) > int(num_str[1]) > int(num_str[0]):
    print('Да')
else:
    print('Нет')
