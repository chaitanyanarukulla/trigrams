"""Generates a random story based on the text file with  word count"""
import random
import sys


def read_file(input_text):
    """Reads the inputted text file. and returns"""
    the_file = open(input_text, 'r')
    text = the_file.read()
    the_file.close()
    return text


def changes_text_into_dict(text):
    """Converts text into dictionary and returs key value
    pairs by stripping new lines and spliting at' '
    and  also checks if keys  exit if key already exit
    with same value it  appends new value."""
    dictionary = {}
    text = text.replace('\n', ' ')
    while len(text.split(" ")) > 2:
        split_text = text.split(" ", 3)
        keys = (split_text[0], split_text[1])
        value = split_text[2]
        if keys not in dictionary:
            dictionary[keys] = [value]
        else:
            new_value = dictionary.get(keys)
            new_value.append(value)
            dictionary[keys] = new_value
        length = len(split_text[0]) + 1
        text = text[length:]
    return dictionary


def generate_random_text(dictionary, new_sentence):  #no cover
    """generates random text with key from dictionary."""
    random_key = random.choice(list(dictionary.keys()))
    word_1 = str(random_key[0])
    word_2 = str(random_key[1])
    word_3 = random.choice(dictionary[random_key])
    new_sentence.extend([word_1, word_2, word_3])
    return new_sentence


def make_new_sentence(dictionary, stop):
    """Make a new sentences using random key value pairs
     from the dictionary."""
    new_sentence = []
    generate_random_text(dictionary, new_sentence)
    while len(new_sentence) < stop:
        rand_sentence = (new_sentence[-2], new_sentence[-1])
        if rand_sentence in dictionary:
            fetch_rand_sentence = random.choice(dictionary[rand_sentence])
            new_sentence.append(fetch_rand_sentence)
        else:
            generate_random_text(dictionary, new_sentence)
    return " ".join(new_sentence)


def main(path_of_file, stop):
    """calls all the functions that will change
    text.txt files and make new_sentence to create new story
    from __main__"""
    text = read_file(path_of_file)
    trigrams = changes_text_into_dict(text)
    new_story = make_new_sentence(trigrams, stop)
    print(new_story)
    sys.exit(0)


if __name__ == "__main__":
    path_of_file = sys.argv[1]
    stop = sys.argv[2]
    main(path_of_file, int(stop))
