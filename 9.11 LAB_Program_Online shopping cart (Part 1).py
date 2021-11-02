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
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        return "{:s} {:d} @ ${:d} = ${}".format(self.item_name, self.item_quantity, self.item_price,
                                                self.item_quantity * self.item_price)


if __name__ == "__main__":
    print("Item 1")
    Iwant = ItemToPurchase()
    Iwant.item_name = input("Enter the item name:\n")
    Iwant.item_price = int(input("Enter the item price:\n"))
    Iwant.item_quantity = int(input("Enter the item quantity:\n"))
    print()
    print("Item 2")
    Iwant2 = ItemToPurchase()
    Iwant2.item_name = input("Enter the item name:\n")
    Iwant2.item_price = int(input("Enter the item price:\n"))
    Iwant2.item_quantity = int(input("Enter the item quantity:\n"))
    print()
    print("TOTAL COST")
    print(Iwant.print_item_cost())
    print(Iwant2.print_item_cost())
    print()
    print("Total: ${:d}".format((Iwant.item_quantity * Iwant.item_price) + (Iwant2.item_quantity * Iwant2.item_price)))