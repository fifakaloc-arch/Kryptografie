# 8. úkol (20. 10. 2026)
# Naprogramujte Kasiského test: program pro daný vstupní text vypíše řetězce délky nejméně 3, které mají v textu opakovaný výskyt, spolu se vzdálenostmi mezi těmito výskyty a seznamem dělitelů oněch vzdáleností.

# Nakonec můžete buď navrhnout několik vhodných kandidátů na délku klíče, nebo uživatele nechat, ať si kandidáty na základě vypsaných údajů určí sám.

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def find_segnemts(text):
    """Function will go over the text and return dictionary with list of positions for each key that is present more then once."""

    current_segment_length = 3
    final_result_dict = {}
    while(current_segment_length <= len(text)):

        temp_result_dict = {}

        for i in range(len(text) - current_segment_length + 1):
            segment = text[i:i+current_segment_length]

            passing = False
            for symbol in segment:
                if symbol not in ALPHABET:
                    passing = True
                    break

            if passing:
                continue

            if segment not in temp_result_dict:
                temp_result_dict[segment] = []
            temp_result_dict[segment].append(i)
        
        temp_result_dict = cleaning_process(temp_result_dict)
        final_result_dict = merge_dictionaries(temp_result_dict, final_result_dict)

        current_segment_length += 1

    return final_result_dict

def merge_dictionaries(dictA, dictB):

    result = dict(dictA)

    for key in dictB:
        if key not in result:
            result[key] = dictB[key]
        else:
            result[key].extend(dictB[key])

    return result

def cleaning_process(dictionary):
    for key in list(dictionary.keys()):
        if len(dictionary[key]) < 2:
            del dictionary[key]
    return dictionary


def Kasiskeho_test(text):

    resulting_dict = {}

    position_dictionary = find_segnemts(text)

    for key, positions in position_dictionary.items():

        distances = []
        divisors = []

        for i in range(len(positions) - 1):
            distance = positions[i + 1] - positions[i]
            distances.append(distance)

        for distance in distances:

            temp_divisors = []

            for i in range(2, distance + 1):
                if distance % i == 0:
                    temp_divisors.append(i)

            divisors.append(temp_divisors)

        resulting_dict[key] = {
            "posi": positions,
            "dist": distances,
            "divi": divisors
        }

    return resulting_dict

if __name__ == "__main__":


    user_input_msg = input("Message to encrypt: ")
    msg = user_input_msg.upper().replace(" ", "")

    resulting_dict = Kasiskeho_test(msg)
    for segment, values in resulting_dict.items():
        print("Segment:", segment)
        print("Positions:", values["posi"])
        print("Distances:", values["dist"])
        print("Divisors:", values["divi"])
        print("-------------------------")