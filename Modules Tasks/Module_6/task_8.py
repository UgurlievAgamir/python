stroka = input()

print(stroka[2])
print(stroka[len(stroka) - 1])

for i in range(0, 5):
    print(stroka[i], end='')

print('\n')

for i in range(0, len(stroka) - 2):
    print(stroka[i], end='')

print('\n')

string_chet = ''
string_nechet = ''
for i in range(0, len(stroka)):
    if i % 2 == 0:
        string_chet += stroka[i]
    else:
        string_nechet += stroka[i]

print(string_chet)
print(string_nechet)

print(stroka[::-1])
print(stroka[::-2])
