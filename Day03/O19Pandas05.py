
import pandas as pd
import numpy as np

s1 = pd.Series(np.arange(4), index=['a', 'c', 'd', 'e'])
s2 = pd.Series(np.arange(5), index=['a', 'c', 'e', 'f', 'g'])

print(f"s1 :\n{s1}")

print("-" * 60)
print(f"s2 :\n{s2}")

print("-" * 60)
print(f"s1 + s2 :\n{s1 + s2}")

print("-" * 60)

print("DataFrame".center(60, "-"))

df1 = pd.DataFrame(np.arange(6).reshape(2, 3),
                   columns=list("ABC"),
                   index=['tim', 'tom'])

df2 = pd.DataFrame(np.arange(9).reshape(3, 3),
                   columns=list('ACD'),
                   index=['tim', 'kate', 'tom'])

print(f"df1 :\n{df1}")

print("-" * 60)

print(f"df2 :\n{df2}")

print("-" * 60)

print(f"df1 + df2 = \n{df1 + df2}")

print("-" * 60)

print(df1.add(df2, fill_value=0))

print("-" * 60)

print(f"1 / df1 :\n{1 / df1}" )

print("-" * 60)

print(df1 * 3)

print("-" * 60)

print(df1.mul(3))

print("-" * 60)

print(f'df2 :\n{df2}')

print("-" * 60)

print(f"df2.iloc[1] :\n{df2.iloc[1]}")

print("-" * 60)

r2 = df2.iloc[1]

res = df2 - r2

print(f"res :\n{res}")

print("-" * 60)

df = pd.DataFrame(np.random.randn(4, 3),
                  columns=list("ABC"),
                  index=['Kim', 'Susan', 'Tim', 'Tom'])
print(f"df :\n{df}")

print("-" * 60)

print(np.abs(df))

print("-" * 60)

f = lambda x: x.max() - x.min()

print(df.apply(f))

print("-" * 60)

print(df.apply(f, axis=1))

print("-" * 60)

print(df)

print("-" * 60)

def f(x):
    return x ** 2

print(df.apply(f))
