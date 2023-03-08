from random import randint
from os import system
system('cls')

first_list = [randint(1, 10) for _ in range(int(input('Size first list: ')))]
second_list = [randint(1, 10) for _ in range(int(input('Size second list: ')))]

print(first_list)
print(second_list)

final_list = [i for i in first_list if i not in second_list]

print(final_list)
