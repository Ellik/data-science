import pandas as pd

# С помощью функции query найдите тех, у кого ставка меньше 2000, а выигрыш
# больше 0. Сохраните в новый датафрейм log2.

log = pd.read_csv("data/log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win']

log2 = log.query('bet < 2000 & win > 0')

print(log2)
