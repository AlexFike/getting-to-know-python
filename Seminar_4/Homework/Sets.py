from random import randint

first_num = int(input('Размер первого множества: '))
second_num = int(input('Размер второго множества: '))


# first_lst = [int(input(f'Введите число {i+1} первого множества: '))
#              for i in range(first_num)]
# second_lst = [int(input(f'Введите число {i+1} второго множества: '))
#               for i in range(second_num)]

first_lst = [randint(1, 20) for _ in range(first_num)]
second_lst = [randint(1, 20) for _ in range(second_num)]

print(first_lst)
print(second_lst)

result = sorted(list(set(first_lst).intersection(set(second_lst))))

print(result)
