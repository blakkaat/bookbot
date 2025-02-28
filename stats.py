def get_word_total(text):
    words = text.split()
    return len(words)

def get_character_total(text):
    characters = {}

    for char in text:
        lowered_char = char.lower()
        if lowered_char not in characters:
            characters[lowered_char] = 1
        else:
            characters[lowered_char] += 1
    return characters

def sort(dict):
    return dict["num"]


def sort_characters(characters):
    list = []

    for char in characters:
        if char.isalpha():
            dict = {
                "char": char,
                "num": characters[char]
            }
            list.append(dict)

    list.sort(reverse=True, key=sort)

    return list