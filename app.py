"""
Why do we need to explore data?
1 -> Understand the data set 
2 -> Identify the problems
3 -> plan next steps

"""
import pandas as pd 

df = pd.read_csv("data2.csv", encoding="utf-8")
print(df)

# gcsfs library to read the cloud data 