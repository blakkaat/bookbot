from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def display_list(list):
    for dict in list:
        print(f'{dict["char"]}: {dict["num"]}')

def main():
    book = get_book_text("books/frankenstein.txt")
    word_total = get_word_total(book)
    character_dictionary = get_character_total(book)
    list = sort_characters(character_dictionary)

    print("============ BOOKBOT ============")
    print('Analyzing book found at books/frankenstein.txt...')
    print("----------- Word Count ----------")
    print(f'Found {word_total} total words')
    print("--------- Character Count -------")
    display_list(list)
    print("============= END ===============")



main()