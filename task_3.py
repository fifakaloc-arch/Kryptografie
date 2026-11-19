#3. - 6. úkol (13. 10. 2026)
#Naprogramujte šifrovací a dešifrovací funkci pro klasické šifry: posuvnou

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26

def posuvna_encryption(msg, offset):
    """Returns encrypted msg."""
    encrypted_msg = ""

    for symbol in msg:
        temp_pos = ALPHABET.find(symbol)

        if temp_pos == -1:
            raise ValueError("Message contains non-English letters.")

        new_symbol_number = (temp_pos + offset) % ALPHABET_LENGTH

        encrypted_msg += ALPHABET[new_symbol_number]

    return encrypted_msg

def posuvna_decryption(msg, offset):
    """Retursn decrypted msg that was inputed."""
    decrypted_msg = ""

    for symbol in msg:
        temp_pos = ALPHABET.find(symbol)

        if temp_pos == -1:
            raise ValueError("Message contains non-English letters.")

        new_symbol_number = (temp_pos - offset) % ALPHABET_LENGTH

        decrypted_msg += ALPHABET[new_symbol_number]

    return decrypted_msg

if __name__ == "__main__":

    user_input = input("Offset for the cypher (number): ")

    try:
        offset = int(user_input)
    except ValueError:
        raise ValueError("Offset must be an integer.")

    user_input_msg = input("Message to encrypt: ")
    msg = user_input_msg.upper().replace(" ", "")

    print(f"\n {user_input_msg}")

    encrypted_msg = posuvna_encryption(msg, offset)
    print(f"\n {encrypted_msg}")

    dercrypted_msg = posuvna_decryption(encrypted_msg, offset)
    print(f"\n {dercrypted_msg}")