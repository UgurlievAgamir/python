import round_system as rs


def wof_start() -> None:
    """
    Функция запускает игру
    :return: ничего
    """
    while True:
        command: int = int(input('1 - Начать игру, 2 - Выход \n'))

        if command == 1:
            rs.start_game()
            print('Хотите сыграть еще?')
        elif command == 2:
            break
