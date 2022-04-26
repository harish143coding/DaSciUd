import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



raw_df = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in raw_df.iterrows()}



user_ip = input(f"enter a word :").upper()
new_lis_alphabets = [new_dict[x] for x in user_ip]
print(new_lis_alphabets)