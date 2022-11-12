#100 days of python - project 2

print ('Welcome to the tipo calculator!')
total_bill = input ('What was the total bill? ')
percentage = input('What percentage tip would you like to give? Choose between 10, 12 or 15: ')
number_of_people = input('How many people to plit the bill? ')

total_bill_flt = float(total_bill)

percentage_int = int(percentage)/100

#print(type(percentage_int))

number_of_people_int = int(number_of_people)

total_payment = (total_bill_flt*percentage_int) + total_bill_flt

payment_person = total_payment/number_of_people_int

money = round(payment_person, 2)




print(f'Each pearson should pay: {money}')