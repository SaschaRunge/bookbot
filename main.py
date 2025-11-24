import sys

from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    return None

def is_valid_call():
    if len(sys.argv) != 2:
        return False
    return True

def print_report(word_count, sorted_char_count, filepath_to_book):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")

    for char in sorted_char_count:
        if (char["char"].isalpha()):
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

def main():
    if not is_valid_call():
        print("Usage: python3 main.py <path_to_book>")
        return  
    
    filepath_to_book = sys.argv[1]

    book_text = get_book_text(filepath_to_book)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = get_sorted_char_count(char_count)
        
    print_report(word_count, sorted_char_count, filepath_to_book)

main()