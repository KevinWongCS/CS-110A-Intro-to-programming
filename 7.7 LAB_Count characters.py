#
# 7.7 LAB: Count characters
#
# Write a program whose input is a string which contains a character and a phrase, and whose
# output indicates the number of times the character appears in the phrase.
#
# Ex: If the input is:
#
# n Monday
#
# the output is:
#
# 1
#
# Ex: If the input is:
#
# z Today is Monday
#
# the output is:
#
# 0
#
# Ex: If the input is:
#
# n It's a sunny day
#
# the output is:
#
# 2
#
# Case matters.
#
# Ex: If the input is:
#
# n Nobody
#
# the output is:
#
# 0
#
# n is different than N.

def string_creator(list):
    # joins elements of a list into a string
    string = ''
    for element in list:
        string = ' '.join(list)
    return string


def character_counter(character, string):
    # returns number of times character occurs in string
    character_count = string.count(character)
    return character_count


if __name__ == "__main__":
    user_string = str(input())
    # takes first letter in user_string and stores it in character
    user_list = user_string.split()
    character = user_list.pop(0)

    user_string_new = string_creator(user_list)

    print(character_counter(character, user_string_new))