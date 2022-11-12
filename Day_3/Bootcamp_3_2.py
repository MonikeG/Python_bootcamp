
print("Welcome to Python Pizza Deliveries!")
print('Here you can calculate your pizza price')
price = 0

size = input("What size pizza do you want? S, M, or L ")
if size == 'S':
    price = 15
    print ('Small Pizza: $15')
elif size == 'M':
    price = 20
    print ('Medium Pizza: $20')
else:
    price = 25
    print('Large Pizza: $25')

add_pepperoni = input("Do you want pepperoni? Y or N ")

if add_pepperoni == 'Y':   
    if size == 'S':
        price += 2
        print ('Pepperoni for Small Pizza: +$2')
    if size == 'M':
        price += 3
        print ('Pepperoni for Medium or Large Pizza: +$3')
    if size == 'L':
        price += 3
        print ('Pepperoni for Medium or Large Pizza: +$3')
else:
    print ('No pepperoni')

extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == 'Y':
    price += 1
    print ('Extra cheese for any size pizza: + $1')
else:
    print("No extra cheese")

print (f'Your final bill is: ${price}')
