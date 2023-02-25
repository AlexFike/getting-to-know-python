from random import randint

test_list = [randint(1, 10) for _ in range(20)]

print(test_list)
print(set(test_list))
print(len(set(test_list)))

