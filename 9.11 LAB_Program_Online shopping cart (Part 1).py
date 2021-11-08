# 9.11 LAB*: Program: Online shopping cart (Part 1)
#
# (1) Build the ItemToPurchase class with the following specifications:
#
#     Attributes (3 pts)
#         item_name (string)
#         item_price (int)
#         item_quantity (int)
#     Default constructor (1 pt)
#         Initializes item's name = "none", item's price = 0, item's quantity = 0
#     Method
#         print_item_cost()
#
#
# Ex. of print_item_cost() output:
#
# Bottled Water 10 @ $1 = $10
#
# (2) In the main section of your code, prompt the user for two items and create two objects
# of the ItemToPurchase class. (2 pts)
#
# Ex:
#
# Item 1
# Enter the item name:
# Chocolate Chips
# Enter the item price:
# 3
# Enter the item quantity:
# 1
#
# Item 2
# Enter the item name:
# Bottled Water
# Enter the item price:
# 1
# Enter the item quantity:
# 10
#
#
# (3) Add the costs of the two items together and output the total cost. (2 pts)
#
# Ex:
#
# TOTAL COST
# Chocolate Chips 1 @ $3 = $3
# Bottled Water 10 @ $1 = $10
#
# Total: $13
#


class ItemToPurchase:
    # PARAMETERIZED CONSTRUCTOR ----------------------- CAUSED ME ALOT OF TROUBLE WITH SYNTAX!!!!!!!!
    # could have also put the parameters along side "self"
    # def __init__(self, item_name, item_price, item_quantity, item_description):
    # the above is called a parameterized constructor
    # if using a parameterized constructor, we initialize the parameters inside the constructor
    # i.e. def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = 0):
    # used when you want to pass the values during object creation
    # i.e. Iwant = ItemToPurchase(COCO, 2, 5)
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity


    def print_item_cost(self):
        print("{:s} {:d} @ ${:d} = ${}".format(self.item_name, self.item_quantity, self.item_price,
                                                self.item_quantity * self.item_price))
    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))
########################## part 2 of assignment ####################################################


if __name__ == "__main__":
    print("Item 1")
    item_name = input("Enter the item name:\n")
    item_price = int(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    Iwant = ItemToPurchase(item_name, item_price, item_quantity)
    print()
    # note: the above and below are two acceptable way to create an instance for a class
    # top way is better imo
    print("Item 2")
    Iwant2 = ItemToPurchase()
    Iwant2.item_name = input("Enter the item name:\n")
    Iwant2.item_price = int(input("Enter the item price:\n"))
    Iwant2.item_quantity = int(input("Enter the item quantity:\n"))
    print()
    print("TOTAL COST")
    Iwant.print_item_cost()
    print(Iwant2.print_item_cost())
    print()
    print("Total: ${:d}".format((Iwant.item_quantity * Iwant.item_price) + (Iwant2.item_quantity * Iwant2.item_price)))
    # ########################## part 2 of assignment ####################################################
