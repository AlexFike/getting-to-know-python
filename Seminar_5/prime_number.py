def prime_number(number):
    if number == 1 or number == 0:
        return False
    if not number % 2 and number != 2:
        return False
    for i in range(3, number//2, 2):
        if not number % i:
            return False
    return True


num = int(input('Ведите простое число: '))

print(prime_number(num))
