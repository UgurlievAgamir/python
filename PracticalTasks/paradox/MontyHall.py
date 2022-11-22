import random


def monty_hall(count_of_iterations: int) -> str:
    """
    Функция проверяет парадокс монти холла
    :param count_of_iterations: количество итераций для проверки парадокса
    :return: результат эксперимента
    """

    count: int = 0
    count_changed_choice: int = 0

    for i in range(0, count_of_iterations):
        a: list = [0, 0, 1]
        player_choice: int = random.choice(a)
        if player_choice == 1:
            count += 1
        else:
            a.remove(0)
            a.remove(player_choice)
            if a[0] == 1:
                count_changed_choice += 1
    return f'количество не меняя выбор: {count} количество поменяв выбор: {count_changed_choice} вероятность выиграша ' \
           f'при своем выборе: {(count * 100) / (count + count_changed_choice)} '
