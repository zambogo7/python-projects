import random
print("password generator")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['~','`','!','@','#','$','%','^','&','*','(',')','-','+',':',';','|','/',',','.',',','>','?']
print("Welcome to the paswors generator")

nr_letters=int(input("How many letter would you like your password to have?\n"))
nr_numbers=int(input("How many numbers would you like"))
nr_symbols=int(input("How many symbols would you like"))

#the easiest way but hackable

password=""
for char in range(1, nr_numbers+1):
    password+=random.choice(letters)
for char in range(1,nr_numbers):
    password+=random.choice(numbers)
for char in range(1,nr_symbols):
    password+=random.choice(symbols)
print (password)

#the hard way but unhackable
password_list=[]
for char in range(1, nr_numbers+1):
    password_list.append(random.choice(letters))
for char in range(1,nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(1,nr_symbols):
    password_list.append(random.choice(symbols))
#print (password)

#randomise the password by using shuffle

random.shuffle(password_list)

#turn a list to a string
password1=""
for char in password_list:
    password1+=char
print(password1)
