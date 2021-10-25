# (1) Output a menu of automotive services and the corresponding cost of each service. (2 pts)
#
# Ex:
#
# Davy's auto shop services
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# Car wax -- $12
#
#
#
# (2) Prompt the user for two services from the menu. (2 pts)
#
# Ex:
#
# Select first service:
# Oil change
# Select second service:
# Car wax
#
#
#
# (3) Output an invoice for the services selected. Output the cost for each service and the total cost. (3 pts)
#
# Davy's auto shop invoice
#
# Service 1: Oil change, $35
# Service 2: Car wax, $12
#
# Total: $47
#
#
#
# (4) Extend the program to allow the user to enter a dash (-), which indicates no service. (3 pts)
#
# Ex:
#
# Davy's auto shop services
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# Car wax -- $12
#
# Select first service:
# Tire rotation
# Select second service:
# -
#
# Davy's auto shop invoice
#
# Service 1: Tire rotation, $19
# Service 2: No service
#
# Total: $19

print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")
service_1 = str(input("Select first service:\n"))
service_2 = str(input("Select second service:\n"))

services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
    "no service": 0
}

print("\nDavy's auto shop invoice\n")
if service_1 in services:
    print("Service 1: {:s}, ${:d}".format(service_1, services[service_1]))
elif service_1 == "-":
    print("Service 1: No service")
    service_1 = "no service"
if service_2 in services:
    print("Service 2: {:s}, ${:d}\n".format(service_2, services[service_2]))
elif service_2 == "-":
    print("Service 2: No service\n")
    service_2 = "no service"
print("Total: ${:d}".format(services[service_1] + services[service_2]))
