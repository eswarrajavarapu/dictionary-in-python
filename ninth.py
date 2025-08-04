import os
print('welcome to silent auction program')
end_of_game = False
dict1 = {}
name = ''
x = 0

while not end_of_game:
    name = input('enter your name: ')
    bid_price = int(input('enter your bid price: '))
    dict1[name] = bid_price



    check_bidders = input('Are there any bidders')
    if check_bidders == 'yes':

        os.system('cls')

    elif check_bidders == 'no':

        for bidder_info in dict1:
            if dict1[bidder_info]> x:
                name = bidder_info

                x = dict1[bidder_info]

        print(f'highest bid is {x} and name is {name}')
        end_of_game = True







