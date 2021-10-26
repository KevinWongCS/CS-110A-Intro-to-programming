# Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing
# the integer in binary. For an integer x, the algorithm is:
#
# As long as x is greater than 0
#    Output x % 2 (remainder is either 0 or 1)
#    x = x // 2
#
# Note: The above algorithm outputs the 0's and 1's in reverse order. You will need to write a second function
# to reverse the string.
#
# Ex: If the input is:
#
# 6
#
# the output is:
#
# 110
#
# Your program must define and call the following two functions. The function integer_to_reverse_binary()
# should return a string of 1's and 0's representing the integer in binary (in reverse). The function reverse_string()
# should return a string representing the input string in reverse.
# def integer_to_reverse_binary(integer_value)
# def reverse_string(input_string)

def integer_to_reverse_binary(integer_value):
    reverse_binary = ''
    while integer_value > 1:
        reverse_binary += str(integer_value % 2)
        integer_value = integer_value // 2
    if integer_value == 1:
        reverse_binary += str(integer_value % 2)
    return reverse_binary

def reverse_string(input_string):
    reverse_input_string = ''
    for i in range(len(input_string)):
        reverse_input_string += input_string[len(input_string) - i -1]
    return reverse_input_string

if __name__ == '__main__':
    integer_value = int(input())
    input_string = integer_to_reverse_binary(integer_value)
    print(reverse_string(input_string))

