#
# 4.20 LAB: Warm up: Automobile service cost
#
# (1) Prompt the user for an automobile service. Output the user's input. (1 pt)
#
# Ex:
#
# Enter desired auto service:
# Oil change
# You entered: Oil change
#
#
# (2) Output the price of the requested service. (4 pts)
#
# Ex:
#
# Enter desired auto service:
# Oil change
# You entered: Oil change
# Cost of oil change: $35
#
#
# The program should support the following services (all integers):
#
#     Oil change -- $35
#     Tire rotation -- $19
#     Car wash -- $7
#
# If the user enters a service that is not listed above, then output the following error message:
#
# Error: Requested service is not recognized
#

services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7
}

requested_service = str(input("Enter desired auto service:\n"))

if requested_service in services:
    print("You entered:", requested_service)
    if requested_service == "Oil change":
        print("Cost of oil change: ${:d}".format(services[requested_service]))
    if requested_service == "Tire rotation":
        print("Cost of tire rotation: ${:d}".format(services[requested_service]))
    if requested_service == "Car wash":
        print("Cost of car wash: ${:d}".format(services[requested_service]))
elif requested_service not in services:
    print("You entered: {:s}".format(requested_service))
    print("Error: Requested service is not recognized")
