First_name = input('Enter your first name: ')
Second_name = input('Enter your second name:')
percentage = 0
percentage_1 = 0
for i in range(len(First_name)):
    if First_name[i] == 't' or First_name[i] == 'r' or First_name[i] == 'u' or First_name[i] == 'e':
        percentage += 1
    if First_name[i] == 'l' or First_name[i] == 'o' or First_name[i] == 'v' or First_name[i] == 'e':
        percentage_1 += 1
for i in range(len(Second_name)):
    if Second_name[i] == 't' or Second_name[i] == 'r' or Second_name[i] == 'u' or Second_name[i] == 'e':
        percentage += 1
    if Second_name[i] == 'l' or Second_name[i] == 'o' or Second_name[i] == 'v' or Second_name[i] == 'e':
        percentage_1 += 1
z = int(str(percentage) + str(percentage_1))
print(z)
if z<10 and z>90:
    print(f'your z is {z}% and you will be like coke and mentos ')
if z>=40 and z<=50:
    print(f'your z is {z}% and you will be alright together ')

