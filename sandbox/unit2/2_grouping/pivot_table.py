import pandas as pd
from IPython.display import display

df = pd.read_csv('../data_sf.csv')

# pivot = df[df['Club'].isin(['FC Barcelona', 'Real Madrid', 'Juventus', 'Manchester United'])].pivot_table(
#     values=['Wage'],
#     index=['Nationality'],
#     columns=['Club'],
#     aggfunc='sum',
#     margins=True,
#     fill_value=0
# )

#  если указали массив столбцов при конфигурации (['Wage']), то его нужно явно указать при доступе к значениям
# display(pivot.loc['Argentina']['Wage']['Manchester United'])

#  тут столбец дефолтный, поэтому указывать его явно не нужно
# df2 = df.pivot_table(columns="Position", index='Club', values='Wage', aggfunc='max')
# display(df2.loc['Manchester United']['GK'])

# Используя таблицу, созданную на предыдущем шаге, определите, сколько клубов не содержат
# данных о центральных полузащитниках. (CM)
# pivot = df.pivot_table(
#     values='Name',
#     index='Position',
#     columns='Club',
#     aggfunc='count',
#     fill_value=0
# )
#
# filtered = pivot.loc['CM']
# print(filtered[filtered == 0].count())  # можно так
# print(filtered.value_counts().sort_index())  # или так

# С помощью сводной таблицы и функции loc посчитайте, сколько
# получают ("Wage") русские футболисты ("Russia"), играющие за ФК "AS Monaco".
# pivot = df.pivot_table(
#     values='Wage',
#     index='Nationality',
#     columns='Club',
#     fill_value=0,
#     aggfunc='sum'
# )
#
# display(pivot.loc['Russia']['AS Monaco'])

# Создайте сводную таблицу, содержащую сведения о средней скорости футболистов (SprintSpeed), занимающих
# разные позиции (Position) в разных футбольных клубах (Club).
# Основываясь на данных таблицы, отметьте три позиции, представители которых
# в среднем обладают самой высокой скоростью.

# pivot = df.pivot_table(
#     columns='Position',
#     index='Club',
#     values='SprintSpeed',
#     aggfunc='mean',
#     fill_value=0
# )
# display(pivot.max().sort_values(ascending=False))

# Используя таблицу, созданную на предыдущем шаге, отметьте названия
# трёх клубов, в которых центральные форварды (ST) обладают наибольшей средней скоростью.
pivot = df.pivot_table(
    columns='Position',
    index='Club',
    values='SprintSpeed',
    aggfunc='mean',
    fill_value=0
)

display(pivot['ST'].sort_values(ascending=False))
