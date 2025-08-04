list_numbers = input('Enter the list of numbers:')
new_list = list_numbers.split(',')
print(new_list)
maximum = 0
for number in new_list:
    X = int(number)
    if X > maximum:
        maximum = X
print(f'the maximum number is {maximum}')


