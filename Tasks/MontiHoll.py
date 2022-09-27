import random

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
print(count, count_changed_choice)
