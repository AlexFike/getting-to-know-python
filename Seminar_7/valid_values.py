def same_by(characteristic, objects):
    return len(list(filter(characteristic, objects))) == 0


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
