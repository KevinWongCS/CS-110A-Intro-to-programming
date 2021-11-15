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

###########################################
# Exercise 86: The Twelve Days of Christmas
###########################################
# The Twelve Days of Christmas is a repetitive song that describes an increasingly long
# list of gifts sent to one’s true love on each of 12 days. A single gift is sent on the first day.
# A new gift is added to the collection on each additional day, and then the complete collection is sent.
# The first three verses of the song are shown below. The complete lyrics are available on the internet.
#
# Your task is to write a program that displays the complete lyrics for The Twelve Days of Christmas. Write a
# function that takes the verse number as its only parameter and displays the specified verse of the song. Then
# call that function 12 times with integers that increase from 1 to 12.
#
# Each item that is sent to the recipient in the song should only appear once in your program, with the possible
# exception of the partridge. It may appear twice if that helps you handle the difference between “A partridge in a
# pear tree” in the first verse and
# “And a partridge in a pear tree” in the subsequent verses. Import your solution
# to Exercise 85 to help you complete this exercise.

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# ordinal_num_2 = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
# verses = ["A partridge in a pear tree", "Two turtle doves", "Three French hens", "Four calling birds", "Five gold rings",\
#           "Six geese a-laying", "Seven swans a-swimming", "Eight maids a-milking", "Nine ladies dancing", "Ten lords a-leaping",\
#           "Eleven pipers piping", "Twelve drummers drumming"]
# # Dictionary, key: ordinals and values: verses
# verse_dict = {}
# int_ord_dict = {}
# for counter, ordinal in enumerate(ordinal_num_2):
#     verse_dict[ordinal] = verses[counter]
# # Dictionary, key: integers and values: ordinals
# for counter, number in enumerate(num):
#     int_ord_dict[number] = ordinal_num_2[counter]
#
# def twelve_days_song(): # i have to call this function 12 times (for loop obvs)
#     # displays the complete lyrics for The Twelve Days of Christmas.
#     for ordinal in verse_dict:
#         print("On the {} day of Christmas my true love sent to me".format(ordinal))
#         for counter in range(ordinal_num_2.index(ordinal),-1, -1): # should be the current number's index printing every preceding index in descending order.
#             if ordinal == 'first' and ordinal_num_2.index(ordinal) == 0:
#                 print("{}.".format(verses[counter]))
#             elif ordinal != 'first' and counter != 0:
#                 print("{},".format(verses[counter]))
#             elif ordinal != 'first' and counter == 0:
#                 print("{}.".format((verses[counter]).replace("A", "And a")))
#
# def verse_number_recall(verse_num):
#     # takes the verse number as its only parameter and displays the specified verse of the song.
#     if verse_num in int_ord_dict:
#         print("On the {} day of Christmas my true love sent to me".format(int_ord_dict[verse_num]))
#         print("{}.\n".format(verses[verse_num - 1]))
#         print()
#
# if __name__ == "__main__":
#     verse_num = int(input("Enter a verse number from 1 to 12:\n"))
#     verse_number_recall(verse_num)
#     twelve_days_song()


###############################
# Exercise 94: Random Password
###############################
# Write a function that generates a random password. The password should have a random length of between 7 and 10
# characters. Each character should be randomly selected from positions 33 to 126 in the ASCII table. Your function
# will not take any parameters. It will return the randomly generated password as its only result. Display the randomly
# generated password in your file’s main program. Your main program should only run when your solution has not been
# imported into another file.
#
# Hint: You will probably find the chr function helpful when completing this exercise. Detailed information
# about this function is available online.

# import random
# def random_pwd_generator():
#     password = ""
#     for counter in range(random.randrange(7, 11, 1)): # note: upperrange of random.randrange is not included
#         password += chr(random.randrange(33, 127, 1))
#     print("Your password({} characters): {}".format(counter + 1, password))
#
# if __name__ == "__main__":
#     random_pwd_generator()