import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
},
                  index=['a', 'b', 'c', 'd', 'e'])

print(df)
print(type(df))
print(df.values)  # df.values can be used to convert pandas df to numpy arrays
print(type(df.values))
