def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(count)

def get_book_text(file):
    with open(file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)



main()