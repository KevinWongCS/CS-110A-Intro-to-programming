# Write a program that reads a list of integers, and outputs whether the list contains all
# even numbers, odd numbers, or neither. The input begins with an integer indicating the number
# of integers in the list. The first integer is not in the list.
#
# Ex: If the input is:
#
# 5
# 2
# 4
# 6
# 8
# 10
#
# the output is:
#
# all even
#
# Ex: If the input is:
#
# 5
# 1
# -3
# 5
# -7
# 9
#
# the output is:
#
# all odd
#
# Ex: If the input is:
#
# 5
# 1
# 2
# 3
# 4
# 5
#
# the output is:
#
# not even or odd
#
# Your program must define and call the following two functions. is_list_even() returns true if all
# integers in the list are even and false otherwise. is_list_odd() returns true if all integers in the
# list are odd and false otherwise.
# def is_list_even(my_list)
# def is_list_odd(my_list)

import math
even_num_list = []
odd_num_list = []
def is_list_even(list):
    bool_even = True
    for x in list:
        if (x == 0) or (x % 2 != 0):
            bool_even = False
            break
    return bool_even

def is_list_odd(list):
    bool_odd = True
    for y in list:
        if (y == 0) or (y % 2 == 0):
            bool_odd = False
            break
    return bool_odd

if __name__ == '__main__':
    num_list = []
    my_list = int(input())
    for i in range(my_list):
        num = int(input())
        num_list.append(math.fabs(num))

    if is_list_even(num_list):
        print('all even')
    elif is_list_odd(num_list):
        print('all odd')
    else:
        print('not even or odd')