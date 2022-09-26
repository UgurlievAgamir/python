import random

lives = 3
count = 0

while True:
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    operator = random.randint(0, 4)

    player_answer = 0
    answer = 0

    if operator == 0:
        player_answer = int(input(f'{n1} + {n2} = '))
        answer = n1 + n2
    elif operator == 1:
        player_answer = int(input(f'{n1} - {n2} = '))
        answer = n1 - n2
    elif operator == 2:
        player_answer = float(input(f'{n1} / {n2} = '))
        answer = n1 / n2
    else:
        player_answer = int(input(f'{n1} * {n2} = '))
        answer = n1 * n2

    if player_answer == answer:
        print('Верно')
        count += 1
    else:
        print('Неверно')

        lives -= 1
        if lives <= 0:
            print('Игра окончена')
            print(f'Количество решенных примеров {count}')
            break

        print(f'Осталось жизней {lives}')
