#Bootcamp_challenge
#Calculadora de ano bissexto
print('Welcome to leap yeap calculator')
year = int(input("Which year do you want to check? "))


if (year % 4) == 0:
    if (year % 4) == 0 and (year % 100) != 0:
        print("Leap year")
    elif (year % 100) == 0 and (year % 400) == 0:
        print ("Leap yeap")
    else:
        print("Not a Leap Year")
else:
    print ("Not a Leap Year")


    