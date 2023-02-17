
boarding_train_car = int(input('В какой вагон по счету зашел Витя: '))
train_car_number = int(input('Какой номер у вагона в который зашел Витя: '))

if boarding_train_car == train_car_number:
    print('Недостаточно информация для определения количества вагонов')
else:
    print(
        f'Поезд состоит из {boarding_train_car+train_car_number - 1} вагонов')
