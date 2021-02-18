# coding=utf-8
string = 'прелестная строка'

for i, char in enumerate(string):
    if (i == 0 or i % 2 == 0) and char in "а, у, о, ы, и, э, я, ю, ё, е":
        print("Строка мне не нравится!")
        break
else:
    print("Какая хорошая строка!")