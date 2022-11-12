#Bootcamp_3

#lesson_1

print('Welcome to IBM calculator')

number = input("which number would you like to check? ")
number_int = int(number)
if number_int % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#lesson_2
#IMC 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

    #ou
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")

#height_float = float(height)
#weight_float = float(weight)

IMC_calc = (float(weight/(height**2)))
IMC =int(round (IMC_calc))

if IMC < 18.5:
    print (f"Your BMI is {IMC}and you are underweight")

elif IMC >= 18.5 and IMC < 25:
    print (f"Your BMI is {IMC}and you have a normal weight")

elif IMC >= 25 and  IMC < 30:
    print (f"Your BMI is {IMC}and you are slightly overweight")

elif IMC >= 30 and IMC <35:
    print (f"Your BMI is {IMC}and you are obese")
    
else:
    print (f"Your BMI is {IMC}and you are clinically obese")




