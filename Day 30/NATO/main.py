# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# A dictionary in this format
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.

# My solution #

# while True:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print(f"Sorry, only letters in the alphabet please.")
#     else:
#         print(output_list)
#         break

# A Recursive solution #

def nato():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print(f"Sorry, only letters in the alphabet please.")
        nato()
    else:
        print(output_list)

nato()
