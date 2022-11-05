word_list = input().split(' ')
sentence = ''

for word in word_list:
    print(sentence.count(word))
    sentence += word
