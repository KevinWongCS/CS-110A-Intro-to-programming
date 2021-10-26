# An acronym is a word formed from the initial letters of words in a set phrase.
# Write a program whose input is a phrase and whose output is an acronym of the input. If a
# word begins with a lower case letter, don't include that letter in the acronym. Assume there
# will be at least one upper case letter in the input.
#
# Ex: If the input is:
#
# Institute of Electrical and Electronics Engineers
#
# the output is:
#
# IEEE
#

def acronym_creator(string):
    new_string = ''
    new_string_2 = ''
    string_list = string.split()
    for word in string_list:
        # puts first letter of words into string
        new_string += word[0]
        # print(new_string)
    for word in new_string:
        # strips lower case characters
        if word.isupper() == True:
            new_string_2 += word
        else:
            continue
    print(new_string_2)

if __name__ == "__main__":
    user_input = str(input())
    acronym_creator(user_input)