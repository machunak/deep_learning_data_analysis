import pandas as pd

s = pd.Series([1, 3, 5, 7])
print(s)

print(s.index)
print(s.values)

print(s[0])
print(s[3])

s.index = ['a', 'b', 'c', 'd']
print(s)

print('-' * 30)

data = {
    'city': ['mokpo', 'mokpo', 'mokpo', 'pusan', 'pusan', 'pusan'],
    'year': [2021, 2022, 2023, 2021, 2022, 2023],
    'population': [300, 400, 350, 250, 300, 350]
}

df = pd.DataFrame(data)
print(df)
print(df.index)
print(df.columns)
print(df.values)

df.index = list('abcdef')

print(df['city'])
print(df.iloc[0])
print(df.loc['a'])

print(df.iloc[:3])

print(df.iloc[3:6])