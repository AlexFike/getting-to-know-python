number_factorial = int(input('Введите число для вычисления факториала: '))

i = 2
factorial = 1

while i <= number_factorial:
    factorial *= i
    i += 1

print(factorial)
