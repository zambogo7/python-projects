print('''       
******************************************************

                  Y\     /Y
                              | \ _ / |
        _____                 | =(_)= |
    ,-~"     "~-.           ,-~\/^ ^\/~-.
  ,^ ___     ___ ^.       ,^ ___     ___ ^.
 / .^   ^. .^   ^. \     / .^   ^. .^   ^. \
Y  l    O! l    O!  Y   Y  lo    ! lo    !  Y
l_ `.___.' `.___.' _[   l_ `.___.' `.___.' _[
l^~"-------------"~^I   l^~"-------------"~^I
!\,               ,/!   !                   !
 \ ~-.,_______,.-~ /     \                 /
  ^.             .^       ^.             .^    
    "-.._____.,-"           "-.._____.,-"

*******************************************************               
               
               ''')

print("        Welcome to Tressure island \n Your mission is to find the tressure")
choice1=input('Choose your direction, do you want to go to left or right. Type "left" or "right\n"').lower()
if choice1=="left":
    choice2=input('You\'ve reached at a river type "swim" or "wait" to continue \n').lower()
    if choice2=="wait":
        choice3=input('Enter the door and choose your color. Type "blue" or "yellow" or "red"\n').lower()
        if choice3=="blue":
            print("You have entered a room of fire. Game over!")
        elif choice3=="yellow":
            print("You have been awarded your tressure. You win!")
        elif choice3=="red":
            print("You have entered a room of lion. Game over!")
        else:
            print("Invalid choice. Game over!")
    else:
        print("You\'ve been eaten by wild animals leaving in water.Game over")
    
else:
    print("You have fallen into a deep. Game over")

