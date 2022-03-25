#a program that print c hecks for a prime numbers

#n=int(input("Enter any  number to check whether it is prime or not\t"))
def prime_number_checker(num):
    is_prime=True
    for i in range(2,num-1):
        if num%i==0:
            is_prime=False
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

    
prime_number_checker(list(range(1,101)))