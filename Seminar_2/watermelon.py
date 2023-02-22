from random import randint

watermelon_count = int(input('Введите количество продаваемых арбузов: '))

start_rnd, end_rnd = 1, 10

min_wt, max_wt = end_rnd, start_rnd

for i in range(watermelon_count):
    watermelon_wt = randint(start_rnd, end_rnd)
    print(watermelon_wt, end=', ')
    if watermelon_wt > max_wt:
        max_wt = watermelon_wt
    if watermelon_wt < min_wt:
        min_wt = watermelon_wt

print(f'\nВес арбуза для себя => {max_wt}'
      f'\nВес арбуза для тещи => {min_wt}')
