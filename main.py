def main():
    with open("books/frankenstein.txt", "r") as file:
        content = file.read()
        words = count_words(content)
        character_dict = count_characters(content)
        print_report(file, words, character_dict)

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

def print_report(file, words, character_dict):
    print(f"--- Begin report for {file.name} ---")
    print(f"There are {words} words in the document.\n")

    for char in character_dict:
        if char != '\n':
            print(f"The '{char}' character was found {character_dict[char]} times")


main()