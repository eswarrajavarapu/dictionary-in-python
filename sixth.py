list_heights = input('Enter the list of heights seperated by comma: ')
new_list = list_heights.split(',')
print(new_list)
sum1= 0
length = 0
for i in new_list:
    length += 1
print(length)
for i in range(length):
    x = int(new_list[i])
    sum1 += x
print(sum1)
total = sum1/length
print(total)

