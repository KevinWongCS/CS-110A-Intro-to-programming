# Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south,
# and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the
# primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90.
#
# Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary,
# indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.
#
# Ex: If the input is:
#
# 90
#
# the output is:
#
# I-90 is primary, going east/west.
#
# Ex: If the input is:
#
# 290
#
# the output is:
#
# I-290 is auxiliary, serving I-90, going east/west.
#
# Ex: If the input is:
#
# 0
#
# the output is:
#
# 0 is not a valid interstate highway number.
#
# Ex: If the input is:
#
# 200
#
# the output is:
#
# 200 is not a valid interstate highway number.

user_input = int(input())

if (user_input < 1 or user_input > 999 or user_input == 200):
    print(user_input, "is not a valid interstate highway number.")

if (user_input >= 1 and user_input <= 999 and user_input != 200):
    highway = "primary"
    direction = "north/south"
    if user_input % 2 == 0:
        direction = "east/west"
    if user_input >= 99:
        highway = "auxiliary"
        primary_highway = user_input % 100
        print("I-{:d} is {:s}, serving I-{:d}, going {:s}.".format(user_input, highway, primary_highway, direction))
    else:
        print("I-{:d} is {:s}, going {:s}.".format(user_input, highway, direction))
