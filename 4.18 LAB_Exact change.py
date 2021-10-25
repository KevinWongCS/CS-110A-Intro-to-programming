# Write a program with total change amount as an integer input, and output the
# change using the fewest coins, one coin type per line. The coin types are Dollars,
# Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate,
# like 1 Penny vs. 2 Pennies.
#
# Ex: If the input is:
#
# 0
#
# (or less than 0), the output is:
#
# No change
#
# Ex: If the input is:
#
# 45
#
# the output is:
#
# 1 Quarter
# 2 Dimes
#

change = int(input())

if change <= 0:
    print("No change")
#Dollars
elif change > 0:
    change_dollars = change // 100
    change = change % 100
    if change_dollars == 0:
        print(end ="")
    elif change_dollars > 1:
        print(change_dollars, "Dollars")
    else:
        print(change_dollars, "Dollar")
#Quarters
if change > 0:
    change_quarters = change // 25
    change = change % 25
    if change_quarters == 0:
        print(end ="")
    elif change_quarters > 1:
        print(change_quarters, "Quarters")
    else:
        print(change_quarters, "Quarter")
#Dimes
if change > 0:
    change_dimes = change // 10
    change = change % 10
    if change_dimes == 0:
        print(end="")
    elif change_dimes > 1:
        print(change_dimes, "Dimes")
    else:
        print(change_dimes, "Dime")
#Nickels
if change > 0:
    change_nickels = change // 5
    change = change % 5
    if change_nickels == 0:
        print(end="")
    elif change_nickels > 1:
        print(change_nickels, "Nickels")
    else:
        print(change_nickels, "Nickel")
#Pennies
if change > 0:
    change_pennies = change // 1
    change = change % 1
    if change_pennies == 0:
        print(end="")
    elif change_pennies > 1:
        print(change_pennies, "Pennies")
    else:
        print(change_pennies, "Penny")
