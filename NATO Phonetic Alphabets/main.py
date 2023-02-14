# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#

import pandas

alphabets_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(alphabets_df)


alphabets_dict = {}
for (index, row) in alphabets_df.iterrows():
    alphabets_dict[row.letter] = row.code

# print(alphabets_dict)

name = input("What's your name? ")

alphabets_list = [alphabets_dict[letter.title()] for letter in name if letter.title() in alphabets_dict.keys()]
print(alphabets_list)