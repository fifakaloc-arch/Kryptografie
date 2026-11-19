#3. - 6. úkol (13. 10. 2026)
#Naprogramujte šifrovací a dešifrovací funkci pro klasické šifry: Vigenèrovu

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26

def vigenere_encryption(msg, key):
    """Returns encrypted msg."""
    encrypted_msg = ""
    i = 0
    
    for symbol in msg:
        position = ALPHABET.find(symbol)

        if position == -1:
            raise ValueError("Message contains non-English letters.")

        encrypted_msg += ALPHABET[(position + ALPHABET.find(key[i % len(key)])) % ALPHABET_LENGTH]

        i +=1

    return encrypted_msg

def vigenere_decryption(msg, key):
    """Retursn decrypted msg that was inputed."""
    decrypted_msg = ""
    i = 0

    for symbol in msg:
        position = ALPHABET.find(symbol)

        if position == -1:
            raise ValueError("Message contains non-English letters.")

        decrypted_msg += ALPHABET[(position - ALPHABET.find(key[i % len(key)])) % ALPHABET_LENGTH]
        i += 1

    return decrypted_msg

if __name__ == "__main__":

    user_input_msg = input("Message to encrypt: ")
    msg = user_input_msg.upper().replace(" ", "")

    user_input_key = input("Enter the key that will be use to encrypt (string of letters of English aplhabet): ")
    key = user_input_key.upper().replace(" ", "")

    if len(key) == 0:
        raise ValueError("Key cannot be empty.")

    for symbol in key:
        if ALPHABET.find(symbol) == -1:
            raise ValueError("Key must contail letters from English alphabet.")

    print(f"\n {user_input_msg}")

    encrypted_msg = vigenere_encryption(msg, key)
    print(f"\n {encrypted_msg}")

    dercrypted_msg = vigenere_decryption(encrypted_msg, key)
    print(f"\n {dercrypted_msg}")