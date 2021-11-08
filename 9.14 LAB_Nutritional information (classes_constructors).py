#
# 9.14 LAB: Nutritional information (classes/constructors)
#
# Complete the FoodItem class by adding a constructor to initialize a food item. The constructor should
# initialize the name (a string) to "None" and all other instance attributes to 0.0 by default. If the
# constructor is called with a food name, grams of fat, grams of carbohydrates, and grams of protein, the
# constructor should assign each instance attribute with the appropriate parameter value.
#
# The given program accepts as input a food item name, fat, carbs, and protein and the number of servings. The
# program creates a food item using the constructor parameters' default values and a food item using the input
# values. The program outputs the nutritional information and calories per serving for both food items.
#
# Ex: If the input is:
#
# M&M's
# 10.0
# 34.0
# 2.0
# 1.0
#
# where M&M's is the food name, 10.0 is the grams of fat, 34.0 is the grams of carbohydrates, 2.0 is the
# grams of protein, and 1.0 is the number of servings, the output is:
#
# Nutritional information per serving of None:
#    Fat: 0.00 g
#    Carbohydrates: 0.00 g
#    Protein: 0.00 g
# Number of calories for 1.00 serving(s): 0.00
#
# Nutritional information per serving of M&M's:
#    Fat: 10.00 g
#    Carbohydrates: 34.00 g
#    Protein: 2.00 g
# Number of calories for 1.00 serving(s): 234.00

class FoodItem:
    # TODO: Define constructor with parameters to initialize instance
    #       attributes (name, fat, carbs, protein)
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    food_item1 = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())

    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    num_servings = float(input())

    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    food_item1.get_calories(num_servings)))

    print()

    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    food_item2.get_calories(num_servings)))
