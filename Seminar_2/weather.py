from random import randint

days = int(input('Введите число дней: '))

count_max = 0
count = 0
temperature_day = 0

for i in range(days):

    temperature_day = temperature_day + randint(-4, 4)
    print(temperature_day, end=", ")

    if temperature_day > 0:
        count += 1
    else:
        count = 0
    if count > count_max:
        count_max = count


print(f'\n{count_max}')
