word = input()

if word.count('f') > 1:
    print(str(word.find('f')) + ' ' + str(word.rfind('f')))
elif word.count('f') == 1:
    print(word.find('f'))
else:
    print(-1)
