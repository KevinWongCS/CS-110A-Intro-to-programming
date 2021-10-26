def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100
    num_quarters = user_total // 25
    user_total %= 25
    num_dimes = user_total // 10
    user_total %= 10
    num_nickels = user_total // 5
    user_total %= 5
    num_pennies = user_total
    ### TEST ####
    # print(num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)
    ### TEST ####
    #### NOTE: THIS IS THE REASON WHY FIRST FEW ATTEMPTS DIDN'T WORK ####
    return (num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)

def coin_singular_plural_printer(list):
    index = 0
    coin_singular = ['dollar', 'quarter', 'dime', 'nickel', 'penny']
    coin_plural = ['dollars', 'quarters', 'dimes', 'nickels', 'pennies']
    index = 0
    for number in list:
        if number == 0:
            index += 1
        elif number == 1:
            print(str(number) + ' ' + coin_singular[index])
            index += 1
        elif number > 1:
            print(str(number) + ' ' + coin_plural[index])
            index += 1

if __name__ == '__main__':
    input_val = int(input())
    if input_val == 0:
        print('no change')
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
        num_coins_list = []
        num_coins_list.append(num_dollars)
        num_coins_list.append(num_quarters)
        num_coins_list.append(num_dimes)
        num_coins_list.append(num_nickels)
        num_coins_list.append(num_pennies)
        ### TEST ####
        # print(num_coins_list)
        ### TEST ####
        coin_singular_plural_printer(num_coins_list)