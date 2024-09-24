def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(file):
    with open(file) as f:
        return f.read()

main()