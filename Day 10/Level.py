word = input("What's the word?: ")
second_word = ""
word_list = list(word)
second_list = []

for character in word_list:
    second_list.insert(0, character)

if word_list == second_list:
    print("\nYes, it's the same if you reverse it")
else:
    print("\nNo, it won't be the same")

print(word)

for letter in second_list:
    second_word += letter
print(second_word)
