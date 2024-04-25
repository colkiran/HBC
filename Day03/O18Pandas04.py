
import pandas as pd
import numpy as np

obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])

print(f"DataSeries :\n{obj}")

print("-" * 60)

print(f"obj['c'] :{obj['c']}")

print("-" * 60)

print(f"obj[2] :{obj[2]}")

print("-" * 60)

print(f"obj[0:3] :\n{obj[0:3]}")

print("-" * 60)

print(f"obj[['a', 'c']] :\n{obj[['a', 'c']]}")

print("-" * 60)

print(f"obj['b':'e'] :\n{obj['b':'e']}")

print("Data Frame".center(60, "-"))

data = pd.DataFrame(
    np.arange(16).reshape(4, 4),
    index=["Blr", "Che", "Hyd", "Mum"],
    columns=['one', 'two', 'three', 'four']
)

print(f"data: \n{data}")

print("-" * 60)

print(data['two'])

print("-" * 60)

print(data[['one', 'two']])

print("-" * 60)

print(data[:3])

print("-" * 60, "\n")

print(data[data["four"]>5])

print("-" * 60)

data[data<5]=0

print(data)

print("-" * 60)

print(data)

print("-" * 60)

print(data.iloc[1])     # first row from the series

print("-" * 60)

print(data.iloc[1, [1, 2, 3]])

print("-" * 60)

print(data.iloc[[1, 3], [1, 2, 3]])

print("-" * 60)

print(data.loc['Che', ['one', 'two']])

print("-" * 60)

print(data.loc[:'Che', 'four'])

print("-" * 60)

print(data.iloc[-1])
