# (1) Prompt the user for a title for data. Output the title. (1 pt)
#
# Ex:
#
# Enter a title for the data:
# Number of Novels Authored
# You entered: Number of Novels Authored
#
#
# (2) Prompt the user for the headers of two columns of a table. Output the column headers. (1 pt)
#
# Ex:
#
# Enter the column 1 header:
# Author name
# You entered: Author name
#
# Enter the column 2 header:
# Number of novels
# You entered: Number of novels
#
#
# (3) Prompt the user for data points. Data points must be in this format: string, int. Store the information
# before the comma into a string variable and the information after the comma into an integer. The
# user will enter -1 when they have finished entering data points. Output the data points. Store the
# string components of the data points in a list of strings. Store the integer components of the data
# points in a list of integers. (4 pts)
#
# Ex:
#
# Enter a data point (-1 to stop input):
# Jane Austen, 6
# Data string: Jane Austen
# Data integer: 6
#
#
# (4) Perform error checking for the data point entries. If any of the following errors occurs, output the
# appropriate error message and prompt again for a valid data point.
#
#     If entry has no comma
#         Output: Error: No comma in string. (1 pt)
#     If entry has more than one comma
#         Output: Error: Too many commas in input. (1 pt)
#     If entry after the comma is not an integer
#         Output: Error: Comma not followed by an integer. (2 pts)
#
#
# Ex:
#
# Enter a data point (-1 to stop input):
# Ernest Hemingway 9
# Error: No comma in string.
#
# Enter a data point (-1 to stop input):
# Ernest, Hemingway, 9
# Error: Too many commas in input.
#
# Enter a data point (-1 to stop input):
# Ernest Hemingway, nine
# Error: Comma not followed by an integer.
#
# Enter a data point (-1 to stop input):
# Ernest Hemingway, 9
# Data string: Ernest Hemingway
# Data integer: 9
#
#
# (5) Output the information in a formatted table. The title is right justified with a minimum field width
# value of 33. Column 1 has a minimum field width value of 20. Column 2 has a minimum field width value of 23. (3 pts)
#
# Ex:
#
#         Number of Novels Authored
# Author name         |       Number of novels
# --------------------------------------------
# Jane Austen         |                      6
# Charles Dickens     |                     20
# Ernest Hemingway    |                      9
# Jack Kerouac        |                     22
# F. Scott Fitzgerald |                      8
# Mary Shelley        |                      7
# Charlotte Bronte    |                      5
# Mark Twain          |                     11
# Agatha Christie     |                     73
# Ian Flemming        |                     14
# Stephen King        |                     54
# Oscar Wilde         |                      1
#
#
# (6) Output the information as a formatted histogram. Each name is right justified with a minimum
# field width value of 20. (4 pts)
#
# Ex:
#
#          Jane Austen ******
#      Charles Dickens ********************
#     Ernest Hemingway *********
#         Jack Kerouac **********************
#  F. Scott Fitzgerald ********
#         Mary Shelley *******
#     Charlotte Bronte *****
#           Mark Twain ***********
#      Agatha Christie *************************************************************************
#         Ian Flemming **************
#         Stephen King ******************************************************
#          Oscar Wilde *
#


if __name__ == "__main__":
    # get title
    user_title = str(input('Enter a title for the data:\n'))
    print('You entered: {}\n'.format(user_title))
    # get column names
    user_column_1 = str(input('Enter the column 1 header:\n'))
    print('You entered: {}\n'.format(user_column_1))
    user_column_2 = str(input('Enter the column 2 header:\n'))
    print('You entered: {}\n'.format(user_column_2))
    data_point_dict = {}
    while True:
        user_data_point = str(input('Enter a data point (-1 to stop input):\n'))
        # checks if user data point has a comma seperator
        if user_data_point == '-1':
            break
        if ',' not in user_data_point:
            print('Error: No comma in string.\n')
            continue
        # checks if value has only 1 comma
        if user_data_point.count(',') > 1:
            print('Error: Too many commas in input.\n')
            continue
        # checks if value entered after comma is a digit
        after_comma_index = user_data_point.find(',')  # index of comma, i want everthing after the comma
        string_after_comma = user_data_point[after_comma_index + 1:len(user_data_point)].strip()
        if string_after_comma.isdigit() == False:
            print('Error: Comma not followed by an integer.\n')
            continue
        # outputs data string and data integer
        else:
            user_data_point_list = user_data_point.split(',')
            data_string = user_data_point_list[0].strip()
            data_integer = user_data_point_list[1].strip()
            data_point_dict[data_string] = int(data_integer)
            print('Data string: {}'.format(data_string))
            print('Data integer: {}\n'.format(int(data_integer)))
    # print(data_point_dict)

    # prints table
    print()
    print('        {}'.format(user_title))
    format_string = '{column_1:<20}|{column_2:>23}'
    print(format_string.format(column_1=user_column_1, column_2=user_column_2))
    print('-' * 44)
    for key in data_point_dict:
        print(format_string.format(column_1=key, column_2=data_point_dict[key]))

    # prints histogram
    print()
    histogram = '{column_1:>20}'
    for key in data_point_dict:
        print(histogram.format(column_1=key), '*' * data_point_dict[key])


# sample input:
# Number of Novels Authored
# Author name
# Number of novels
# Jane Austen, 6
# Charles Dickens, 20
# Ernest Hemingway 9
# Ernest Hemingway9
# Ernest Hemingway, 9
# Jack Kerouac, 22
# F, Scott Fitzgerald, 8
# F. Scott, Fitzgerald, 8
# F. Scott Fitzgerald, 8
# Mary Shelley, 7
# Charlotte Bronte, 5
# Mark Twain, 11
# Agatha Christie, seventythree
# Agatha Christie, seventythree
# Agatha Christie, seventythree
# Agatha Christie, 73
# Ian Flemming, 14
# Stephen King, 54
# Oscar Wilde, 1
# -1