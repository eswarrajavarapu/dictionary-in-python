class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Male(Human):
    def eat(self):
        print('I can eat')
class Female(Male):
    def __init__(self, name, age, can_dance):
        super().__init__(name, age)
        self.can_dance = can_dance
    def sleep(self):
        print('I can sleep')
female = Female('eswar', 21, True)
female.show_details()

