"""
NaN (Not a Number)
None(for object data type)

isnull() method wich detects null values in dataframe and return boolean dataframe 
True -> values are missing
False -> values are present

"""

import pandas as pd

data = {
    "Name":["Ram", None, "Dhansham", "Ghansham", "Aditi", "Jagdish","Raj", "Sitaram"], 
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

print("Dataframe which contains null values...")
print(df.isnull())

print("\nColumns Containing Null Values...")
print(df.isnull().sum())
