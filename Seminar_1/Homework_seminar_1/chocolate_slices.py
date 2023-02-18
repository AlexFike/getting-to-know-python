
horizontal_size = int(input('Введите размер шоколадки по горизонтали: '))
vertical_size = int(input('Введите размер шоколадки по вертикали: '))

slices = int(input('Введите сколько кусочков вы хотите отломить: '))

if (slices % horizontal_size == 0 or
        slices % vertical_size == 0) and \
        slices != horizontal_size*vertical_size:
    print('Вы можете отломить от шоколадки необходимое количество долек ;)')
else:
    print('Кто-то останется без шоколада :(')
