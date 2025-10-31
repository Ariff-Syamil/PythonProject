# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# for (index,row) in data.iterrows():
#     data_dict.update({row.letter: row.code})

# letter = [letter for letter in word]
# nato_phonetic_alphabet = []
# for alphabet in letter:
#     for (key,value) in data_dict.items():
#         if alphabet == key:
#             nato_phonetic_alphabet.append(value)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato_alphabet():
    word = input("What is the word? \n").upper()
    try:
        nato_phonetic_alphabet = [data_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only letter.")
        nato_alphabet()
    else:
        print(nato_phonetic_alphabet)

nato_alphabet()