proverb = 'Программисты - это устройства, преобразующие кофеин в код.'

new_proverb = ''

for s in range(0, len(proverb) - 1, 2):
    idx = s
    nextIdx = s + 2
    piece = proverb[idx: nextIdx]
    flip = piece[::-1]
    new_proverb = new_proverb + flip

print(new_proverb)