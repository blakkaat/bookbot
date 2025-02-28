from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def display_list(list):
    for dict in list:
        print(f'{dict["char"]}: {dict["num"]}')

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    word_total = get_word_total(book)
    character_dictionary = get_character_total(book)
    list = sort_characters(character_dictionary)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...')
    print("----------- Word Count ----------")
    print(f'Found {word_total} total words')
    print("--------- Character Count -------")
    display_list(list)
    print("============= END ===============")



main()