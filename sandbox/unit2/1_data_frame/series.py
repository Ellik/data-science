import pandas as pd

data = pd.Series(list(range(10, 1001)))
res = data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122]
print(res)
