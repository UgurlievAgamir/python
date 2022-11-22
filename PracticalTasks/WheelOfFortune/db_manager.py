import random

locked_symbol: str = '\u25A0'
heart_symbol: str = '\u2764'

current_session_record: int = 0
record: int = 0

with open("record_db", encoding='UTF-8') as r_db:
    record = int(r_db.read())

words_list: list = []
with open('words_db', encoding='UTF-8') as w_db:
    words_list = w_db.read().splitlines()


def get_random_word() -> str:
    """
    :return: случайное уникальное слово из базы данных слов
    """

    word: str = random.choice(words_list)
    words_list.remove(word)
    return word


def update_record() -> None:
    """
    Функция обновляет значение рекорда
    """
    with open('record_db', encoding='UTF-8', mode='w') as db:
        db.write(str(record))
