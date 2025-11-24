def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 0
        char_count[char.lower()] += 1
    return char_count

def sort_on(items):
    return items["num"]

def get_sorted_char_count(char_count):
    sorted_char_count = []

    for char in char_count:
        sorted_char_count.append({"char": char, "num": char_count[char]})

    sorted_char_count.sort(reverse=True, key=sort_on)

    return sorted_char_count





    