import db_manager as db_m
import difficult_system as ds
import word_handler as wh


def win_round() -> None:
    """
    Функция засчитывает победу в раунде
    """
    print('Вы выиграли! Приз в студию!')

    db_m.current_session_record += 1

    if db_m.current_session_record > db_m.record:
        print('Это ваш новый рекорд угаданных подряд слов: ' + str(db_m.current_session_record))
        db_m.record = db_m.current_session_record
        db_m.update_record()


def start_game() -> None:
    """
    Функция разыгрывает игру до проигрыша игрока или до конца имеющихся слов
    """
    lives_count: int = 0
    if not ds.is_difficult_set:
        lives_count = ds.get_lives_count_by_difficult()
        ds.lives = lives_count
        ds.is_difficult_set = True
    else:
        lives_count = ds.lives
    current_word: str = db_m.get_random_word()
    locked_word: str = wh.lock_word(current_word)

    while True:
        print(f'{locked_word} | {db_m.heart_symbol}x{lives_count}')
        player_answer: str = input('Назовите букву или слово целиком: ')

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
            lives_count -= 1

        if lives_count == 0:
            print('Жизни закончились. Вы проиграли')
            print('Ваш рекорд ' + str(db_m.record))
            break
