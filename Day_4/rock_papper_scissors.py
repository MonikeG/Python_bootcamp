#rock_papper_scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random



choice = int(input("What do you choose? Type 0 for Paper, 1 for Scissors and 2 for Rock. "))


hand = random.randint(0, 2)


if choice == 0:
    print (paper)
    print(f'Computer chose {hand}:')

    if hand == 0:
        print (paper)
        print ("A Tie!")
    if hand == 1:
        print (rock)
        print ('You Win!')
    if hand == 2:
        print (scissors)
        print("You Lose!")
if choice == 1:
    print (scissors)
    print(f'Computer chose {hand}:')

    if hand == 0:
        print (paper)
        print ("You win!")
    if hand == 1:
        print (rock)
        print ('You Lose!')
    if hand == 2:
        print (scissors)
        print("A Tie!")
if choice == 2:
    print (rock)
    print(f'Computer chose {hand}:')

    if hand == 0:
        print (paper)
        print ("You Lose!")
    if hand == 1:
        print (rock)
        print ('A Tie!')
    if hand == 2:
        print (scissors)
        print("You win!")
if choice >= 3:
    print("You typed an invalid number.")

   