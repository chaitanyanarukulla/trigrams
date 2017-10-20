"""This module reads a file then converts into text and uses to predictive text to write random stuff"""
def read_file(input_text):
    """Reads the inputted text file."""
    the_file = open(input_text, 'r')
    data = the_file.read()
    the_file.close()
    return data


def change_string_text_to_list(string_item):
    """Take a single string(text), and returns a list of its words"""
    string_of_words = "I wish I may I wish I might"
    list_of_words = string_of_words.split()
    for index, item in enumerate(list_of_words):
        key_value = {}
        if index < len(list_of_words) - 2:
            dic_key = list_of_words[index] + " " + list_of_words[index + 1]
            if dic_key in key_value:
                key_value[dic_key].append(list_of_words[index + 2])
            else:
                key_value[dic_key] = [list_of_words[index + 2]]
                print(key_value)


change_string_text_to_list(read_file('text.txt'))
