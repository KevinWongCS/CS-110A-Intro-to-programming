#######################################################
# Exercise 85: Convert an Integer to its Ordinal Number
########################################################
# Words like first, second and third are referred to as ordinal numbers. In this exercise, you will
# write a function that takes an integer as its only parameter and returns a string containing the appropriate
# English ordinal number as its only result. Your function must handle the integers between 1 and 12 (inclusive).
# It should return an empty string if a value outside of this range is provided as a parameter. Include a main
# program that demonstrates your function by displaying each integer from 1 to 12 and its ordinal number. Your
# main program should only run when your file has not been imported into another program.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# ordinal_numb = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th'] # not needed
ordinal_num_2 = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
# suffix = ["th","st","nd","rd","th","th","th","th","th","th"] # not needed
ordinal_num_dict = {}
# created ordinal dictionary: key = integer: value = ordinal equivalent
for counter, number in enumerate(num):
    ordinal_num_dict[number] = ordinal_num_2[counter]

def ordinal_converter(integer):
    # returns the ordinal for an integer from 1 to 12
    if integer in ordinal_num_dict:
        print(ordinal_num_dict[integer])
    else:
        print("")

if __name__ == "__main__":
    # get integer from user
    user_int = int(input("Enter a integer from 1 to 12: \n"))
    ordinal_converter(user_int)