def main():
    with open("books/frankenstein.txt", "r") as file:
        content = file.read()
        words = count_words(content)
        print(f"There are {words} words in the document.")

def count_words(string):
    words = string.split()
    return len(words)

main()