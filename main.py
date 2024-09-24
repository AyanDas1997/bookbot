def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    new_char_dict = char_count(text)
    print(new_char_dict)

def get_book_text(file):
    with open(file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main()