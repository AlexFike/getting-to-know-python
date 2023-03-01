from random import randint
size = randint(10, 20)
first_list = [str(randint(1000, 10000)) for _ in range(size)]
print(first_list)

number = input('Введите цифру: ')
second_list = [i.replace(number, '') for i in first_list
               if len(i.replace(number, '')) > 0]
print(second_list)

third_list = []
for i in second_list:
    temp = sum(int(j) for j in i)
    while temp > 9:
        temp = temp//10+temp % 10
    third_list.append(temp)
print(third_list)


final_list = list(set(third_list))
print(final_list)
