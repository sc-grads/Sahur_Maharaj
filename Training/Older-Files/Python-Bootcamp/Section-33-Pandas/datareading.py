import pandas as pd

data = list(range(2, 11, 2))

s1 = pd.Series(data)

print(s1)

lables = ['a', 'b', 'c', 'd', 'e']
s2 = pd.Series(data=data, index=lables)

print(s2)

# orderd items only are acceptable for serises

print(s1[2])
print(s2 + s1)

# data Frames
data = [['Dan', 30, 40000], ['John', 40, 50000],
        ['Helen', 35, 60000], ['Marry', 29, 58000]]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Salary'])
print(df)
type(df), type(df['Name'])  # => (pandas.core.frame.DataFrame, pandas.core.series.Series)
print(df.shape)  # <-- rows and cells
print(df['Name'])
print(df[['Name', 'Salary']])
# add column
df['Phone'] = ['11111', '22222', '33333', '44444']
df.drop(2, 0)
df.drop('Age', axis=1)
df.drop('Age', axis=1, inplace=True)
df.rename(columns={'Name': 'First Name', 'Salary': 'Annual Salary'}, inplace=True)

x = df.loc[0]
print(x)
print(df.loc[1, 'Name'])
type(df.loc[0])
print(df.loc[0:2])
print(df.loc[[0, 1, 3], ['Name', 'Annual Salary']])
print(df.loc[0:2, ['Name', 'Mobile Phone']])
print(df.loc[:, ['Name', 'Annual Salary']])
print(df.iloc[0])
print(df.iloc[0, 1])
print(df.iloc[0:3])
print(df.iloc[3, 0:2])
print(df.iloc[[1, 3], 0:2])
df.sample()
df.sample(n=2)
df.sample(frac=0.2)
dict(zip(df['Name'], df['Age']))


