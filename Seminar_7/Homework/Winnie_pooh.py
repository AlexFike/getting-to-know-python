from os import system
system('cls')

text = input('A poem by Winnie the Pooh: ')


def valid_rhythm_winnie_pooh(poem: str) -> str:
    # valid_poem = [len([char for char in phrase if char in 'йуеыаоэяию'])
    #                 for phrase in poem.split()]
    valid_poem = [len(tuple(filter(lambda x: x in 'йуеыаоэяию', phrase)))
                  for phrase in poem.split()]
    for i in range(1, len(valid_poem)):
        if valid_poem[0] != valid_poem[i]:
            return 'Пам парам'
    return 'Парам пам-пам'


print(valid_rhythm_winnie_pooh(text))
