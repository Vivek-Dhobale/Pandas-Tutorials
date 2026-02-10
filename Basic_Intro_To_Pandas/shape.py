"""
1. How big is your dataset?
2. What are the names of the columns?
Ans.
   shape is the attribute It returns tuple with number of rows and column Ex., (3,4)
   columns is an attribute which returns the names of column as an index object.
"""
import pandas as pd

data = {
    "Name":["Ram", "Sham", "Dhansham", "Ghansham", "Aditi", "Jagdish","Raj", "Sitaram"], 
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

print("Sample Dataframe...")
print(df)

print(f"Shape : {df.shape}")
print(f"Columns : {df.columns}")
print(f"size : {df.size}")