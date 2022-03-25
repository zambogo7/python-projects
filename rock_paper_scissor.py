import random
print("This is a rock, paper and scissor game")
rock='''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissor='''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper='''
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

game_images=[rock,paper,scissor]

gamer_choice=int(input("input your choice. Type '0' for rock '1' for paper and '2' for scissor\n"))
print(game_images[gamer_choice])
computer_choice=random.randint(0,2)
print("computer chose:\n")
print(game_images[computer_choice])
if gamer_choice>=3 or gamer_choice<0:
    print("You typed an invalid number, you loose!")
elif gamer_choice==computer_choice:
    print("Draw")
elif gamer_choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice==0 and gamer_choice==2:
 print("you loose")
elif computer_choice > gamer_choice:
    print("you loose!")
elif gamer_choice>computer_choice:
    print("you win!")



