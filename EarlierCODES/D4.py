import random
game = ["Rock","Paper","Scissors"]
choice = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors : "))
comp_choice = (random.randint(0,2))

if choice<=2 and choice>=0:
    print("computer choose : "+game[comp_choice])
    print("you choose : "+game[choice])

loose = comp_choice == ((choice+1)%3)
win = choice == ((comp_choice+1)%3)

if choice>2 or choice<0:
    print("Bhai khelne bhi nahi aata hai kya?")
elif loose:
    print("You Loose")
elif win:
    print("You win")
else :
    print("its a draw")