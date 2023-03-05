def fibonacci(number):
    return 0 if number == 0 else 1 if number == 1 else fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(7))
