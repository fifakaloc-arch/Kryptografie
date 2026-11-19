#3. - 6. úkol (13. 10. 2026)
#Naprogramujte šifrovací a dešifrovací funkci pro klasické šifry: substituční

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26

# KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"

def substitution_encryption(msg, key_alphabet):
    """Returns encrypted msg."""
    encrypted_msg = ""

    for symbol in msg:
        position = ALPHABET.find(symbol)

        if position == -1:
            raise ValueError("Message contains non-English letters.")

        encrypted_msg += key_alphabet[position]

    return encrypted_msg

def substitution_decryption(msg, key_alphabet):
    """Retursn decrypted msg that was inputed."""
    decrypted_msg = ""

    for symbol in msg:
        position = key_alphabet.find(symbol)

        if position == -1:
            raise ValueError("Message contains non-English letters.")

        decrypted_msg += ALPHABET[position]

    return decrypted_msg

if __name__ == "__main__":

    user_input_msg = input("Message to encrypt: ")
    msg = user_input_msg.upper().replace(" ", "")

    user_input_key_alphabet = input("Input the key alphabet (sequence of letters, small/big doesnt matter, spaces allowed): ")
    key_alphabet = user_input_key_alphabet.upper().replace(" ", "")

    if len(key_alphabet) > ALPHABET_LENGTH:
        raise ValueError("Alphabet has too many letters it needs to have 26.")
    elif len(key_alphabet) < ALPHABET_LENGTH:
        raise ValueError("Alphabet has too few letters it needs to have 26")

    if len(key_alphabet) != ALPHABET_LENGTH or set(key_alphabet) != set(ALPHABET):
        raise ValueError("Key must contain every English letter exactly once.")

    print(f"\n {user_input_msg}")

    encrypted_msg = substitution_encryption(msg, key_alphabet)
    print(f"\n {encrypted_msg}")

    dercrypted_msg = substitution_decryption(encrypted_msg, key_alphabet)
    print(f"\n {dercrypted_msg}")