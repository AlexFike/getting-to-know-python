crane = int(input('Введите общее количество Журавликов: '))

petya_and_sereja = crane//3
katya = crane - petya_and_sereja
sereja = petya_and_sereja//2
petya = sereja

print(f'Журавлики Пети - {petya} '
      f'Журавлики Кати - {katya} '
      f'Журавлики Сережи - {sereja}')
