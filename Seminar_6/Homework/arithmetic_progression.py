from os import system
system('cls')


def arithmetic_progression(number, step, end):
    return [number + step*i for i in range(end)]


element = int(input('Element: '))
step = int(input('Difference: '))
elements_count = int(input('Elements count: '))

print(arithmetic_progression(element, step, elements_count))
