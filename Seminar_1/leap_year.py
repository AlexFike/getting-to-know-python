
number_year = int(input('Введите номер года: '))

if number_year % 400 == 0 or number_year % 100 != 0 and number_year % 4 == 0:
    print('Год является високосным')
else:
    print("Год не високосный")
