# Write a program that replaces words in a sentence. The input begins with word replacement
# pairs (original and replacement). The next line of input is the sentence where any word on
# the original list is replaced.
#
# Ex: If the input is:
#
# automobile car   manufacturer maker   children kids
# The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.
#
# the output is:
#
# The car maker recommends car seats for kids if the car doesn't already have one.
#
# You can assume the original words are unique.

def list_dictionary(list):
    # converts list into a dictionary
    dictionary = {}
    for word in list:
        if list.index(word) % 2 == 0:
            dictionary[word] = list[list.index(word) + 1]
    return dictionary

# working list to dictionary converter
# contact_list = {}
# for string in user_list:
#     if user_list.index(string) % 2 == 0:
#         contact_list[string] = user_list[user_list.index(string) + 1]

def word_replacer(dictionary, string):
    for key in dictionary:
        if key in string:
            string = string.replace(key, dictionary[key])
    return string


if __name__ == "__main__":
    user_string = input()
    user_sentence = input()
    user_string_2 = user_string.split()
    ### string method
    # phrase = phrase.replace('one', 'uno')
    #  list.count(x)

    user_words = list_dictionary(user_string_2)
    new_sentence = word_replacer(user_words, user_sentence)
    print(new_sentence)

