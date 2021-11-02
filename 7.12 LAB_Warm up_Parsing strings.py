# (1) Prompt the user for a string that contains two strings separated by a comma. (1 pt)
#
#     Examples of strings that can be accepted:
#         Jill, Allen
#         Jill , Allen
#         Jill,Allen
#
# Ex:
#
# Enter input string:
# Jill, Allen
#
#
# (2) Report an error if the input string does not contain a comma. Continue to prompt until a
# valid string is entered. Note: If the input contains a comma, then assume that the input also contains two strings. (2 pts)
#
# Ex:
#
# Enter input string:
# Jill Allen
# Error: No comma in string.
#
# Enter input string: Jill, Allen
#
#
# (3) Using string splitting, extract the two words from the input string and then remove any spaces. Output the two words. (2 pts)
#
# Ex:
#
# Enter input string:
# Jill, Allen
# First word: Jill
# Second word: Allen
#
#
# (4) Using a loop, extend the program to handle multiple lines of input. Continue until the user enters q to quit. (2 pts)
#
# Ex:
#
# Enter input string:
# Jill, Allen
# First word: Jill
# Second word: Allen
#
# Enter input string:
# Golden , Monkey
# First word: Golden
# Second word: Monkey
#
# Enter input string:
# Washington,DC
# First word: Washington
# Second word: DC
#
# Enter input string:
# q
#


def get_input():
    user_input = str(input('Enter input string:\n'))
    return user_input


def word_seperator(string):
    if ',' not in string:
        print('Error: No comma in string.\n')
    # remove ','
    else:
        string_list = string.split(',')
        # print('string_list', string_list)
        print('First word: {}'.format(string_list[0].strip()))
        print('Second word: {}\n'.format(string_list[1].strip()))


if __name__ == "__main__":
    user_input = get_input()
    while True:
        if user_input == 'q':
            break
        else:
            word_seperator(user_input)
            user_input = get_input()


