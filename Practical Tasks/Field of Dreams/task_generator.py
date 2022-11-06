import random

words_list = []
with open('database', encoding='UTF-8') as db:
    words_list = db.readlines()


def get_word():
    word = random.choice(words_list)
    words_list.remove(word)
    return word
