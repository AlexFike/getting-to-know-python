

test = [i for i in range(20)]
print(test)

shift = int(input('Сколько элементов сдвинуть: '))
test_2 = test[shift:] + test[:shift]
print(test_2)
