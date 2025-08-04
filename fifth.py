first_row = input('Enter the first row containing three numbers seperated by comma')
second_row = input("Enter the second row containing  three numbers seperated by comma")
third_row = input('Enter the third row containing three numbers seperated by comma')
list1 = first_row.split(',')
list2 = second_row.split(',')
list3 = third_row.split(',')
list_0 = [list1, list2, list3]
row = int(input('Enter the row number'))
column = int(input('Enter the column number'))
list_0[row-1][column-1] = 'X'


print(f'{list_0[0]}\n{list_0[1]}\n{list_0[2]}')




