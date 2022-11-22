import random


def birthday(people_count: int, iterations_count: int = 1000) -> str:
    """
    Функция проверяет парадокс дней рождения
    :param people_count: количество людей в группе
    :param iterations_count: количество итераций для проверки парадокса
    :return: результат эксперимента
    """

    days: list = [day for day in range(0, 29)]
    months: list = [month for month in range(0, 13)]

    count_coincidences: int = 0
    count_not_coincidences: int = 0

    for iterations in range(0, iterations_count + 1):
        d_data: list = []
        m_data: list = []

        for i in range(0, people_count + 1):
            d_data.append(random.choice(days))
            m_data.append(random.choice(months))

        for i in range(0, people_count):
            if d_data.count(d_data[i]) == 1 or m_data.count(m_data[i]) == 1:
                count_not_coincidences += 1
                pass

            for j in range(0, people_count):
                if j == i:
                    pass

                if d_data[j] == d_data[i] and m_data[j] == m_data[i]:
                    count_coincidences += 1

    return f"количество совпадений: {count_coincidences} " \
           f"количество не совпадений: {count_not_coincidences} " \
           f"вероятность совпадения: {(count_coincidences * 100) / (count_not_coincidences + count_coincidences)}"
