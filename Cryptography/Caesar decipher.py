def caesar_decrypt_bruteforce(encrypted_msg):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(1, 26):
        decrypted_message = ""
        
        for c in encrypted_msg:
            if c.isalpha():
                position = alphabet.find(c.lower())
                new_position = (position - key) % len(alphabet)
                new_character = alphabet[new_position]
                decrypted_message += new_character.upper() if c.isupper() else new_character
            else:
                decrypted_message += c 
        print(f"Key {key}: {decrypted_message}")
    print("\nReview the output to find the most readable message.")
encrypted_message = "iqfihhih"
caesar_decrypt_bruteforce(encrypted_message)