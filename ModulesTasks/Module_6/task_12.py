word = input()
f_index = word.find('h')
l_index = word.rfind('h')

word_list = [a for a in word.replace('h', 'H')]
word_list[f_index] = 'h'
word_list[l_index] = 'h'

word = ''
print(word.join(word_list))
