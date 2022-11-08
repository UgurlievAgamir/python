word = input()
left_word = word[len(word) // 2 + len(word) % 2:]
right_word = word[: len(word) // 2 + len(word) % 2]

print(left_word + right_word)
