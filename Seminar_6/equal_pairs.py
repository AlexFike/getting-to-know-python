from random import randint
from os import system
system('cls')

my_list = [randint(1, 10) for _ in range(int(input('Size list: ')))]
print(my_list)


def equal_pairs(check_list):
    result = 0
    for i in set(check_list):
        result += check_list.count(i) // 2
    return result


print(equal_pairs(my_list))
