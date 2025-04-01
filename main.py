from stats import count_words
from stats import count_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


    
def main(file_path="books/frankenstein.txt"):
    num_words = count_words(get_book_text(file_path))
    char_nums = count_char(get_book_text(file_path))
    print(f"{num_words} words found in the document")
    print(char_nums)



main()
    
    