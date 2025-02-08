def caesar_encryption(msg, key=19):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encry_message = ""

    for c in msg:
        if c.isalpha(): 
            position = alphabet.find(c.lower())
            new_position = (position + key) % len(alphabet)
            new_character = alphabet[new_position]
            encry_message += new_character.upper() if c.isupper() else new_character
        else:
            encry_message += c  
    return encry_message

def caesar_decryption(msg, key=19):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decry_message = ""

    for c in msg:
        if c.isalpha(): 
            position = alphabet.find(c.lower())
            new_position = (position - key) % len(alphabet)
            new_character = alphabet[new_position]
            decry_message += new_character.upper() if c.isupper() else new_character
        else:
            decry_message += c  
    return decry_message

while True:
    message = input("Please enter a message (or 'q' to quit): ")
    if message.lower() == "q": break
    encry_message = caesar_encryption(message)
    decry_message = caesar_decryption(encry_message)
    print("Encrypted message: ", encry_message)
    print("Decrypted message: ", decry_message)
