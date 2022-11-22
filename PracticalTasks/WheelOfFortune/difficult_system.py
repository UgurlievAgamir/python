is_difficult_set: bool = False
lives: int = 0


def get_lives_count_by_difficult() -> int:
    """

    :return: колмчество жизней в зависимости от выбранного пользователем сложности игры
    """
    difficult: int = int(input('Выберите сложность: 1 - Легкая, 2 - Нормальная, 3 - Сложная '))

    if difficult == 1:
        return 7
    elif difficult == 2:
        return 5
    elif difficult == 3:
        return 3
    else:
        print('Неверная сложность')
        return get_lives_count_by_difficult()
