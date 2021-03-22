import pandas as pd

# Создайте новый датафрейм sample2, в который будут входить только записи о людях в возрасте меньше 30 лет.
# sample = pd.read_csv('data/sample.csv')
# sample2 = sample[sample.Age < 30]
# print(sample2)

# Создайте новый датафрейм log_win, в который будут входить только записи, где
# пользователь выиграл. Посчитайте, сколько таких записей, и сохраните в переменной win_count.
# log = pd.read_csv("data/log.csv", header=None)
# log.columns = ['user_id', 'time', 'bet', 'win']
# log_win = log[log.win == log.win]  # IF WIN NOT NAN!!!
# win_count = log_win.count()['user_id']
# print(win_count)
# Создайте новый датафрейм sample2, в который будут входить только записи о рабочих младше 30 лет.
# sample = pd.read_csv('data/sample.csv')
# sample2 = sample[(sample.Age < 30) & (sample.Profession == 'Рабочий')]
# print(sample2)
