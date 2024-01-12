import re
import secrets
import string

text = input('Enter a message to encrypt: ')

def generate_random_key(length = 10, lowercase = 10):
    # Define the possible characters for the key
    letters = string.ascii_letters

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(letters)

        constraints = [
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password

#Using random key for more secure encryption
custom_key = generate_random_key()

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

encryption = encrypt(text, custom_key)
print(f'\nEncrypted text: {encryption}\n')

question = input('Do you want to decrypt this message? Y or N: ')

if question == 'Y' :
    decryption = decrypt(encryption, custom_key)
    print(f'\nDecrypted text: {decryption}\n')
else:
    exit()