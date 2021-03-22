# Соединим всё, что мы делали, и очистим файл log.csv. А именно:
# прочитаем файл в переменную log;
# добавим названия колонок user_id, time, bet, win;
# удалим строки, которые содержат значения user_id с ошибками;
# оставим в поле user_id значение типа: "user_N", где N значение идентификатора;
# уберём начальную скобку из поля time.

import pandas as pd
import re

log = pd.read_csv('data/log.csv', header=None)

log.columns = ['user_id', 'time', 'bet', 'win']

log = log[~ log.user_id.str.match('#error', na=False)]


def preparing_user_id(user_id):
    prep = re.search('user_[0-9]+', user_id)
    if prep:
        return prep[0]


log.user_id = log.user_id.apply(preparing_user_id)
log.time = log.time.apply(lambda t: t if pd.isna(t) else str(t).replace('[', ''))
print(log.time.unique())
print(log)



