import random
names = input("Enter everybody's name seperated by comma:")
z = names.split(',')
print(z)
a = random.randint(0, len(z)-1)
print(f'{z[a]} will pay the bill')
