
import random


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

heads_tails = random.randint(0, 1)

#print(heads_tails)

if heads_tails == 1:
    print ('Heads')
else:
    print('Tails')

print(---------------------------------------------------------------------------)

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print (names)

names_len = len(names)
print(names_len)


random_number = random.randint(0, (names_len - 1))
print(random_number)

random_name = names[random_number]
print(random_name)


print(f'{random_name} is going to buy the meal today!')