
import pandas as pd

data = {
    'name' : ['Bill', 'Tom', 'Tim', 'John', 'Alex', 'Venessa', 'Kate'],
    'score': [90, 80, 85, 75, 95, 60, 65],
    'sports': ['wrestling', 'football', 'skiing', 'swimming', 'tennis', 'karate', 'surfing'],
    'sex':['m', 'm', 'm', 'm', 'f', 'f', 'f']
}

df = pd.DataFrame(data)

print(f"Data Frame :{df}")

print("-" * 60)

df = pd.DataFrame(data, columns=['name', 'sports', 'sex', 'score'])
print(f"DataFrame :\n{df}")

print("-" * 60)

print(df.head())

print("-" * 60)

print(df.tail())

print("-" * 60)

print(df.head(3))

print("-" * 60)

print(df.tail(3))

print("-" * 60)

df = pd.DataFrame(data, columns=['name', 'sports', 'sex', 'score'],
                  index=['one', 'two', 'three', 'four', 'five', 'six', 'seven'])
print(f"DataFrame :\n{df}")

print("-" * 60)

print(df['sports'])

print("-" * 60)

my_columns = ['name', 'sports']

print(df[my_columns])

print("-" * 60)

print(df.loc[['one']])
print(df.loc[['five']])
print(df.loc[['seven']])

print("-" * 60)

# print(df['age'] == 18)

df = pd.DataFrame(data, columns=['name', 'sports', 'sex', 'score'],
                  index=['one', 'two', 'three', 'four', 'five', 'six', 'seven'])
values = [18, 19, 20, 18, 17, 17, 18]

df['age'] = values

print(f"Dataframe :\n{df}")

print("-" * 60)

df['pass'] = df.score >= 70

print(df)

print("-" * 60)
del df['pass']

print(df)

print("-" * 60)

scores = {'Math': {'A': 85, 'B': 90, 'C': 95}, 'Physics':{'A': '90', 'B': '80', 'C': '75'}}

scores_df = pd.DataFrame(scores)

print(f"Scores :\n{scores_df}")

print("-" * 60)

print(scores_df.T)

print("-" * 60)

scores_df.index.name = "name"
scores_df.columns.name = "lessons"

print(scores_df)

print("-" * 60)

print(scores_df.values)
