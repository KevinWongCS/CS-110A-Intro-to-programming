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
        self.item_description = 'none'

    def print_item_cost(self):
        return "{:s} {:d} @ ${:d} = ${}".format(self.item_name, self.item_quantity, self.item_price,
                                                self.item_quantity * self.item_price)
    def print_item_description(self):
        return "{}: {}".format(self.item_name, self.item_description)
########################## part 2 of assignment ####################################################
class ShoppingCart(ItemToPurchase):
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        # note: instructions where to not return anything for this method
        # adds items to cart
        self.item_name = input("Enter the item name:\n")
        self.item_description = input("Enter the item description:\n")
        self.item_price = int(input("Enter the item price:\n"))
        self.item_quantity = int(input("Enter the item quantity:\n"))
        self.cart_items.append(self.ItemToPurchase)

    def remove_item(self):
        # note: doesn't return anything, removes items in cart
        ItemName = input("Enter name of item to remove:\n")
        if ItemName not in cart_items:
            print("Item not found in cart. Nothing removed.")
        else:
            self.cart_items.remove(ItemName)

    def modify_item(self):
        # note: doesn't return anything, modifies item quantity
        print("CHANGE ITEM QUANTITY")
        ItemName = input("Enter the item name:\n")
        ItemQuant = input("Enter the new quantity:\n")
        if ItemName not in self.cart_items:
            print("Item not found in cart. Nothing modified.")
        else:
            self.item.quantity = ItemQuant

    def get_num_items_in_cart(self):
        # returns total number of items in cart
        num_items = 0
        for item in self.cart_items:
            num_items += 1
        return num_items

    def get_cost_of_cart(self):
        # returns total cost of all items in cart
        total_cost = 0
        for item in self.cart_items:
            total_cost += self.item_price * self.item_quantity
        return total_cost

    #############  Main output functions for shopping cart #################
    def print_descriptions(self):
        # note: (8) Implement Output item's description menu option in execute_menu(). (2 pts)
        print("{}'s Shopping Cart - {}".format(customer_name, current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print_item_description(item)

    def print_total(self):
        print("{}'s Shopping Cart - {}".format(customer_name, current_date))
        print("Number of Items: {}".format(self.get_num_items_in_cart(self)))
        print()
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print_item_cost(item)
            print()
            print("Total: {:d}".format(self.get_cost_of_cart(self)))

    def print_menu():
        # note: (7) Implement Output shopping cart menu option in execute_menu(). (3 pts)
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()
        print("Choose an option:")

    def get_choice(self):
        self.user_choice = str(input())

    def execute_menu(self, user_choice, cart_items):
        self.print_menu()
        while True:
            if self.user_choice == "q":
                break
            elif self.user_choice == "a":
                ItemToPurchase = input()
                self.add_item(self.cart_items)
            # elif user_choice == "r":
            #
            # elif user_choice == "c":
            # elif user_choice == "i":
            # elif user_choice == "o":

            else:
                print("Invalid choice")
                self.user_choice = str(input())




if __name__ == "__main__":

    testcart = ShoppingCart()
    testcart.get_choice()
    testcart.execute_menu(user_choice)