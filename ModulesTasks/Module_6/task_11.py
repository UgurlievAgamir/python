word = input()

word_formatted = word[:word.find('h')]
word_formatted += word[word.find('h')+1:word.rfind('h')+1][::-1]
word_formatted += word[word.rfind('h'):]

print(word_formatted)