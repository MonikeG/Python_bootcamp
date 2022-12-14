
from hangman_words import word_list

import random

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

#print(chosen_word)

lives = 6

from hangman_art import logo, stages
print(logo)

display = []

for letter in chosen_word:
   
    display += "_"
    

print(display)


end_game = False


while not end_game:
    
    guess = input("Make a guess: ").lower()

    if guess in display:
      print(f"You already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

   
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose!")

        print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print('You Win')
 

        
    print(stages[lives])







