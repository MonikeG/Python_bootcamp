'''You need to write a function that checks whether if the number passed into it is a prime number or not.'''

def prime_checker(number):
    if number % 2 == 0:
        print("It's not a prime number.")
    elif number % 3 == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")



n = int(input("Check this number: "))
prime_checker(number=n)