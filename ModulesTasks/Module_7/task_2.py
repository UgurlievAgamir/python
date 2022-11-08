dict = {}
reversed_dict = {}

sin_count = int(input())

for i in range(0, sin_count):
    key, sin_word = input().split()
    dict[key] = sin_word

word = input()

for key, item in dict.items():
    reversed_dict[item] = reversed_dict.get(item, []) + [key]

print(reversed_dict.get(word))
