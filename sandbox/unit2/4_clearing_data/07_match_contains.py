import pandas as pd

# str.match ("abc") — ищет строки, которые начинаются c abc,
# str.contains ("abc") — ищет строки, в которых есть abc.
# Обе функции применимы только к объектам Series и не могут
# работать с NaN, необходимо использовать параметр na = False

# sample = pd.read_csv('data/sample.csv')
# filtered_sample = sample[sample.Name.str.match("К", na=False)]
# # filtered_sample = sample[~ sample.Name.str.match("К", na=False)] # ~ inverse
# print(filtered_sample)


# Найдите записи, где в городах есть буква «о», и сохраните в переменную sample3
# sample = pd.read_csv('data/sample.csv')
# sample3 = sample[sample.City.str.contains("о", na=False)]
# print(sample3)

# Найдите записи, где в городах нет буквы "о", и сохраните в переменную
# sample4. Не забудьте про NaN и параметр na:
# sample = pd.read_csv('data/sample.csv')
# sample4 = sample[~sample.City.str.contains("о", na=False)]
# print(sample4)

# Сохраните в переменную new_log датафрейм, из которого удалены
# записи, в которых есть ошибка в поле user_id
log = pd.read_csv("data/log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
new_log = log[~ log.user_id.str.match('#error', na=False)]
print(new_log)
