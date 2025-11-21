import unicodedata


def convert_str_to_normalized(text: str) -> str:
    # replace spaces with underscores and convert to uppercase
    output_text = text.replace(" ", "_").upper()
    # remove accents
    output_normalized = unicodedata.normalize('NFD', output_text)
    output_str = ''.join(c for c in output_normalized if unicodedata.category(c) != 'Mn')
    
    return output_str

def convert_person_fullname_to_short(person_name: str) -> str:
    listed_person_name = person_name.split(" ")
    short_person_name = f"{listed_person_name[0]} {listed_person_name[2]}"
    
    return short_person_name