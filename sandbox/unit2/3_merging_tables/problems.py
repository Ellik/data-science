from IPython.display import display
import pandas as pd

# есть дубли в файле movies
bad_movies = pd.read_csv('bad_movies.txt', sep='\t')
bad_ratings = pd.read_csv('bad_ratings.txt', sep='\t')
# удалить дубликаты
bad_movies.drop_duplicates(subset='movieId', keep='first', inplace=True)
joined = bad_ratings.merge(bad_movies, on='movieId', how='left')
display(joined)

