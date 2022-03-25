alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#function to apply the algorithm

def encode_decode(start_text, shift_amount, cipher_direction):
    #set end text to null so that you can apppend the result in it
    end_text=""
    #make a variable 'char' that will hold every charatecter in the start_text
    for char in start_text:
        #if the char is in the alphabets the do encoding and decoding
        if char in alphabets:
            #get the position of char
            position=alphabets.index(char)
            #for encoding
            if cipher_direction=="encode":
                #add the 1st position to the shift amount to get the new_position
                new_position=position+shift_amount
                #append the positions of alphabets into end_text
                end_text+=alphabets[new_position]
            #for decoding
            elif cipher_direction=="decode":
                #subtract the shift_amount from the position to get the new_position
                new_position=position-shift_amount
                #append the positioins of the alphabets into the end_text
                end_text+=alphabets[new_position]
        #if the char is not in the alphabets then append char into the end text
        else:
            end_text+=char
    #print the cipher direction and the end text
    print(f"The {cipher_direction}d text is {end_text}")


#run the program inifit time till the user type no
should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt or 'decode' to decrypt\t")
    text=input("Type you message\t").lower()
    shift=int(input("Enter a shift number\t"))
    shift=shift%26
    #call the fuction using the aguments
    encode_decode(text, shift, direction)

    user_choice=input("Type 'yes' to continue and 'no' to stop ")
    if user_choice=="no":
        should_continue=False
        print("goodbye")

