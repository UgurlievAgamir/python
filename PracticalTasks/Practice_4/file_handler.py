def read_file(file_name):
    output_text = {}
    with open(file_name, encoding='UTF-8') as file:
        words_list = file.read().split(' ')

    for i in range(0, len(words_list)):
        words_list[i] = words_list[i].lower()
        words_list[i] = "".join(a for a in words_list[i] if a.isalpha())

    for word in words_list:
        if word == '' or len(word) == 1:
            words_list.remove(word)

    output_text = set(words_list)

    return list(output_text)


def write_file(file_name, words_list):
    words_list = sorted(words_list)
    with open(file_name, encoding='UTF-8', mode='w') as file:
        file.write('Всего уникальных слов: ' + str(len(words_list)))
        file.write('\n======================\n')
        file.write('\n'.join(words_list))
