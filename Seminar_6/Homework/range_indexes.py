from random import randint
from os import system
system('cls')

my_list = [randint(1, 100) for _ in range(int(input('Size list: ')))]
print(my_list)


def range_indexes(check_list, start, end):
    return [i for i in range(len(check_list)) if start < check_list[i] < end]


start = int(input('Start range: '))
end = int(input('End range: '))

print(range_indexes(my_list, start, end))
