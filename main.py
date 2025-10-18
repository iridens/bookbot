
import sys
from stats import get_total_words, get_word_repetitions, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookpath = sys.argv[1]
    #bookpath = "books/frankenstein.txt"
        book_text = get_book_text(bookpath)
        dict_list = sort_dictionary(get_word_repetitions(book_text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookpath}")
        print("----------- Word Count ----------")
        print(f"Found {get_total_words(book_text)} total words")
        print("--------- Character Count -------")
        for dictionary in dict_list:
            print(f"{dictionary['char']}: {dictionary['num']}")
        print("============= END ===============")
main()
