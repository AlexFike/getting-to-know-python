from random import randint
from os import system
system('cls')

my_list = [randint(1, 10) for _ in range(int(input('Size list: ')))]
print(my_list)


def older_brother(list_brothers):
    count = 0
    for i in range(-1, len(list_brothers) - 1):
        if list_brothers[i-1] < list_brothers[i] > list_brothers[i+1]:
            count += 1
    return count


print(older_brother(my_list))
