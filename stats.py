# Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.

#     Convert any character to lowercase using the .lower() method, we don't want duplicates.
#     Use a dictionary of String -> Integer. The returned dictionary should look something like this:


def count_words(text):
    num_words = 0
    for word in text.split():
        num_words += 1
    return num_words

def count_char(text):
    char_count_dict = {}
    for char in text.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict
