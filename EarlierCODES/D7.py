import random
word_list = ["hello","bike","rope","winning","hangman"]
random.seed(0)
word = random.choice(word_list)
guess = '_'*len(word)
life = 10
while life > 0 :
    print(guess)
    ch = (input(f"Guess the Letter in the word ({life}/10 lives):"))[0]
    if not ch:
        continue
    correct_guess=False
    for i in range(len(word)):
        if word[i].lower() == ch.lower():
            guess = guess[:i]+ch.lower()+guess[i+1:]
            correct_guess = True
    if guess == word:
        print("congrats! You guessed the word : ",guess)
        break
    if correct_guess:
        print("Your guess was correct!")
    else :
        print("Incorrect Guess!")
        life-=1
if(life==0):
    print("You lost all your lives! correct word was : ",word)
