def read_file(file_name):
    output_text = {}
    with open(file_name, encoding='UTF-8') as file:
        cache_list = file.read().split(' ')

    for i in range(0, len(cache_list)):
        cache_list[i] = cache_list[i].lower()

    output_text = set(cache_list)

    return output_text


def write_file(file_name):
    with open(file_name, encoding='UTF-8', mode='r+') as file:
        words_list = file.read().split(' ')

        for i in range(0, len(words_list)):
            words_list[i]