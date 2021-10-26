# When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust
# the data. This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.
#
# For this program, adjust the values by dividing all values by the largest value. The input begins with
#     an integer indicating the number of floating-point values that follow.
#
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('{:.2f}'.format(your_value))
#
# Ex: If the input is:
#
# 5
# 30.0
# 50.0
# 10.0
# 100.0
# 65.0
#
# the output is:
#
# 0.30
# 0.50
# 0.10
# 1.00
# 0.65
#
# The 5 indicates that there are five floating-point values in the list, namely 30.0, 50.0, 10.0, 100.0,
# and 65.0. 100.0 is the largest value in the list, so each value is divided by 100.0.

length_list = int(input())
height_list = []
largest_height = 0
i = 0
while i < length_list:
    height = float(input())
    height_list.append(height)
    i += 1

    if largest_height < height:
        largest_height = height

for height in height_list:
    normalized_height = height / largest_height
    print('{:.2f}'.format(normalized_height))