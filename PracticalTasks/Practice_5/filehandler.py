def translate_to_list(file_name):
    try:
        file = open(file_name)
        count = int(file.readline())
        numbers_list = file.read().splitlines()

        if len(numbers_list) > count:
            raise Exception('Количество не совпадает')
        numbers_list = [int(numbers_list[i]) for i in range(0, count)]

        return numbers_list
    except FileNotFoundError:
        return 'Файл не найден. Проверьте правильность названия'
    except TypeError:
        return 'В файле не все элементы числа'
    except Exception as ex:
        return 'Ошибка обработки: ' + str(ex)
    finally:
        try:
            file.close()
        except:
            pass
