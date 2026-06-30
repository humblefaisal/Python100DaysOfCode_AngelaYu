import random
guess_num = random.randint(1,100)
chances=0
match input("Enter mode of difficulty ('easy' or 'hard'): ").lower():
    case 'easy':
        chances = 10
    case 'hard':
        chances=5
    case _ :
        chances=5
        print("Invalid input! defaults to easy..")

def compare(num):
    if num==guess_num:
        return (f"Right guess {guess_num}! You won",True)
    elif num>guess_num:
        return ("Too High!",False)
    return ("Too low!",False) 


while chances>0:
    print(f"Chanes left : {chances}")
    guess=int(input("Enter your guess : "))
    response = compare(guess)
    print(response[0])
    if response[1] : break
    chances-=1
if chances==0:
    print(f"You are out of chances! The number was : {guess_num}")
