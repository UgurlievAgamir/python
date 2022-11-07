import round_system as rs

while True:
    command = int(input('1 - Начать игру, 2 - Выход \n'))

    if command == 1:
        rs.start_game()
        print('Хотите сыграть еще?')
    elif command == 2:
        break
