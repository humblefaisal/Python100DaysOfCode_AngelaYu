import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_codes = {row.letter:row.code for (index,row) in nato_data.iterrows() }
def generate_nato():
    # print(nato_codes)
    name = input("Input your string : ").upper()
    try :
        nato_op = [nato_codes[letter] for letter in name]
    except KeyError:
        print("Sry, only letters")
        generate_nato()
    else :
        print(nato_op)

generate_nato()
