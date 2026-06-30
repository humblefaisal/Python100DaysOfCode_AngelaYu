import random
from os import system
cards = []
for i in range(2, 12):
    cards.extend([i]*4)
cards.extend([10]*12)

def calc_sum(cards):
    sum=0
    for val in cards:
        sum+=int(val)
    while sum>21 and cards.count(11)>0:
        cards[cards.index(11)]=1
        sum-=10
    return sum
def winner(a,b):
    """
    returns positive val for if a is winner negative for b and 0 for draw
    assumes that both sum is <=21
    """
    return a-b
    

while True:
    want_to_play = bool(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=='y')
    system("cls")
    if not want_to_play: break
    print("------xxx------")
    random.shuffle(cards)
    print(cards)
    print("Cards shuffling...")
    print("------xxx------")
    #Black jack logic
    i=0
    user_cards = []
    dealer_cards = []
    user_cards.append(cards[i]);i+=1;user_cards.append(cards[i]);i+=1
    user_sum = calc_sum(user_cards)
    dealer_cards.append(cards[i]);i+=1;dealer_cards.append(cards[i]);i+=1
    dealer_sum = calc_sum(dealer_cards)

    #user picks card as long as he wants to, or else sum>21
    print(f"dealer cards : _ {dealer_cards[1]}")
    while True:
        print(f"Your cards : {user_cards} , Sum = {user_sum}")
        if user_sum > 21 : break
        add_cards = bool(input("Do you want take more cards? Type 'y' or 'n': ").lower()=='y') 
        if not add_cards : break
        user_cards.append(cards[i]);i+=1
        user_sum = calc_sum(user_cards)
    if user_sum > 21 :
        print("Busted! You lost to the dealer!")
        continue
    while dealer_sum<17:
        print(f"dealer cards : {dealer_cards}")
        dealer_cards.append(cards[i]);i+=1
        dealer_sum = calc_sum(dealer_cards)
    
    print(f"dealer cards : {dealer_cards}")
    if dealer_sum > 21:
        print("You won to the dealer")
        continue
    match winner(user_sum,dealer_sum):
        case x if x>0:
            print("You are winner!")
        case x if x<0:
            print("Dealer won!")
        case 0:
            print("Draw!")


