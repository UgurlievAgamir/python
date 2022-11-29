import re

# re.search(pattern, string)	Найти в строке string первую строчку, подходящую под шаблон pattern;


string = 'Телефон 123-12-12'
pattern = r'\d\d\D\d\d'

match = re.search(pattern, string)
print(match[0] if match else 'Not found')

string = 'Телефон 1231212'
pattern = r'\d\d\D\d\d'
match = re.search(pattern, string)
print(match[0] if match else 'Not found')


# re.fullmatch(pattern, string)	Проверить, подходит ли строка string под шаблон pattern;

string = '12-12'
pattern = r'\d\d\D\d\d'

match = re.fullmatch(pattern, string)
print('YES' if match else 'NO')

string = 'Т. 12-12'
pattern = r'\d\d\D\d\d'

match = re.fullmatch(pattern, string)
print('YES' if match else 'NO')


# re.split(pattern, string, maxsplit=0)	Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern;

string = 'Я помню чудное мгновенье'
pattern = r'\W+'

print(re.split(pattern, string))


# re.findall(pattern, string)	Возвращает список всех неперекрывающихся совпадений с шаблоном pattern в строке string,
# включая пустые совпадения. Если шаблон имеет группы, возвращает список фрагментов текста, совпавших с группами.
# Если в шаблоне присутствует более одной группы, каждый элемент в списке будет представлен кортежем, содержащим текст из каждой группы.

string = 'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'
pattern = r'\d\d\.\d\d\.\d{4}'

print(re.findall(pattern, string))


# re.sub(pattern, repl, string, count=0)	Заменить в строке string все непересекающиеся шаблоны pattern на repl;

string = 'Эта строка написана 20.11.2022, а могла бы и 22.11.2022'
pattern = r'\d\d\.\d\d\.\d{4}'

print(re.sub(pattern, r'DD.MM.YYYY', string))
