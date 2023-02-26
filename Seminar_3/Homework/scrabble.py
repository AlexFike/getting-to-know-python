dict_eng = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
            'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'D': 2,
            'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4,
            'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8,
            'X': 8, 'Q': 10, 'Z': 10}

dict_rus = {'А': 1, 'В': 1, 'Е': 1, 'И': 1,
            'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
            'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
            'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
            'Й': 4, 'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
            'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10}

valid_select_dict = True

while (valid_select_dict):
    language = input('На каком языке будет слово(english, русский): ').lower()
    valid_select_dict = False if language == 'english' or \
        language == 'русский' else print('Язык выбран не правильно!')

use_dict = dict_eng if language == 'english' else dict_rus

word = input('Введите слово: ').upper()

point_word = sum(use_dict[item] for item in word if use_dict.get(item))

print(f'Ваше количество очков: {point_word}')
