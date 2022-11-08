word = input()

word_formatted = word[:word.find('h')]
word_formatted += word[word.rfind('h')+1:]

print(word_formatted)