import db_manager as db_m
import difficult_system as ds

locked_symbol = '\u25A0'
heart_symbol = '\u2764'


def lock_word(word):
    word_list = [a for a in word]
    output = ''

    for i in range(0, len(word)):
        word_list[i] = locked_symbol

    return output.join(word_list)


def unlock_part_of_word(unlocked_word, locked_word, part):
    all_part_indexs = []

    locked_word_list = [a for a in locked_word]
    output = ''

    for i in range(0, len(unlocked_word)):
        if unlocked_word[i] == part:
            all_part_indexs.append(i)

    for j in all_part_indexs:
        locked_word_list[j] = part

    return output.join(locked_word_list)


def win_round():
    print('Вы выиграли! Приз в студию!')

    db_m.current_session_record += 1

    if db_m.current_session_record > db_m.record:
        print('Это ваш новый рекорд угаданных подряд слов: ' + str(db_m.current_session_record))
        db_m.record = db_m.current_session_record
        db_m.update_record()

    db_m.record = max(db_m.current_session_record, db_m.record)


def start_game():
    lifes_count = 0
    if not ds.is_difficult_set:
        lifes_count = ds.get_lifes_count_by_difficult()
        ds.lifes = lifes_count
        ds.is_difficult_set = True
    else:
        lifes_count = ds.lifes
    current_word = db_m.get_random_word()
    locked_word = lock_word(current_word)

    while True:
        print(f'{locked_word} | {heart_symbol}x{lifes_count}')
        player_answer = input('Назовите букву или слово целиком: ')

        if player_answer == current_word:
            win_round()
            break
        elif player_answer in current_word:
            if player_answer in locked_word:
                print('Эта буква уже открыта')
            else:
                print('Правильно!')
                locked_word = unlock_part_of_word(current_word, locked_word, player_answer)

            if locked_symbol not in locked_word:
                win_round()
                break
        else:
            print('Неправильно. Вы теряете жизнь')
            lifes_count -= 1

        if lifes_count == 0:
            print('Жизни закончились. Вы проиграли')
            print('Ваш рекорд ' + str(db_m.record))
            break
