word = input()

if len(word) % 2 != 0:
    left_word = word[:len(word) // 2]
    right_word = word[len(word) // 2:]

    left_word += word[(len(word) - 1) // 2]

print(right_word + left_word)
