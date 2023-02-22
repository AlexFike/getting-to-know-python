
numbers_sum = int(input('Введите сумму чисел: '))
numbers_multi = int(input('Введите произведение чисел: '))

first_number = None
second_number = None

for i in range(1, numbers_sum):
    if (numbers_sum - i) * i == numbers_multi:
        first_number = i
        second_number = numbers_sum - i
        break

print('Подсказки не верны!' if first_number == None else
      f'{first_number} и {second_number} - загаданные числа')
