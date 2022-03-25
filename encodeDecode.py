alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt or 'decode' to decrypt\t")
text=input("Type you message\t").lower()
shift=int(input("Enter a shift number\t"))

#The better function for the challenge

def encode_decode(start_text, shift_amount, cipher_direction):
    end_text=""
    for letter in start_text:
        position=alphabets.index(letter)
        if cipher_direction=="encode":
            new_position=position+shift_amount
            end_text+=alphabets[new_position]
        elif cipher_direction=="decode":
            new_position=position-shift_amount
            end_text+=alphabets[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

encode_decode(text, shift, direction)


#A simple code for the challenge
    


# def encrypt(plain_text,shift_amount):
#     encrypted_text=""
#     for letter in plain_text:
#         position=alphabets.index(letter)
#         new_position=position+shift_amount
#         new_letter=alphabets[new_position]
#         encrypted_text+=new_letter

#     print(f"The encode text is {encrypted_text}")

# if direction=="encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction=="decode":
   

#     def decrypt(cipher_text, shift_amount):
#         decrypted_text=""
#         for letter in cipher_text:
#             position=alphabets.index(letter)
#             new_position=position-shift_amount
#             new_letter=alphabets[new_position]
#             decrypted_text+=new_letter

#         print(f"The decoded text is {decrypted_text}")
#     decrypt(cipher_text=text, shift_amount=shift)






