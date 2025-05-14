from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

continue_game = True

def caesar(cipher_text, shift_amount, direction_value):
    caesar_text = ''
        # if direction_value == "decode":       This skips the if conditions and makes it simpler.
        #    shift_amount *= -1                 Has to be out of the for loop in order to work properly.
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)    
            if direction_value == "encode":
                new_position = position + shift_amount
            elif direction_value == "decode":
                new_position = position - shift_amount
            caesar_text += alphabet[new_position]        
        else:
            caesar_text += char    
    print(f"The {direction_value}d text is: '{caesar_text}'.")

while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(cipher_text=text, shift_amount=shift, direction_value=direction)
    keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if keep_going == "yes":
        continue
    elif keep_going == "no":
        print("Program closing, thank you for your time!")
        continue_game = False
    else:
        print("Invalid command. Closing the program.")
        continue_game = False
    
# def encrypt(plain_text, shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     decipher_text = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         old_position = position - shift_amount
#         decipher_text += alphabet[old_position]
#     print(f"The decoded text is {decipher_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Invalid command.")