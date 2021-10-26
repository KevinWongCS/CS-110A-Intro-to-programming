# Many documents use a specific format for a person's name. Write a program whose input is:
#
# firstName middleName lastName
#
# and whose output is:
#
# lastName, firstInitial.middleInitial.
#
# Ex: If the input is:
#
# Pat Silly Doe
#
# the output is:
#
# Doe, P.S.
#
# If the input has the form:
#
# firstName lastName
#
# the output is:
#
# lastName, firstInitial.
#
# Ex: If the input is:
#
# Julia Clark
#
# the output is:
#
# Clark, J.
#

user_name = str(input())


def initials_printer(user_name):
    user_name_list = user_name.split()
    # prints last name
    print(user_name_list[len(user_name_list) - 1] + ',', end=' ')
    # prints first name depending if there's a middle name or not
    first_name = user_name_list[0]
    if (len(user_name_list) - 1) <= 1:
        print(first_name[0:1] + '.')
    else:
        print(first_name[0:1] + '.', end='')
    # prints middle names in entered order
    if len(user_name_list) >= 2:
        for i in range(1, len(user_name_list) - 1):
            middle_name = user_name_list[i]
            print(middle_name[0:1] + '.')


initials_printer(user_name)