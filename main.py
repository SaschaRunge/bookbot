def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    return None

def get_word_count(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")

main()