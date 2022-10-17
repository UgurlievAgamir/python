string = input()

print(string[2])
print(string[len(string) - 1])

string_1 = ""
for i in range(0, 5):
    string_1 += string[i]

print(string_1)

string_2 = ""
for i in range(0, len(string) - 2):
    string_2 += string[i]

