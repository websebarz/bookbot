import sys

from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    txt = get_book_txt(sys.argv[1])
    num_words = get_num_words(txt)
    chars_dict = get_chars_dict(txt)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(sys.argv[1], num_words, chars_sorted_list)

def get_book_txt(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

main()
