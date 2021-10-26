# (1) Prompt the user to enter a string of their choosing. Store the text in a string. Output the string. (1 pt)
#
# Ex:
#
# Enter a sample text:
# we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes,
# more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!
#
# You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews
# and,  yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and
# our journeys continue!
#
#
# (2) Implement the print_menu() function to print the following command menu. (1 pt)
#
# Ex:
#
# MENU
# c - Number of non-whitespace characters
# w - Number of words
# f - Fix capitalization
# r - Replace punctuation
# s - Shorten spaces
# q - Quit
#
#
# (3) Implement the execute_menu() function that takes 2 parameters: a character representing the user's
# choice and the user provided sample text. execute_menu() performs the menu options, according to the user's
# choice, by calling the appropriate functions described below. (1 pt)
#
#
# (4) In the main program, call print_menu() and prompt for the user's choice of menu options for analyzing/editing
# the string. Each option is represented by a single character.
#
# If an invalid character is entered, continue to prompt for a valid choice. When a valid option is entered, execute
# the option by calling execute_menu(). Then, print the menu and prompt for a new option. Continue until the user
# enters 'q'. Hint: Implement Quit before implementing other options. (1 pt)
#
# Ex:
#
# MENU
# c - Number of non-whitespace characters
# w - Number of words
# f - Fix capitalization
# r - Replace punctuation
# s - Shorten spaces
# q - Quit
#
# Choose an option:
#
#
# (5) Implement the get_num_of_non_WS_characters() function. get_num_of_non_WS_characters() has a string
# parameter and returns the number of characters in the string, excluding all whitespace. Call
# get_num_of_non_WS_characters() in the execute_menu() function, and then output the returned value. (4 pts)
#
# Ex:
#
# Enter a sample text:
# we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,
# yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and
# our journeys continue!
#
# You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle
# crews and,  yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here;
# our hopes and our journeys continue!
#
# MENU
# c - Number of non-whitespace characters
# w - Number of words
# f - Fix capitalization
# r - Replace punctuation
# s - Shorten spaces
# q - Quit
#
# Choose an option:
# c
# Number of non-whitespace characters: 181
#
#
# (6) Implement the get_num_of_words() function. get_num_of_words() has a string parameter and returns
# the number of words in the string. Hint: Words end when a space is reached except for the last word in
# a sentence. Call get_num_of_words() in the execute_menu() function, and then output the returned value. (3 pts)
#
# Ex:
#
# Number of words: 35
#
#
# (7) Implement the fix_capitalization() function. fix_capitalization() has a string parameter and returns an
# updated string, where lowercase letters at the beginning of sentences are replaced with uppercase letters.
# fix_capitalization() also returns the number of letters that have been capitalized. Call fix_capitalization()
# in the execute_menu() function, and then output the number of letters capitalized followed by the edited string.
# Hint 1: Look up and use Python functions .islower() and .upper() to complete this task. Hint 2: Create an empty
# string and use string concatenation to make edits to the string. (3 pts)
#
# Ex:
#
# Number of letters capitalized: 3
# Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,
# yes;  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!
#
#
# (8) Implement the replace_punctuation() function. replace_punctuation() has a string parameter and two keyword
# argument parameters exclamation_count and semicolon_count. replace_punctuation() updates the string by replacing
# each exclamation point (!) character with a period (.) and each semicolon (;) character with a comma (,).
# replace_punctuation() also counts the number of times each character is replaced and outputs those counts. Lastly,
# replace_punctuation() returns the updated string. Call replace_punctuation() in the execute_menu() function, and
# then output the edited string. (3 pts)
#
# Ex:
#
# Punctuation replaced
# exclamation_count: 1
# semicolon_count: 2
# Edited text: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,
# yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here,  our hopes and our journeys continue.
#
#
# (9) Implement the shorten_space() function. shorten_space() has a string parameter and updates the string by
# replacing all sequences of 2 or more spaces with a single space. shorten_space() returns the string. Call
# shorten_space() in the execute_menu() function, and then output the edited string. Hint: Look up and use Python
# function .isspace(). (3 pt)
#
# Ex:
#
# Edited text: we'll continue our quest in space. there will be more shuttle flights and more shuttle crews and, yes,
# more volunteers, more civilians, more teachers in space. nothing ends here; our hopes and our journeys continue!
#

def repeater(sample_text):
    return sample_text

def print_menu():
    print("MENU\n\
c - Number of non-whitespace characters\n\
w - Number of words\n\
f - Fix capitalization\n\
r - Replace punctuation\n\
s - Shorten spaces\n\
q - Quit\n")

### EXECUTE MENU FUNCTION print_menu () repeated in each function to satisfy test ###
def execute_menu_2(user_choice, sample_text):
    if user_choice != 'q':
        if user_choice == 'c':
            print('Number of non-whitespace characters: {}\n'.format(get_num_of_non_WS_characters(sample_text)))
        if user_choice == 'w':
            # print('{:s}'.format(get_num_of_words(sample_text)))
            print('Number of words: {:d}\n'.format(get_num_of_words(sample_text)))
        if user_choice == 'f':
            letter_cap_counter, edited_sample_text = fix_capitalization_2(sample_text)
            print('Number of letters capitalized: {:d}'.format(letter_cap_counter))
            print('Edited text: {:s}\n'.format(edited_sample_text))
        if user_choice == 'r':
            edited_sample_text, exclamation_count, semicolon_count = replace_punctuation_2(sample_text)
            print('Punctuation replaced')
            print('exclamation_count: {:d}'.format(exclamation_count))
            print('semicolon_count: {:d}'.format(semicolon_count))
            print('Edited text: {:s}\n'.format(edited_sample_text))
        if user_choice == 's':
            print('Edited text: {:s}\n'.format(shorten_space(sample_text)))

        print_menu()
        print('Choose an option:')

### EXECUTE MENU / for unit test ###
def execute_menu(user_choice, sample_text):
    if user_choice != 'q':
        if user_choice == 'w':
            # print('{:s}'.format(get_num_of_words(sample_text)))
            print('Number of words: {:d}\n'.format(get_num_of_words(sample_text)))

### NUMBER OF NON-WHITE SPACE CHARACTERS ###
def get_num_of_non_WS_characters(sample_text):
    characters = 0
    for char in sample_text:
        if char != ' ':
            characters += 1
    return characters

### NUMBER OF WORDS / FOR UNIT TEST ###
def get_num_of_words(sample_text):
    num_words = int(len(sample_text.split()))
    # return ('Number of words: {:d}\n'.format(num_words))
    return num_words

### FIX CAPITALIZATION ####
def fix_capitalization_2(sample_text):
    capitalize = True
    letter_cap_counter = 0
    edited_sample_text = ''
    for char in sample_text:
        if capitalize == False:
            edited_sample_text += char
            if char == '.':
                capitalize = True
        elif char != ' ' and capitalize == True and char.islower():
            char = char.upper()
            edited_sample_text += char
            letter_cap_counter += 1
            capitalize = False
        else:
            edited_sample_text += char

    return letter_cap_counter, edited_sample_text

### FIX CAPITALIZATION / for unit test ###
def fix_capitalization(sample_text):
    capitalize = True
    letter_cap_counter = 0
    edited_sample_text = ''
    for char in sample_text:
        if capitalize == False:
            edited_sample_text += char
            if char == '.':
                capitalize = True
        elif char != ' ' and capitalize == True and char.islower():
            char = char.upper()
            edited_sample_text += char
            letter_cap_counter += 1
            capitalize = False
        else:
            edited_sample_text += char

    return edited_sample_text, letter_cap_counter

#### REPLACE PUNCTUATION ####
def replace_punctuation_2(sample_text, exclamation_count = 0, semicolon_count = 0):
    edited_sample_text = ''
    for char in sample_text:
        if char != '!' and char != ';':
            edited_sample_text += char
        if char == '!':
            edited_sample_text += '.'
            exclamation_count += 1
        if char == ';':
            edited_sample_text += ','
            semicolon_count += 1

    return edited_sample_text, exclamation_count, semicolon_count
#### REPLACE PUNCTUATION / for unit test
def replace_punctuation(sample_text, exclamation_count = 0, semicolon_count = 0):
    edited_sample_text = ''
    for char in sample_text:
        if char != '!' and char != ';':
            edited_sample_text += char
        if char == '!':
            edited_sample_text += '.'
            exclamation_count += 1
        if char == ';':
            edited_sample_text += ','
            semicolon_count += 1

    return edited_sample_text

#### SPACE CORRECTION ###
def shorten_space(sample_text):
    edited_sample_text = ''
    sample_text_list = sample_text.split()
    for word in sample_text_list:
        if word != sample_text_list[len(sample_text_list) - 1]:
            edited_sample_text += word + ' '
        elif word == sample_text_list[len(sample_text_list) - 1]:
            edited_sample_text += word
    return edited_sample_text



if __name__ == '__main__':
    sample_text = str(input('Enter a sample text:\n'))
    print('\nYou entered: {:s}\n'.format(repeater(sample_text)))
    print_menu()
    user_choice = str(input('Choose an option:\n'))
    execute_menu_2(user_choice, sample_text)


