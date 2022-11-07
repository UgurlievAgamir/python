import random

current_session_record = 0
record = 0

with open('record_db', encoding='UTF-8') as db:
    record = int(db.read())

words_list = []
with open('words_db', encoding='UTF-8') as db:
    words_list = db.read().splitlines()


def get_random_word():
    word = random.choice(words_list)
    words_list.remove(word)
    return word


def update_record():
    with open('record_db', encoding='UTF-8', mode='w') as db:
        db.write(str(record))