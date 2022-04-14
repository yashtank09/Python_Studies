import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

# making data frame from  data file
df = pd.read_csv(r'abc.csv')
df.head()
print(df)
