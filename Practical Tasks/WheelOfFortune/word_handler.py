from db_manager import locked_symbol


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
