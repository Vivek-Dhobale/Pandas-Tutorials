"""
droping missing data from dataset

using dropna() method we can remove missing values of the column and rows in the dataset

df.dropna(axis = 0, inplace = True)
"""

import pandas as pd

data = {
    "Name":["Ram", None, "Dhansham", "Ghansham", "Aditi", "Jagdish","Raj", "Sitaram"], 
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

print("Original Dataframe...")
print(df)

print("After Removing Missing values...")
df.dropna(axis=0, inplace=True)
print(df)