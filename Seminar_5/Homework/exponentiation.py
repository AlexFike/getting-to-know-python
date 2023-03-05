
valid = True

while valid:
    try:
        number = int(input('Введите число возводимое в степень: '))
        degree = int(input('Введите степень: '))
        valid = False
    except:
        print('Вы ввели неверные параметры! Попробуйте еще раз.')


def exponentiation(number, degree):
    return number if degree == 1 else number * exponentiation(number, degree - 1)


dict_print_utf8 = {1: '¹', 2: '²', 3: '³', 4: '⁴',
                   5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹', 0: '⁰'}

print(f'{exponentiation(number, degree)}({number}', end='')
for i in str(degree):
    print(dict_print_utf8.get(int(i)), end='')
print(')')
