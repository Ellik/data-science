from IPython.display import display
import pandas as pd

df = pd.read_csv('data_sf.csv')
df_prep = df[df.columns[1:8]].head(25)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     display(df_prep)

# Предположим, что перед нами стоит задача быстро оценить, сколько
# футболистов относится к каждой из представленных национальностей.

# temp = df_prep['Nationality'].value_counts()  # кол-во игроков в каждой строне
# display(temp)
# print(temp.index[0])  # страна в в которой больше всего игроков
# display(temp.loc[temp > 1])  # показать те стрраны где кол-во игроков > 1

# temp = df['Position'].value_counts(normalize=True) # вывести в процентнтном соотношении
# print(temp)


# Из-за того, что цифры зарплат повторяются не часто , трудно
# сделать какие-то выводы. Но всё будет более наглядно, если мы
# разобьем весь возможный диапазон зарплат на 4 равных промежутка и
# подсчитаем количество футболистов, попадающих в каждый из промежутков. Именно
# для этого нужен параметр bins:
# temp = df['FKAccuracy'].value_counts(bins=5)  # вывести в процентнтном соотношении
# print(temp)
# temp_to_df = temp.reset_index()
# temp_to_df.columns = ['Диапозон попаданий', 'Кол-во игроков']
# display(temp_to_df)


# У какого процента испанских футболистов (Nationality = 'Spain')
# зарплата (Wage) находится в пределах 25% минимума от наблюдаемого
# уровня зарплат среди испанских игроков? Ответ дайте в
# виде целого числа (округлите полученный результат) без знака %.
# filtered = df[df.Nationality == 'Spain']
# res = filtered['Wage'].value_counts(bins=4, normalize=True)
# print(res)

# Укажите количество национальностей (Nationality), к которым относятся
# футболисты, выступающие за клуб (Club) "Manchester United"
# filtered = df[df.Club == 'Manchester United']
# res = filtered['Nationality'].nunique()
# print(res)

# С помощью функции unique определите двух футболистов из Бразилии (Nationality = 'Brazil'), выступающих
# за клуб (Club) 'Juventus'. Перечислите их имена (Name, как в датафрейме)
# через запятую в алфавитном порядке.
# filtered = df[(df.Nationality == 'Brazil') & (df.Club == 'Juventus')]
# res = filtered['Name'].unique()
# print(res)

# Укажите, какой из клубов (Club) насчитывает большее количество
# футболистов возрастом (Age) старше 35 лет
# filtered = df[df.Age > 35]
# res = filtered['Club'].value_counts()
# print(res)

# С помощью функции value_counts с параметром bins разбейте всех футболистов
# родом из Аргентины (Nationality = 'Argentina') на 4 равные
# группы по возрасту. Сколько футболистов в возрасте от 34,75 до 41 года в сборной Аргентины?
# filtered = df[df.Nationality == 'Argentina']
# res = filtered['Age'].value_counts(bins=4)
# print(res)

# Сколько процентов футболистов из Испании (Nationality = 'Spain') имеют
# возраст (Age) 21 год? Введите с точностью до 2 знаков после запятой
# без указания знака % (например, 12.35).
# filtered = df[df.Nationality == 'Spain']
# res = filtered['Age'].value_counts(normalize=True)
# print(res)

####################
# ####GROUPBY#######
####################
# Отметьте позиции (Position), по которым общая сумма зарплат (Wage)
# игроков превышает 5 млн евро в год.
# grouped = df.groupby(['Position'])['Wage'].sum()
# display(grouped[grouped > 5000000].sort_values(ascending=False))

# Посчитайте среднюю зарплату (Wage) и цену (Value) игроков разных позиций (Position).
# Представители какой позиции имеют самую высокую среднюю ценность?
# Какова средняя зарплата футболистов на данной позиции?
# grouped = df.groupby(['Position'])[['Wage', 'Value']].mean()
# print(grouped.sort_values('Value', ascending=False).head(10))

# Посчитайте среднюю (mean) и медианную (median) зарплату (Wage)
# футболистов из разных клубов (Club). В скольких клубах средняя и медианная зарплаты совпадают?
# grouped = df.groupby(['Club'])['Wage'].agg(['mean', 'median'])
# grouped = grouped[grouped['mean'] == grouped['median']]
# indexes = grouped.index
# print(len(indexes))

# Определите максимальную зарплату футболиста национальности
# (Nationality) Аргентина ("Argentina") в возрасте 20 лет.
# grouped = df[(df['Nationality'] == 'Argentina') & (df['Age'] == 20)].groupby(['Nationality'])[['Wage']].min()
# print(grouped)

# Определите максимальную силу (Strength) и баланс (Balance) среди игроков
# клуба (Club) "FC Barcelona" из Аргентины ("Argentina"). Ответ введите через
# точку с запятой без пробела.
# filtered = df[(df['Club'] == 'FC Barcelona') & (df['Nationality'] == 'Argentina')]
# grouped = filtered.groupby(['Club'])[['Strength', 'Balance']].max()
# print(grouped)
