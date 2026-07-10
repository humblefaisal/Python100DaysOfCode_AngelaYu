import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_codes = {row.letter:row.code for (index,row) in nato_data.iterrows() }
# print(nato_codes)
name = input("Input your string : ").upper()
nato_op = [nato_codes[letter] for letter in name]
print(nato_op)

