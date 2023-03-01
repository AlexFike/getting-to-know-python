text = input('Введите текст: ').lower()
split_char = "!?,.'`;():"

for i in split_char:
    text = text.replace(i, ' ')

print(f'{set(text.split())} => {len(set(text.split()))}')

text_dict = {}
for i in text.split():
    text_dict[i] = text_dict.get(i, 0)+1
print(f'{text_dict} => {len(text_dict)}')
