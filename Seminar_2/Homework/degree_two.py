last_number = int(
    input('Введите число до которого нужно вывести все степени двойки: '))
degree = 0

while degree*2 <= last_number:
    degree = 1 if degree == 0 else degree * 2
    print(degree, end=" ")
