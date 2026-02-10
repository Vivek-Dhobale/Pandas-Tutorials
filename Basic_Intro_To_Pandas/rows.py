"""
head(n) -> It displays the n number of rows in the dataframe deafult value is 5
tail(n) -> It displays dataframes n number last rows  deafult value is 5

"""

import pandas as pd

df = pd.read_csv("data2.csv", encoding="utf-8")

print("Display first three rows...")
print(df.head(3))

print("Display last three rows...")
print(df.tail(3))



