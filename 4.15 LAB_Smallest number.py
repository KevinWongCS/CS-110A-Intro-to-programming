# Write a program whose inputs are three integers, and whose output is the smallest of the three values.
#
# Ex: If the input is:
# 7
# 15
# 3
#
# the output is:
# 3

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 <= num2 and num1 <= num3:
    print(num1)
elif num2 < num3:
    print(num2)
else:
    print(num3)