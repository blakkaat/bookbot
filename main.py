def main():
    with open("books/frankenstein.txt", "r") as file:
        content = file.read()
        words = count_words(content)
        character_dict = count_characters(content)
        sorted_character_dict = sort_character_dict(character_dict)
        print_report(file, words, sorted_character_dict)


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

def print_report(file, words, sorted_character_dict):
    print(f"--- Begin report for {file.name} ---")
    print(f"There are {words} words in the document.\n")
    for dict in sorted_character_dict:
        print(f"The '{dict['name']}' was found {dict['num']} times")

def sort_character_dict(character_dict):
    x = []
    for char in character_dict:
        if char.isalpha():
            x.append({'name': char, 'num': character_dict[char]})
        x.sort(reverse=True, key=sort_on)
    return x

def sort_on(sorted):
    return sorted["num"]

main()