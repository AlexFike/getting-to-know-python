from random import randint

flowerbed = [randint(1, 9) for _ in range(10)]
print(flowerbed)


def MaxSumSequences(lst, sequence):
    result = temp = sum(lst[:sequence - len(lst)])
    for i in range(len(lst)-1):
        # print(f'{result} - {lst[i]}[{i}] + '
        #       f'{lst[sequence - len(lst)+i]}[{sequence - len(lst)+i}]')
        temp = temp - lst[i] + lst[sequence - len(lst)+i]
        result = max(temp, result)
    return result


print(MaxSumSequences(flowerbed, 3))
