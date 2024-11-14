def main():
    with open("books/frankenstein.txt", "r") as file:
        content = file.read()
        words = count_words(content)
        character_dict = count_characters(content)
        print(f"There are {words} words in the document.")
        print(character_dict)

def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    characters = {}
    for char in string:
        if char.lower() not in characters:
            characters[char.lower()] = 1
        else:
            characters[char.lower()] += 1
    return characters



main()