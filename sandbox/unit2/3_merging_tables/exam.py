from IPython.display import display
import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Сколько раз была выставлена низшая оценка 0.5 в наших рейтингах? Используйте файл ratings.csv.
# display(ratings[ratings['rating'] == 0.5])

# Объедините датафреймы ratings и movies, используя параметр how='outer'.
# Сколько строк в получившемся датафрейме?
# joined = ratings.merge(movies, on='movieId', how='outer')
# display(joined.count())

# Найдите в датафрейме movies фильм с movieId=3456. Какой у него год выпуска?
joined = movies.merge(ratings, on='movieId', how='left')
display(joined[joined['movieId'] == 3456])

