def reverse(numbers):
    element = int(input('Введите число: '))
    if numbers == 1:
        print(element, end=" ")
        return
    else:
        reverse(numbers-1)
        print(element, end=" ")


reverse(5)
