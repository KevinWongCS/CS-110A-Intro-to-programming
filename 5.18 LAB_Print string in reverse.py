input_text = input('')


reverse_input_text = ''

while not(input_text == 'Done' or input_text == 'done' or input_text == 'd'):
    for i in range((len(input_text) - 1), -1, -1):
        print(input_text[i], end = '')
    print()
    input_text = input('')