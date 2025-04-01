import sys
from stats import count_words
from stats import count_char
from stats import sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

    
def main(file_path="books/frankenstein.txt"):
    num_words = count_words(get_book_text(file_path))
    char_nums = count_char(get_book_text(file_path))
    report = sort_dict(char_nums)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in report:
        character = char_dict["name"]
        count = char_dict["num"]
        print(f"{character}: {count}")



main()
