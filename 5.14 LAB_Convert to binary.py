#
# 5.14 LAB: Convert to binary
#
# Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's
# representing the integer in binary. For an integer x, the algorithm is:
#
# As long as x is greater than 0
#    Output x modulo 2 (remainder is either 0 or 1)
#    Assign x with x divided by 2
#
# Note: The above algorithm outputs the 0's and 1's in reverse order.
#
# Ex: If the input is:
#
# 6
#
# the output is:
#
# 011
#
# 6 in binary is 110; the algorithm outputs the bits in reverse.

number = int(input())

binary_number = ''

while number // 2 != 0:
    if number % 2 == 1:
        binary_number += '1'
    if number % 2 == 0:
        binary_number += '0'
    number = number // 2
    if number // 2 == 0:
        binary_number += '1'
else:
    print(binary_number)

# binary_number_rev = ''
# index = 0
# for index in range(0, len(binary_number)):
#     binary_number_rev += binary_number[(len(binary_number) - 1) - index]
# print(binary_number_rev)



