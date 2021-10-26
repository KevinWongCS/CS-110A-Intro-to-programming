#
# 7.9 LAB: Palindrome
#
# A palindrome is a word or a phrase that is the same when read both forward and backward.
# Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose
# input is a word or phrase, and that outputs whether the input is a palindrome.
#
# Ex: If the input is:
#
# bob
#
# the output is:
#
# bob is a palindrome
#
# Ex: If the input is:
#
# bobby
#
# the output is:
#
# bobby is not a palindrome
#
# Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

# for letter in 'daniel':
#     print(letter)
# #works
def is_palindrome(user_string):
    # determines if string is a palindrome, ignoring whitespaces
    palindrome = True
    index = 1
    new_string = '' # string used to compare user_string against
    # removes white spaces from string
    for letter in user_string:
        if letter == ' ':
            continue
        else:
            new_string += letter
    # compares first letter to last letter and increments inwards
    # breaks when letters aren't equal
    for letter in new_string:
        if letter == new_string[len(new_string) - index]:
            palindrome = True
        else:
            palindrome = False
            break
        index += 1
    # print statement
    if palindrome == False:
        print("{} is not a palindrome".format(user_string))
    else:
        print("{} is a palindrome".format(user_string))


if __name__ == "__main__":
    user_string = str(input())
    is_palindrome(user_string)