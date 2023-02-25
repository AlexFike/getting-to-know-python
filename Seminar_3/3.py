from random import randint

test = [randint(1, 10) for _ in range(20)]
print(test)
# test_set = set(test)
# for item in test_set:
#     test.remove(item)
# set_2 = set(test)
# set_3 = list(test_set.difference(set_2))

new_list = [i for i in test if test.count(i) == 1]

print(new_list)
