"""
info() -> method which displays the information of data set

1. number of column,rows ?------------------|
2. what type of data in the column ?        |---> df.info() method is the answer.
3. which column holds missing data ?--------|        |---> number of rows and columns
                                                     |---> column names
                                                     |---> datatype int64,float64,object
                                                     |---> non null counts and memory usage of dataframe

"""
import pandas as pd

df = pd.read_csv("data2.csv", encoding="utf-8")

print("Displaying the info of dataset...")

print(df.info())