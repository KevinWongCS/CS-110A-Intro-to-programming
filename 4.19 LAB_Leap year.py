# A year in the modern Gregorian Calendar consists of 365 days. In reality, the earth takes
# longer to rotate around the sun. To account for the difference in time, every 4 years, a
# leap year takes place. A leap year is when a year has 366 days: An extra day, February 29th. The
# requirements for a given year to be a leap year are:
#
# 1) The year must be divisible by 4
#
# 2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400
#
# Some example leap years are 1600, 1712, and 2016.
#
# Write a program that takes in a year and determines whether that year is a leap year.
#
# Ex: If the input is:
#
# 1712
#
# the output is:
#
# 1712 - leap year
#
# Ex: If the input is:
#
# 1913
#
# the output is:
#
# 1913 - not a leap year

is_leap_year = False

input_year = int(input())

if ((input_year % 100)) == 0 and ((input_year % 400) == 0):
    print(input_year, "- leap year")
elif ((input_year % 100) != 0) and ((input_year % 4) == 0):
    print(input_year, "- leap year")
else:
    print(input_year, "- not a leap year")

