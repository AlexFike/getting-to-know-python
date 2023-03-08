number = int(input('Введите число: '))

for i in range(1, number):
    fist_sum = sum(j for j in range(1, i) if i % j == 0)
    # сумма всех делителей каждого числа начиная с 1 и заканчивая number = first_sum
    second_sum = sum(k for k in range(1, fist_sum) if fist_sum % k == 0)
    # сумма всех делителей first_sum = second_sum
    if i < fist_sum < number and i == second_sum:
        # число должно быть меньше first_sum и меньше number и
        # число должно ровняться second_sum
        print(i, fist_sum)
        # вывод чисел


def sum_dev(i):
    return sum(j for j in range(1, i//2+1) if i % j == 0)


def friendly_numbers(number):
    result = []
    for i in range(1, number):
        j = sum_dev(i)
        if i > j < number and i == sum_dev(j):
            result.append((i, j))
    return result


print(friendly_numbers(number))
