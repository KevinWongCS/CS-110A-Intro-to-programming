# Write a program that first gets a list of integers from input. That list is followed by two more integers
# representing lower and upper bounds of a range. Your program should output all integers from the list that
# are within that range (inclusive of the bounds).
#
# Ex: If the input is:
#
# 25 51 0 200 33
# 0 50
#
# the output is:
#
# 25 0 33
#
# The bounds are 0-50, so 51 and 200 are out of range and thus not output.
#
# For coding simplicity, follow each output integer by a space, even the last one. Do not end with newline.

def list_string2int_converter(list):
    # converts a list of strings to list of integers
    new_list = [int(i) for i in list]
    return new_list


if __name__ == "__main__":
    # get input
    user_string = input()
    user_range = input()

    # parse input into a list of strings
    user_list = user_string.split()
    range = user_range.split()

    # list of strings to list of ints
    user_list_2 = list_string2int_converter(user_list)
    user_range_2 = list_string2int_converter(range)

    # upper and lower range
    upper_range = user_range_2[1]
    lower_range = user_range_2[0]

    ### TEST ###
    # print(user_list_2, user_range_2, upper_range, lower_range)
    ### TEST ###

    for number in user_list_2:
        if number >= lower_range and number <= upper_range:
            print(number, end=' ')