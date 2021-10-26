# (1) Prompt the user to enter four numbers, each corresponding to a person's weight in pounds. Store
# all weights in a list. Output the list. (2 pts)
#
# Ex:
#
# Enter weight 1:
# 236.0
# Enter weight 2:
# 89.5
# Enter weight 3:
# 176.0
# Enter weight 4:
# 166.3
# Weights: [236.0, 89.5, 176.0, 166.3]
#
# (2) Output the average of the list's elements with two digits after the decimal point. Hint: Use a
# conversion specifier to output with a certain number of digits after the decimal point. (1 pt)
#
# (3) Output the max list element with two digits after the decimal point. (1 pt)
#
# Ex:
#
# Enter weight 1:
# 236.0
# Enter weight 2:
# 89.5
# Enter weight 3:
# 176.0
# Enter weight 4:
# 166.3
# Weights: [236.0, 89.5, 176.0, 166.3]
#
# Average weight: 166.95
# Max weight: 236.00
#
# (4) Prompt the user for a number between 1 and 4. Output the weight at the user specified location and
# the corresponding value in kilograms. 1 kilogram is equal to 2.2 pounds. (3 pts)
#
# Ex:
#
# Enter a list location (1 - 4):
# 3
# Weight in pounds: 176.00
# Weight in kilograms: 80.00
#
# (5) Sort the list's elements from least heavy to heaviest weight. (2 pts)
#
# Ex:
#
# Sorted list: [89.5, 166.3, 176.0, 236.0]
#
# Output the average and max weights as floating-point values with two digits after the decimal point,
# which can be achieved as follows:
# print('{:.2f}'.format(your_value))

# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.

# FIXME (2): Output average of weights.

# FIXME (3): Output max weight from list.

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.

# FIXME (5): Sort the list and output it.

#  	my_list = [5, 8]
#     my_list.append(16)

if __name__ == "__main__":
    weight_list = []
    # BETTER WAY TO GET A NON AMOUNT OF INPUT
    for i in range(4):
        weight = input('Enter weight {:d}:\n'.format(i + 1))
        weight_list.append(weight)

    # VERY INEFFICIENT WAY TO DO IT
    # getting 4 weights and appending them into a list
    # weight_list = []
    # weight1 = float(input('Enter weight 1:\n'))
    # weight2 = float(input('Enter weight 2:\n'))
    # weight3 = float(input('Enter weight 3:\n'))
    # weight4 = float(input('Enter weight 4:\n'))
    # weight_list.append(weight1)
    # weight_list.append(weight2)
    # weight_list.append(weight3)
    # weight_list.append(weight4)

    # for average weight and max weight
    print('Weights:', weight_list)
    print()
    print('Average weight: {:.2f}'.format(sum(weight_list) / len(weight_list)))
    print('Max weight: {:.2f}'.format(max(weight_list)))
    print()

    # for weight in lbs and kg conversion 2.2 lbs per 1 kg
    location = int(input('Enter a list location (1 - 4):\n'))
    print('Weight in pounds: {:.2f}'.format(weight_list[location - 1]))
    print('Weight in kilograms: {:.2f}'.format(weight_list[location - 1] / 2.2))
    print()

    # sorted list light to heavy
    print('Sorted list:', sorted(weight_list))