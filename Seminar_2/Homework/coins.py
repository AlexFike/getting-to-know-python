from random import randint

count_coins = int(input('Введите количество монеток: '))

head = 0
tail = 0

for _ in range(count_coins):
    coin = randint(0, 1)
    if coin == 1:
        head += 1
    else:
        tail += 1


print(tail if tail < head else head)
