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
from typing import List, Any



class ItemToPurchase:
    # constructor
    def __init__(self, item_name = 'none', item_description = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity


    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price,
                                                self.item_quantity * self.item_price))
    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))

class ShoppingCart:
    # constructor
    def __init__(self, customer_name = "none", current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # "a" option
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    # "r" option
    def remove_item(self, itemName):
        self.cart_items.remove(itemName)

    # "c" option
    def modify_item(self, ItemToPurchase):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == ItemToPurchase.item_name:
                self.cart_items[i].item_quantity = ItemToPurchase.item_quantity

    def get_num_items_in_cart(self):
        # returns total number of items in cart
        num_items = 0
        # for loop returns total number of items in cart
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        # returns total cost of all items in cart
        total_cost = 0
        # for loop that calculates sum of all items in cart
        for item in self.cart_items:
            total_cost = total_cost + (item.item_price * item.item_quantity)
        return total_cost

        #############  print functions or methods for shopping cart class #################
    # "i" option
    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            ItemToPurchase.print_item_description(item)

    # "o" option
    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        if len(self.cart_items) == 0:
            print("Number of Items: 0")
            print()
            print("SHOPPING CART IS EMPTY")
        else:
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            print()
            for item in self.cart_items:
                ItemToPurchase.print_item_cost(item)
        print()
        print("Total: ${}".format(self.get_cost_of_cart()))

    def print_menu(self):
        # passes test
        print()
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

    def execute_menu(self):
        while True:
            print_menu()
            print()
            user_choice = input("Choose an option:\n")
            # loop for correct choice
            while user_choice not in ["a", "r", "c", "i", "o", "q", "p"]:
                user_choice = input("Choose an option:\n")
            if user_choice == "a":
                print("ADD ITEM TO CART")
                # Add item to cart
                item_name = input("Enter the item name:\n")
                item_description = input("Enter the item description:\n")
                item_price = int(input("Enter the item price:\n"))
                item_quantity = int(input("Enter the item quantity:\n"))
                print()
                item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
                self.add_item(item)
                continue
            if user_choice == "r":
                print("REMOVE ITEM FROM CART")
                itemInCart = True
                itemName = input("Enter name of item to remove:\n")
                # checking for matching name
                for item in self.cart_items:
                    if itemName == item.item_name:
                        self.remove_item(item)
                        itemInCart = True
                        break
                    else:
                        itemInCart = False
                if itemInCart == False:
                    print("Item not found in cart. Nothing removed.")
                    print()

                continue
            if user_choice == "c":
                print("CHANGE ITEM QUANTITY")
                # temp item (not appended to list) for swapping quantity with an existing list item
                item_name = input("Enter the item name:\n")
                item_description = "none"
                item_price = 0
                item_quantity = int(input("Enter the new quantity:\n"))
                tempItem = ItemToPurchase(item_name, item_description, item_price, item_quantity)
                # checking for matching name
                for item in self.cart_items:
                    if item.item_name == tempItem.item_name:
                        self.modify_item(tempItem)
                    else:
                        print("Item not found in cart. Nothing modified.")
                        print()
                        break

                continue
            if user_choice == "i":
                self.print_descriptions()
                print()
            if user_choice == "o":
                self.print_total()
                print()
                    #################
            # hidden test bench option "print"
            if user_choice == "p":
                for items in self.cart_items:
                    print(items.item_name)
                    print (items.item_description)
                    print(items.item_price)
                    print(items.item_quantity)
                    #################
            if user_choice == "q":
                break

# for unit test ###########
def print_menu():
    # passes test
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
###########################




if __name__ == "__main__":
    # (3) In the main section of the code, prompt the user for a customer's name and today's
    # date. Output the name and date. Create an object of type ShoppingCart. (1 pt)
    testcart = ShoppingCart()
    testcart.customer_name = input("Enter customer's name:\n")
    testcart.current_date = input("Enter today's date:\n")
    print()
    print("Customer name: {}".format(testcart.customer_name))
    print("Today's date: {}".format(testcart.current_date))
    print()
    testcart.execute_menu()

    # TEST_BENCH
    # testcart = ShoppingCart()
    # testcart.execute_menu()

