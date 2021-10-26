############################################
# Exercise 36: Vowel or Consonant, Section 1
############################################
# In this exercise you will create a program that reads a letter of the alphabet
# from the user. If the user enters a, e, i, o or u then your program should display a
# message indicating that the entered letter is a vowel. If the user enters y then your
# program should display a message indicating that sometimes y is a vowel, and sometimes
# y is a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.

user_letter = input('Enter a letter:\n')
if user_letter == 'a' or user_letter == 'A' or \
    user_letter == 'e' or user_letter == 'E' or \
    user_letter == 'i' or user_letter == 'I' or \
    user_letter == 'o' or user_letter == 'O' or \
    user_letter == 'u' or user_letter == 'U':
    print('The entered letter "{:s}" is a vowel'.format(user_letter))
elif user_letter == 'y' or user_letter == 'Y':
    print('Sometimes "{:s}" is a vowel, and sometimes y is a consonant'.format(user_letter))
else:
    print('The letter "{:s}" is a consonant.'.format(user_letter))
print()

####################################################
# Exercise 45: What Color is that Square?, Section 1
####################################################
# (22 Lines) Positions on a chess board are identified by a letter and a number. The letter
# identifies the column, while the number identifies the row, as shown below: 8, 7, 6, 5, 4, 3, 2, 1
# from  top to bottom row; a, b, c, d, e, f, g, h for each,  column, left to right. W is for white
# color, B is for black color.

user_row = int(input('Enter a row number from 1 to 8:\n'))
user_column = input('Enter a column letter from a to h in lowercase:\n')

while user_row > 8 or user_row < 1:
    user_row = int(input('Enter a row number from 1 to 8:\n'))
while (ord(user_column) - 96) > (ord('h')- 96) or (ord(user_column) - 96) < 0:
    user_column = input('Enter a column letter from a to h in lowercase:\n')

if user_row % 2 == 0 and (ord(user_column) - 96) % 2 == 0 or \
    user_row % 2 != 0 and (ord(user_column) - 96) % 2 != 0:
    print('The square is black')
    print()
else:
    print('The square is white')
    print()

#########################################
# Exercise 64: No More Pennies, Section 2
#########################################
#  February 4, 2013 was the last day that pennies were distributed by the Royal Canadian Mint. Now that
# pennies have been phased out retailers must adjust totals so that they are multiples of 5 cents when
# they are paid for with cash (credit card and debit card transactions continue to be charged to the penny).
# While retailers have some freedom in how they do this, most choose to round to the closest nickel.
#
# Write a program that reads prices from the user until a blank line is entered. Display the total cost of
# all the entered items on one line, followed by the amount due if the customer pays with cash on a second
# line. The amount due for a cash  payment should be rounded to the nearest nickel. One way to compute the
# cash payment amount is to begin by determining how many pennies would be needed to pay the total. Then compute
# the remainder when this number of pennies is divided by 5. Finally, adjust the total down if the remainder is
# less than 2.5. Otherwise adjust the total up.

pennies_per_dollar = 100

total_cost = 0
while True:
    amount = input('Enter price:\n')
    if amount == '':
        break
    elif float(amount) >= 0:
        total_cost += float(amount)
print('Total cost of all entered items: ${:.2f}'.format(total_cost))

dollar_amount_no_change = total_cost // 1
cents_in_pennies = total_cost % 1
nickels_change_possible = cents_in_pennies // 0.05
max_nickels_possible = nickels_change_possible * 0.05
pennies_remaining = cents_in_pennies % 0.05

if pennies_remaining >= 0.025:
    pennies_remaining = 0.05
elif pennies_remaining < 0.25:
    pennies_remaining = 0

amount_due = dollar_amount_no_change + max_nickels_possible + pennies_remaining


print('The amount due: ${:.2f}'.format(amount_due))
print()

#######################################################
# Exercise 66: Compute a Grade Point Average, section 2
#######################################################
# Exercise 51 included a table that shows the conversion from letter grades to grade points at a particular
# academic institution. In this exercise you will compute the grade point average of an arbitrary number of
# letter grades entered by the user. The user will enter a blank line to indicate that all of the grades have
# been provided. For example, if the user enters A, followed by C+, followed by B, followed by a blank line then
# your program should report a grade point average of 3.1.
#
# You may find your solution to Exercise 51 helpful when completing this exercise. Your program does
# not need to do any error checking. It can assume that each value entered by the user will always be a
# valid letter grade or a blank line.

grade_list = []
grade_scale = {'A+' : 4.0, 'A' : 4.0, 'A-' : 3.7,
               'B+' : 3.3, 'B' : 3.0, 'B-' : 2.7,
               'C+' : 2.3, 'C' : 2.0, 'C-' : 1.7,
               'D+' : 1.3, 'D' : 1.0, 'F': 0.0
               }

while True:
    grade = str(input('Enter a grade:\n'))
    # this method was very inefficient
    # if grade == 'A' or grade == 'a' or \
    #     grade == 'A+' or grade == 'A-' or \
    #     grade == 'a+' or grade == 'a-' or \
    #     grade == 'B' or grade == 'b' or \
    #     grade == 'B+' or grade == 'B-' or \
    #     grade == 'b+' or grade == 'b-' or \
    #     grade == 'C' or grade == 'c' or \
    #     grade == 'C+' or grade == 'C-' or \
    #     grade == 'c+' or grade == 'c-' or \
    #     grade == 'D' or grade == 'd' or \
    #     grade == 'D+' or grade == 'd+' or \
    #     grade == 'F' or grade == 'f':

    # this simple if statement makes the code way cleaner
    if grade in grade_scale:
        grade_list.append(grade)
    if grade == '':
        print(grade_list)
        break


total = 0
x = 0
for i in grade_list:
    total += grade_scale[i]
    x += 1
    if x == (len(grade_list)):
        print(round((total / x), 1))
print()