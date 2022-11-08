import WheelOfFortune.db_manager as db_m
import WheelOfFortune.difficult_system as ds
import WheelOfFortune.word_handler as wh


def win_round():
    print('Вы выиграли! Приз в студию!')

    db_m.current_session_record += 1

    if db_m.current_session_record > db_m.record:
        print('Это ваш новый рекорд угаданных подряд слов: ' + str(db_m.current_session_record))
        db_m.record = db_m.current_session_record
        db_m.update_record()


def start_game():
    lifes_count = 0
    if not ds.is_difficult_set:
        lifes_count = ds.get_lifes_count_by_difficult()
        ds.lifes = lifes_count
        ds.is_difficult_set = True
    else:
        lifes_count = ds.lifes
    current_word = db_m.get_random_word()
    locked_word = wh.lock_word(current_word)

    while True:
        print(f'{locked_word} | {db_m.heart_symbol}x{lifes_count}')
        player_answer = input('Назовите букву или слово целиком: ')

        if player_answer == current_word:
            win_round()
            break
        elif player_answer in current_word:
            if player_answer in locked_word:
                print('Эта буква уже открыта')
            else:
                print('Правильно!')
                locked_word = wh.unlock_part_of_word(current_word, locked_word, player_answer)

            if db_m.locked_symbol not in locked_word:
                win_round()
                break
        else:
            print('Неправильно. Вы теряете жизнь')
            lifes_count -= 1

        if lifes_count == 0:
            print('Жизни закончились. Вы проиграли')
            print('Ваш рекорд ' + str(db_m.record))
            break
