"""
1 -> select specific column 
2 -> filter rows
3 -> combine multiple conditions

use Square brackets
boolean conditions 

selecting columns
1-> a Series
2-> Dataframe which holds multiplecolumns of Data

column = df["column name"]
subset = df["column1", "column2", "..."]


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

# Selecting specific column (single column return series)

name = df["Name"]
print(" Name (Single column return Series)")
print(name)

# Selecting multiple columns (multiple columns return Dataframe)

subset = df[["Name", "Age"]]
print("\nName & Age (multiple column return Dataframe)")
print(subset)

#