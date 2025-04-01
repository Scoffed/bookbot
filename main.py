from stats import count_words
from stats import count_char
from stats import sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# print(char_nums)
#     Import and call the function in main.py, and capture the result.
#     Print the report to the console as shown above. If the character is not an alphabetical character (using the .isalpha() method), just skip it.



    
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
    
    #     Import and call the function in main.py, and capture the result.
#     Print the report to the console as shown above. If the character is not an alphabetical character (using the .isalpha() method), just skip it.

# Run and submit the CLI tests.
# Hint

# Here's an example of how you can use the .sort() method to sort a list of dictionaries:

# # A function that takes a dictionary and returns the value of the "num" key
# # This is how the `.sort()` method knows how to sort the list of dictionaries
# def sort_on(dict):
#     return dict["num"]

# vehicles = [
#     {"name": "car", "num": 7},
#     {"name": "plane", "num": 10},
#     {"name": "boat", "num": 2}
# ]
# vehicles.sort(reverse=True, key=sort_on)
# print(vehicles)
# # [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]