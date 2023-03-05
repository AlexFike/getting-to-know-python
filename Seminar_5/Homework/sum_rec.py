numberA = int(input('Введите первое число: '))
numberB = int(input('Введите второе число: '))


def rec_sum(a, b):
    return a + 1 if b == 1 else rec_sum(a + 1, b - 1)


print(f'Сумма чисел: {rec_sum(numberA, numberB)}')
