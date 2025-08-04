print('welcome to pizza order ')
pizza_order = input('Do you want to order pizza if yes enter/press s or m or l ')
bill = 0
if pizza_order == 's':
    print('price of small pizza is 100')
    bill = 100
elif pizza_order == 'm':
    print('price of medium pizza is 200')
    bill = 200
elif pizza_order == 'l':
    print('price of large pizza is 300')
    bill = 300
add_pepperoni  = input('Do you want to add pepperoni y/n ?')
if add_pepperoni == 'y':
    if pizza_order == 's':
        print('price of pepperoni is 50')
        bill = bill + 50
    if pizza_order == 'm' or pizza_order == 'l':
        print('price of pepperoni is 100')
        bill = bill + 100
else:
    print('no pepperoni is added')
print(f'total bill is {bill}.')

