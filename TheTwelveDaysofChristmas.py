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

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ordinal_num_2 = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
verses = ["A partridge in a pear tree", "Two turtle doves", "Three French hens", "Four calling birds", "Five gold rings",\
          "Six geese a-laying", "Seven swans a-swimming", "Eight maids a-milking", "Nine ladies dancing", "Ten lords a-leaping",\
          "Eleven pipers piping", "Twelve drummers drumming"]
# Dictionary, key: ordinals and values: verses
verse_dict = {}
int_ord_dict = {}
for counter, ordinal in enumerate(ordinal_num_2):
    verse_dict[ordinal] = verses[counter]
# Dictionary, key: integers and values: ordinals
for counter, number in enumerate(num):
    int_ord_dict[number] = ordinal_num_2[counter]

def twelve_days_song(): # i have to call this function 12 times (for loop obvs)
    # displays the complete lyrics for The Twelve Days of Christmas.
    for ordinal in verse_dict:
        print("On the {} day of Christmas my true love sent to me".format(ordinal))
        for counter in range(ordinal_num_2.index(ordinal),-1, -1): # should be the current number's index printing every preceding index in descending order.
            if ordinal == 'first' and ordinal_num_2.index(ordinal) == 0:
                print("{}.".format(verses[counter]))
            elif ordinal != 'first' and counter != 0:
                print("{},".format(verses[counter]))
            elif ordinal != 'first' and counter == 0:
                print("{}.".format((verses[counter]).replace("A", "And a")))

def verse_number_recall(verse_num):
    # takes the verse number as its only parameter and displays the specified verse of the song.
    if verse_num in int_ord_dict:
        print("On the {} day of Christmas my true love sent to me".format(int_ord_dict[verse_num]))
        print("{}.\n".format(verses[verse_num - 1]))
        print()

if __name__ == "__main__":
    verse_num = int(input("Enter a verse number from 1 to 12:\n"))
    verse_number_recall(verse_num)
    twelve_days_song()