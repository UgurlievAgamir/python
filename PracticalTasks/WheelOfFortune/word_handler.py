from db_manager import locked_symbol


def lock_word(word: str) -> str:
    """
    Зашифровывает слово
    :param word: не зашифрованное слово
    :return: зашифрованное слово
    """
    word_list: list = [a for a in word]
    output: str = ''

    for i in range(0, len(word)):
        word_list[i] = locked_symbol

    return output.join(word_list)


def unlock_part_of_word(unlocked_word: str, locked_word: str, part: str) -> str:
    """
    Открывает букву во всем слове
    :param unlocked_word: исходное незашифрованное слово
    :param locked_word: зашифрованное слово с возможными открытыми частями, если игрок их угадывал
    :param part: буква, которую нужно открыть во всем слове
    :return: слово в результате открытия буквы
    """
    all_part_indexes: list = []

    locked_word_list: list = [a for a in locked_word]
    output: str = ''

    for i in range(0, len(unlocked_word)):
        if unlocked_word[i] == part:
            all_part_indexes.append(i)

    for j in all_part_indexes:
        locked_word_list[j] = part

    return output.join(locked_word_list)
