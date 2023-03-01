from random import randint

# Мое решение:
test_str = input('Введите строку: ')

new_str = ""
temp_str = ""

for i in range(len(test_str)):
    if temp_str.count(test_str[i]) == 0:
        new_str += f"{test_str[i]} "
    else:
        new_str += f"{test_str[i]}_{temp_str.count(test_str[i])} "
    temp_str += test_str[i]

print(new_str)

# Решение в другом зале:
my_dict = {}

for i in test_str:
    my_dict[i] = my_dict.get(i, 0) + 1
    if my_dict[i] == 1:
        print(i, end=" ")
    else:
        print(f'{i}_{my_dict[i]-1}', end=" ")
print()
# Решение преподавателя:

my_list = [i for i in test_str]
my_dict_2 = {}

for i in my_list:
    my_dict_2[i] = my_dict_2.get(i, -1) + 1
    print(i if my_dict_2.get(i) == 0 else f'{i}_{my_dict_2.get(i)}', end=" ")
