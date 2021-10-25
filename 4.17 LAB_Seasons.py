# Write a program that takes a date as input and outputs the date's season. The input is a string
# to represent the month and an int to represent the day.
#
# Ex: If the input is:
#
# April
# 11
#
# the output is:
#
# Spring
#
# In addition, check if the string and int are valid (an actual month and day).
#
# Ex: If the input is:
#
# Blue
# 65
#
# the output is:
#
# Invalid
#
# The dates for each season are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

input_month = input()
input_day = int(input())

month_dict = {
    "January": 1,
    "Febuary": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
if (input_month not in month_dict) or (input_day <= 0 or input_day > 31)or (input_month == "September" and input_day == 31):
    print("Invalid")
elif (month_dict[input_month] >= 3 and month_dict[input_month] < 6):
    season = "Spring"
elif (month_dict[input_month] >= 6 and month_dict[input_month] < 9):
    season = "Summer"
elif (month_dict[input_month] >= 9 and month_dict[input_month] < 12):
    season = "Autumn"
elif (month_dict[input_month] >= 12 and month_dict[input_month] < 3):
    season = "Winter"

if input_month not in month_dict:
    print(end="")
elif month_dict[input_month] == 3 and input_day < 20:
    season = "Winter"
elif month_dict[input_month] == 6 and input_day < 21:
    season = "Spring"
elif month_dict[input_month] == 9 and input_day < 22:
    season = "Summer"
elif month_dict[input_month] == 12 and input_day < 21:
    season = "Autumn"
elif month_dict[input_month] == 12 and input_day > 20:
    season = "Winter"
if (input_month in month_dict) and (input_day >= 0 and input_day <= 31):
    print(season)

