# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
our_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}
print(our_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("enter a word: ")
phonetic_words = [our_dict[letter.upper()] for letter in user_input]
# phonetic_words = []
# for letter in user_input:
#     phonetic_words.append(our_dict[letter.upper()])

print(phonetic_words)




