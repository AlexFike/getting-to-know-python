from random import randint


def replacing_min_max(lst):
    return [min(lst) if i == max(lst) else i for i in lst]


my_lst = [randint(1, 5) for _ in range(10)]
print(my_lst)

print(replacing_min_max(my_lst))
