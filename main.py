from stats import get_num_words, get_chars_dict

def main():
    book_path = "books/frankenstein.txt"
    txt = get_book_txt(book_path)
    num_words = get_num_words(txt)
    chars_dict = get_chars_dict(txt)
    print(f"{num_words} words found in the document")
    print(chars_dict)

def get_book_txt(path):
    with open(path) as f:
        return f.read()

main()
