number = int(input())

if number < 11 or number > 100:
    print("Input must be 11-100")

while number >= 11 and number <= 100:
    print(number)
    number -= 1
    if number % 11 == 0:
        print(number)
        break

