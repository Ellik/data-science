import pandas as pd

log = pd.read_csv('data/log.csv', header=None)

print(log[0].unique())
