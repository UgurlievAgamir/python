import random


def birthday(people_count):
    days = [day for day in range(0, 28)]
    months = [month for month in range(0, 12)]

    D_data = []
    M_data = []

    count_coincidences = 0
    count_not_coincidences = 0

    for i in range(0, people_count + 1):
        D_data.append(random.choice(days))
        M_data.append(random.choice(months))

    for i in range(0, people_count):
        if D_data.count(D_data[i]) == 1 or M_data.count(M_data[i]) == 1:
            count_not_coincidences += 1
            pass

        for j in range(0, people_count):
            if j == i:
                pass

            if D_data[j] == D_data[i] and M_data[j] == M_data[i]:
                count_coincidences += 1

    return f"количество совпадений: {count_coincidences} " \
           f"количество не совпадений: {count_not_coincidences} " \
           f"вероятность совпадения: {(count_coincidences * 100) / (count_not_coincidences + count_coincidences)}"


def monty_hall(count):
    count = 0
    count_changed_choice = 0

    for i in range(0, 10000):
        a = [0, 0, 1]
        player_choice = random.choice(a)
        if player_choice == 1:
            count += 1
        else:
            a.remove(0)
            a.remove(player_choice)
            if a[0] == 1:
                count_changed_choice += 1

    return f"{count} {count_changed_choice}"
