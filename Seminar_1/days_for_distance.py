
dis_car_in_day = int(input('Введите сколько машина проезжает за день(км): '))
distance = int(input('Введите какое расстояние нужно приодолеть(км): '))

days = (distance + dis_car_in_day - 1)//dis_car_in_day

print(f'Для приодоления такого расстояния потребуется дней: {days}')
