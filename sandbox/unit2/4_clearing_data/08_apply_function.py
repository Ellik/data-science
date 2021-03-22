import pandas as pd
import re

sample = pd.read_csv('data/sample.csv')


# С помощью apply и лямбда-функции увеличьте возраст во всех записях
# на 1 год и сохраните в sample2. В переменной sample2 должен содержаться
# весь датафрейм sample.
# sample2 = sample
# sample2.Age = sample2.Age.apply(lambda x: x + 1)
# print(sample2)

# С помощью apply и lambda-функции замените все буквы в поле City на
# маленькие и сохраните в sample2. Вам может понадобиться функция s.lower().
# Обратите внимание: когда в столбце есть пропущенные значения, необходимо
# в явном виде указывать, что это str (lambda s: str(s).lower())
# sample2 = sample
# sample2.City = sample2.City.apply(lambda s: str(s).lower())
# print(sample2)

# Напишите функцию profession_code, которая на вход получает строку, а на
# выход возвращает:
# 0 — если на вход поступила строка "Рабочий"
# 1 — если на вход поступила строка "Менеджер"
# 2 — в любом другом случае
# Примените функцию profession_code для того, чтобы заменить поле Profession с
# помощью apply. Сохраните получившийся датафрейм в переменную sample2.
# def profession_code(s):
#     if s == 'Рабочий':
#         return 0
#     elif s == 'Менеджер':
#         return 1
#     else:
#         return 2
#
#
# sample2 = sample
# sample2.Profession = sample2.Profession.apply(profession_code)
# print(sample2)

# Напишите функцию age_category, которая на вход получает число, а на выход
# отдаёт:
# "молодой" — если возраст меньше 23
# "средний" — если возраст от 23 до 35
# "зрелый" — если возраст больше 35
# Примените функцию age_category и apply, чтобы создать новую колонку в sample
# под названием 'Age_category'. Не забудьте загрузить датафрейм
# def age_category(age):
#     if age < 23:
#         return 'молодой'
#     elif age >= 23 & age <= 35:
#         return 'средний'
#     else:
#         return 'зрелый'
#
#
# sample['Age_category'] = sample.Age.apply(age_category)
# print(sample)


# Преобразуем поле user_id в датафрейме log, оставив только идентификатор
# пользователя. Например, вместо "Запись пользователя № — user_974" должно
# остаться только "user_974".
# На месте записей с ошибками в user_id должна быть пустая строка "". Сделайте
# это через apply и новую функцию, которую вы создадите. Результат сохраните в log:
# log = pd.read_csv('data/log.csv', header=None)
# log.columns = ['user_id', 'time', 'bet', 'win']
#
#
# def filtering_user_ids(user_id):
#     if '#error' in user_id:
#         return ""
#     else:
#         prep_user_id = re.search('user_[0-9]+', user_id)
#         if prep_user_id:
#             return prep_user_id[0]
#
#
# log.user_id = log.user_id.apply(filtering_user_ids)
# print(log)


# Загрузите log.csv в log. Удалите квадратную скобку из первой строки в столбце
# time, чтобы привести его к более привычному формату: t равен log.time[0]. Сохраните результат в t:
# NaN ПРОПУСКАЕМ
log = pd.read_csv('data/log.csv', header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
log.time = log.time.apply(lambda t: t if pd.isna(t) else str(t).replace('[', ''))
print(log)

