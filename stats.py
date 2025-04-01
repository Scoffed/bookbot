def count_words(text):
    num_words = 0
    for word in text.split():
        num_words += 1
    return num_words

def count_char(text):
    char_count_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    return char_count_dict

def sort_on(dict):
        return dict["num"]
    
def sort_dict(dictionar):
    dict_list = []

    for kv in dictionar:
        dict_char = {}
        dict_char["name"] = kv
        dict_char["num"] = dictionar[kv]
        dict_list.append(dict_char)
        
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list