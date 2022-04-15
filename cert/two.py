import pandas as pd
df = pd.read_csv('tst1.csv')
dfu = df.apply(set)
print(dfu)
