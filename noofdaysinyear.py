import calendar
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year%400 == 0:
                return 'leap year'
            else:
                return 'not leap year'
        else:
            return 'leap year'
    else:
        return 'not leap year'
year = int(input('enter year: '))
leap_or_not =leap_year(year)
if leap_or_not == 'leap year':
    print(f'{year} is a leap year')
number_to_month = input('enter month number')
month = int(number_to_month)
no_of_days = calendar.monthrange(year, month)[1]
print(f'the number of days is {no_of_days}')
