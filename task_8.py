# 8. úkol (20. 10. 2026)
# Naprogramujte Kasiského test: program pro daný vstupní text vypíše řetězce délky nejméně 3, které mají v textu opakovaný výskyt, spolu se vzdálenostmi mezi těmito výskyty a seznamem dělitelů oněch vzdáleností.

# Nakonec můžete buď navrhnout několik vhodných kandidátů na délku klíče, nebo uživatele nechat, ať si kandidáty na základě vypsaných údajů určí sám.



def find_segnemts(text):
    """FUnction will go over the text and return dictionary with list of positions for each key that is present more then once."""

    current_segment_length = 3
    result_dict = {}
    
    while(current_segment_length <= len(text)):

        for i in range(len(text)) - current_segment_length:
            segment = text[i:i+current_segment_length]

            if segment not in result_dict:
                result_dict[segment] = []
            result_dict[segment].append(i)

        

        return



if __name__ == "__main__":
    print("hello")

