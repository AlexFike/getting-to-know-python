ticket = input('Введите номер билета: ')

if int(ticket[0])+int(ticket[1])+int(ticket[2]) == \
   int(ticket[3])+int(ticket[4])+int(ticket[5]):
    print('Поздравляю! У вас счастливый билет =)')
else:
    print('Вам не повезло, у вас не счастливый билет =(')
