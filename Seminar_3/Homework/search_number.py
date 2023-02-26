from random import randint

size = int(input('Введите длину списка: '))
my_list = [randint(1, 100) for _ in range(size)]
print(my_list)

number = int(input('Введите число для поиска: '))

if number in my_list:
    print(f'Число {number} встречается в количестве -> {my_list.count(number)}')
else:
    min_def = abs(my_list[0] - number)
    new_number = my_list[0]
    for item in my_list:
        if abs(item - number) < min_def:
            min_def = abs(item - number)
            new_number = item
    print(f'Ближайшее число к {number} это {new_number}'
          f' и встречается оно в количестве -> {my_list.count(new_number)} ')
