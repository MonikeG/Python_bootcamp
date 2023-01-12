
from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Refactoring

def cesar(plain_text, shift_number, cipher_direction):
    cipher = ""
    if cipher_direction == "decode":
        shift_number *= -1
    for i in plain_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_number
            cipher +=  alphabet[new_position]
        else:
            cipher += i
    
    
    print(f"The {cipher_direction}d text is: {cipher}") 


end_of_cipher = False

while not end_of_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift = shift % 26
    cesar (plain_text=text, shift_number=shift, cipher_direction=direction)
    
    restart = input('Would you like to continue? Type  "yes" or "no"')
    if restart == "no":
        end_of_cipher = True
        print("End of Encrypt")