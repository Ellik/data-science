import pandas as pd

sample = pd.read_csv('data/sample.csv')
# df.columns = ['new_col_name_1', 'new_col_name_2', 'new_col_name_3', 'new_col_name_4']

# Создайте в sample заголовки колонок так, чтобы там были только маленькие
# буквы. Например, вместо 'Age' нужно сделать 'age':
columns = sample.columns
lowerColumns = []
for column in columns:
    lowerColumns.append(column.lower())
sample.columns = lowerColumns

print(sample)