from stats import get_word_count
from stats import get_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    return None

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    print(f"Found {word_count} total words", char_count)

main()