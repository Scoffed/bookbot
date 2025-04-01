from stats import count_words
from stats import count_char
from stats import sort_dicts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


    
def main(file_path="books/frankenstein.txt"):
    num_words = count_words(get_book_text(file_path))
    char_nums = count_char(get_book_text(file_path))
    report = sort_dicts(char_nums)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(report.isalpha())
    # print(char_nums)

#     Import and call the function in main.py, and capture the result.
#     Print the report to the console as shown above. If the character is not an alphabetical character (using the .isalpha() method), just skip it.


main()
    
    