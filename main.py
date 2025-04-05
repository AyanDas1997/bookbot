import sys

from stats import count_words

def main():
    if len(sys.argv)!= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = count_words(text)
    char_dict = char_count(text)
    sorted_list = sorted_char(char_dict)
    new_report = report(count,sorted_list)
    return(new_report)

def get_book_text(file):
    with open(file) as f:
        return f.read()

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
    print(f"--- Begin report of {sys.argv[1]} ---")
    print(f"{count} words found in the document/n")
    for item in sorted_list:
        if item['char'].isalpha() == True:
            print(f"{item['char']}: {item['count']}")
    print("--- End report ---")



main()