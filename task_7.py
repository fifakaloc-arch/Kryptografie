#Naprogramujte frekvenční analýzu: program pro daný vstupní text (řetězec nebo textový soubor) vypíše znaky anglické abecedy spolu s frekvencemi jejich výskytu v tomto textu. Ostatní znaky (např. mezery) jsou ignorovány.

#Dále naprogramujte verze, které takto vypíší dvojice, resp. trojice znaků s jejich frekvencemi výskytu (zde doporučuji vypsat pouze ty digramy a trigramy, které v textu mají výskyt).

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def analyze_single(text):
    """Returns dictionary filled with all 1 letter combinations and their amount."""
    result = {}

    for i in text:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
        
    return result

def analyze_double(text):
    """Returns dictionary filled with all 2 letter combinations and their amount."""
    result = {}

    if len(text) < 2:
        return result

    i = 1

    while i < len(text):
        double = text[i-1] + text[i]

        if double not in result:
            result[double] = 1
        else:
            result[double] += 1

        i += 1
        
    return result

def analyze_triple(text):
    """Returns dictionary filled with all 3 letter combinations and their amount."""
    result = {}

    if len(text) < 3:
        return result

    i = 2

    while i < len(text):
        triple = text[i-2] + text[i-1] + text[i]

        if triple not in result:
            result[triple] = 1
        else:
            result[triple] += 1

        i += 1
        
    return result

def remove_less_than(d_result, n, remove=False):
    """Removes keys whose amount is less than or equal to n. Edits the original dictionary if remove=True."""
    if remove:

        for key in list(d_result.keys()):
            if d_result[key] <= n:
                del d_result[key]

        return d_result
    else:
        # learned with AI didnt know you could do will not use
        # return result = {key: d_result[key] for key in d_result if d_result[key] > n}

        result = {}

        for key in d_result:
            if d_result[key] > n:
                result[key] = d_result[key]

        return result

def calculate_frequency(text_length, dictionary, setting):
    """Calculates frequency for each key in dictionary, setting represents for how many characters (1, 2, 3)."""
    if setting not in {1, 2, 3}:
        raise ValueError("Incorrect setting")
    
    n = text_length - setting + 1        

    if n <= 0:
        return {}

    result = {}

    for key in dictionary:
        result[key] = dictionary[key] / n

    return result

def get_text():
    """Returns text based on the chosen input method."""
    choice = input("Choose input type (1 - manual, 2 - file): ")

    if choice == "1":
        return input("Type the text: ")

    elif choice == "2":
        file_path = input("Enter file path: ")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        except FileNotFoundError:
            raise ValueError("File not found.")

    else:
        raise ValueError("Invalid choice.")

if __name__ == "__main__":

    text_user = get_text()

    text = "".join(char for char in text_user.upper() if char in ALPHABET)

    if len(text) == 0:
        raise ValueError("Can't analyze empty text.")

    single_result = analyze_single(text)
    single_freq = calculate_frequency(len(text), single_result, 1)
    print(remove_less_than(single_result, 0))
    print(single_freq)

    double_result = analyze_double(text)
    double_freq = calculate_frequency(len(text), double_result, 2)
    print(remove_less_than(double_result, 0))
    print(double_freq)

    triple_result = analyze_triple(text)
    triple_freq = calculate_frequency(len(text), triple_result, 3)
    print(remove_less_than(triple_result, 0))
    print(triple_freq)