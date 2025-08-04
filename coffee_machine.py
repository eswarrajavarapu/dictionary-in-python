import coffee_database
resources = {
    'water': 500,
    'milk': 500,
    'coffee': 500,
}
count = 0


def update_resources(numb):
    resources['water'] -= coffee_database.coffee[numb]['water']
    resources['milk'] -= coffee_database.coffee[numb]['milk']
    resources['coffee'] -= coffee_database.coffee[numb]['coffee']
def report():
    print(f'water remaining : {resources["water"]}')
    print(f'milk remaining : {resources["milk"]}')
    print(f'coffee remaining : {resources["coffee"]}')






def insert_coin( name):
    if name == 'latte':
        number = 0
    elif name == 'espresso':
        number = 2
    else:
        number = 1

    cost = 0



    print('please insert coins')
    five = int(input('How many 5Rs. coins:')) #2
    ten = int(input('How many 10Rs. coins:')) #5
    twenty = int(input('How many 20Rs. coins:')) #4
    result = five*5 + ten*10 + twenty*20
    if result == coffee_database.coffee[number]['price']:
        cost += result

        print(f'here is your {name}')
    elif result > coffee_database.coffee[number]['price']:
        change = result - coffee_database.coffee[number]['price']
        print(f'here is your Rs{change} in change')
        print(f'here is your {name}')
    else:
        print("sorry.That's not enough money. Money refunded.")
    update_resources(number)
def check():
    if resources['water'] == 0:
        print('sorry.That is not enough water')
    elif resources['milk'] == 0:
        print('sorry.That is not enough milk')
    elif resources['coffee'] == 0:
        print('sorry.That is not enough coffee')






















end_of_game = False
while not end_of_game:
    choice = input('enter (latte/espresso/cappuccino):')


    if choice == 'latte':
        check()
        insert_coin('latte')




    elif choice == 'espresso':

        check()
        insert_coin('espresso')



    elif choice == 'cappuccino':
         check()
         insert_coin('cappuccino')
    elif choice == 'exit':
        break
    elif choice == 'report':
        report()










































































