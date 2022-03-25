import random
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
''')



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
========='''
]



#Generate a word
word_list=["zedekiah","joseph", "carol"]
#Choose the word randomly
chosen_word=random.choice(word_list)
#get the length of the word
word_length=len(chosen_word)


#set the lives to 6 that is no. of lives in ascii art
lives=6
#generate an empty list with the blank spaces equal to no. of letters in the choosen word
display=[]
for letter in chosen_word:
    display.append("_")
   

end_of_the_game=False
while not end_of_the_game:
 #Allow the user to guess any letter in the word
    guess=input("Guess a letter\t")
    if guess in display:
      print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            # replace the given letter with blank spaces 
            display[position]=letter

    if guess not in chosen_word:
        print(f"You gussed {guess}, which is not in the chosen word. You loose a life")
        lives-=1
        if lives==0:
            end_of_the_game=True
            print("You loose")

   
    #print(display)
    if "_"not in display:
        end_of_the_game=True
        print("you win")
    print(stages[lives])  
  
print(f"The choosen word is {chosen_word}")








