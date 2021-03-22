import pandas as pd

users = pd.read_csv('data/users.csv', encoding="koi8_r", delimiter="\t")
users.columns = ['user_id', 'email', 'geo']
print(users)
