# Implement the build_dictionary() function to build a word frequency dictionary from a list of words.
#
# Ex: If the words list is:
#
# ["hey", "hi", "Mark", "hi", "mark"]
#
# the dictionary returned from calling build_dictionary(words) is:
#
# {'hey': 1, 'hi': 2, 'Mark': 1, 'mark': 1}
#
# Ex: If the words list is:
#
# ["zyBooks", "now", "zyBooks", "later", "zyBooks", "forever"]
#
# the dictionary returned from calling build_dictionary(words) is:
#
# {'zyBooks': 3, 'now': 1, 'later': 1, 'forever': 1}
#
# The main code builds the word list from an input string, calls build_dictionary() to build the
# dictionary, and displays the dictionary sorted by key value.
#
# Ex: If the input is:
#
# hey hi Mark hi mark
#
# the output is:
#
# Mark: 1
# hey: 1
# hi: 2
# mark: 1
#

# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer
    # indicating that word's frequency.
    # words.count(word) returns the occurences of the word in list
    # my_dict[key] = value
    words_dictionary = {}
    for word in words:
        if word not in words_dictionary:
            words_dictionary[word] = words.count(word)
    return words_dictionary

# The following code asks for input, splits the input into a word list,
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))