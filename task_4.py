#3. - 6. úkol (13. 10. 2026)
#Naprogramujte šifrovací a dešifrovací funkci pro klasické šifry: afinní

from math import gcd

# would use import but for convinience will put the entire function here
# from ukol2.task_2 import expanded_euklid_alg

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26

def expanded_euklid_alg(a, b):
    """Returns the greatest common devider and numbers x and y used to satify the eqution a * x + b * y == gcd(a, b)."""
    if b == 0:
        return a, 1, 0

    if a == 0:
        return b, 0, 1
    
    a0 = a
    b0 = b

    i = 0
    x = [1, 0]
    y = [0, 1]

    while b > 0:
        q = a // b
        r = a % b

        x.append(x[i] - q * x[i + 1])
        y.append(y[i] - q * y[i + 1])

        a, b = b, r
        i += 1

    return a, x[i], y[i]

def afinni_encryption(msg, key_a, key_b):
    """Returns encrypted msg."""
    encrypted_msg = ""

    for symbol in msg:
        temp_pos = ALPHABET.find(symbol)

        if temp_pos == -1:
            raise ValueError("Message contains non-English letters.")

        new_symbol_number = (key_a * temp_pos + key_b) % ALPHABET_LENGTH

        encrypted_msg += ALPHABET[new_symbol_number]

    return encrypted_msg  

def afinni_decryption(msg, key_a, key_b):
    """Retursn decrypted msg that was inputed."""
    decrypted_msg = ""

    # a_inv = pow(key_a, -1, 26)

    inv_key_a = expanded_euklid_alg(key_a, ALPHABET_LENGTH)[1] % ALPHABET_LENGTH

    for symbol in msg:
        temp_pos = ALPHABET.find(symbol)

        if temp_pos == -1:
            raise ValueError("Message contains non-English letters.")

        new_symbol_number = (temp_pos - key_b) * inv_key_a % ALPHABET_LENGTH

        decrypted_msg += ALPHABET[new_symbol_number]

    return decrypted_msg

if __name__ == "__main__":
    
    user_input_A = input("Key A for the cypher (number): ")
    user_input_B = input("Key B for the cypher (number): ")

    try:
        key_A = int(user_input_A)
        key_B = int(user_input_B)
    except ValueError:
        raise ValueError("Keys must be an integer.")

    if gcd(key_A, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")

    user_input_msg = input("Message to encrypt: ")
    msg = user_input_msg.upper().replace(" ", "")

    print(f"\n {user_input_msg}")

    encrypted_msg = afinni_encryption(msg, key_A, key_B)
    print(f"\n {encrypted_msg}")

    dercrypted_msg = afinni_decryption(encrypted_msg, key_A, key_B)
    print(f"\n {dercrypted_msg}")