check_fibonacci = int(input('Введите предполагаемое число Фибоначчи: '))

f1 = 0
f2 = 1
count = 1

while f2 < check_fibonacci:
    f1, f2 = f2, f1+f2
    count += 1

print(count if f2 == check_fibonacci else -1)
