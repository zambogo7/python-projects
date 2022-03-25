EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

#function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}.")

#make function to set difficulties
def set_difficulty():
    level=input("Choose the difficulty level. Type 'easy' or 'hard' ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #choosing a rom number between 1 and 100
    from random import randint
    print("Welcome to the guesing game")
    print("I am thinking of a number between 1 and 100")
    answer=randint(1,100)
    turns=set_difficulty()
     

    #Repeat the guesing
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess
        guess=int(input("Make a guess"))
        
        check_answer(guess,answer,turns)

game()
