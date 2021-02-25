from IPython.display import display
import pandas as pd

# df = pd.DataFrame({
#     'col1': [1, 2],
#     'col2': [3, 4]
# })

# display(df)

df = pd.read_csv('../data_sf.csv')

# display(df.head(5))  # tail()
# display(df.info())  # Детальная информация
# display(df.describe())  # describe(include=['object']) детальная информация по конкретному типу

# вывод всей информации
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     display(df.describe())
# display(df.describe(include=['object']))

# выяисляем через конкретные столбцы
# print(round(df['Age'].mean()))  # средний возраст игроков
# print(round(df['Composure'].count()))
# print(round(df['ShortPassing'].std(), 2))
# print(round(df['Wage'].sum()))
# print(round(df['Value'].min()))

# Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых
# выше среднего? Ответ округлите до сотых.
# res = df[df.Wage > df.Wage.mean()].SprintSpeed.mean()
# print(round(res, 2))

# res = df[(df.Composure > 90) & (df.Reactions > 90)].Age.min() todo ?
# print(res)

# Из какой страны (Nationality) происходит больше всего игроков, чья
# стоимость (Value) превышает среднее значение? todo Классное решение!
# res = df[df.Value > df.Value.mean()]
# print(res.describe(include=['object']))

# Определите, во сколько раз средняя сила удара (ShotPower) самых
# агрессивных игроков (игроков с максимальным значением
# показателя "Агрессивность" (Aggression)) выше средней силы удара
# игроков с минимальной агрессией. Ответ округлите до сотых.
res = df[df.Aggression == df.Aggression.max()].ShotPower.mean()
res1 = df[df.Aggression == df.Aggression.min()].ShotPower.mean()
print(res / res1)
