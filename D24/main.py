#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import re

with open("./Input/Letters/starting_letter.txt",mode="r") as letter_template_file:
    with open("./Input/Names/invited_names.txt",mode="r") as names:
        letter_template = letter_template_file.read()
        for line in names.readlines():
            name = line.rstrip("\n")
            letter = letter_template.replace("[name]",name)
            filename = f"./Output/ReadyToSend/{name}_letter"
            with open(filename,mode="w") as op_letter:
                op_letter.write(letter)
                
        


# test = "this is a [test] [name]"
# m = re.search(pattern = "name",string=test)
# print(m)