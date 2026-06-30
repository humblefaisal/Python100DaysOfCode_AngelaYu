import random

print("welcome to password generator!\n")
num_letter = int(input("How many letters you would like in your password?"))
num_symbols = int(input("How many symbols you would like in your password?"))
num_digits = int(input("How many digits you would like in your password?"))

password = []

for i in range(0,num_letter):
    character_case = random.randint(0,1)
    letter = chr((1-character_case)*random.randint(65,90)+character_case*random.randint(97,122))
    password.append(letter) 
for i in range(0,num_symbols) :
    symbol = chr(random.randint(33,47))
    password.append(symbol)
for i in range(0,num_digits):
    number = chr(random.randint(48,57))
    password.append(number)
print(password)
for i in range(0,num_digits+num_letter+num_symbols) :
    index = random.randint(0,num_digits+num_letter+num_symbols-1)
    temp = password[i]
    password[i] = password[index]
    password[index] = temp
print(password)
random.shuffle(password)
print(password)
password_str = ""
for letter in password : 
    password_str+=letter
print("your password is : "+password_str)
 
    