import os
import re
import pandas as pd

# Создайте на основе списка files новый список data, в который поместите только файлы, содержащие в названии "txt".
# files = ['setup.py', 'ratings.txt', 'stock_stats.txt', 'movies.txt', 'run.sh', 'game_of_thrones.mov']
# data = []
# for file in files:
#     if re.compile('.txt$').search(file):
#         data.append(file)
# print(data)


files = os.listdir('data')

total_df = pd.DataFrame(columns=['userId', 'movieId', 'rating', 'timestamp'])
for file in files:
    temp = pd.read_csv(os.path.join('data', file), names=['userId', 'movieId', 'rating', 'timestamp'])
    total_df = pd.concat([total_df, temp])

print(total_df)
