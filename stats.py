



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

#     Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
#         Each dictionary should have two key-value pairs: one for the character itself and one for that character's count.
#         Sort from greatest to least by the count.
#         The .sort() method will be helpful here (see the hint).
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

def sort_dict(dictionar):
    dict_list = []
    for kv in dictionar:
        dict_list.append(kv)