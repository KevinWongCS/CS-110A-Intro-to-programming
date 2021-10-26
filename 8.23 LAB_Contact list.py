#
# 8.23 LAB: Contact list
#
# A contact list is a place where you can store a specific contact with other associated
# information such as a phone number, email address, birthday, etc. Write a program that
# first takes in word pairs that consist of a name and a phone number (both strings). That
# list is followed by a name, and your program should output the phone number associated with that name.
#
# Ex: If the input is:
#
# Joe 123-5432 Linda 983-4123 Frank 867-5309
# Frank
#
# the output is:
#
# 867-5309

user_string = input()
user_name = input()
user_list = user_string.split()
contact_list = {}
## list method ###
# list.index(x)

# turns user entered string into a dictionary
for string in user_list:
    if user_list.index(string) % 2 == 0:
        contact_list[string] = user_list[user_list.index(string) + 1]
# print(contact_list)

# prints phone number for user name
print(contact_list[user_name])