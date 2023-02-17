first_class = int(input('Сколько учеников будет в первом классе: '))
second_class = int(input('Сколько учеников будет во втором классе: '))
third_class = int(input('Сколько учеников будет в третьем классе: '))

count_desk = (first_class+1)//2 + (second_class+1)//2 + (third_class+1)//2

print(f'Необходимое количество парт: {count_desk}')
