def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    char_dict = char_count(text)
    sorted_list = sorted_char(char_dict)
    new_report = report(count,sorted_list)
    return(new_report)

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

def sorted_char(char_dict):
    list_char = [{"char":char, "count":count} for char, count in char_dict.items()]
    sorted_char = sorted(list_char,key = lambda x: x["count"], reverse=True)
    return sorted_char


def report(count, sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document/n")
    for item in sorted_list:
        if item['char'].isalpha() == True:
            print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")



main()