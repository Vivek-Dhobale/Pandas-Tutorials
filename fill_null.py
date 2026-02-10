"""

fillna() method used to fill null/NaN values in dataframe 
df.fillna(value we want to fill, inplace = True)

"""

import pandas as pd 

data = {
    "Name":["Ram","sham", "Dhansham", "Ghansham", "Aditi", "Jagdish","Raj", "Sitaram"], 
    "Age":[28,None,22,30,None,40,25,32],
    "Salary":[None,40000,45000,52000,49000,None,48000,58000],
    "Performance Score":[85,89,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

print("Original Dataframe...")
print(df)

#df.fillna(0, inplace=True)

# print("After filling NaN values...")
# modified_age = df["Age"].fillna(df["Age"].mean())
# print(modified_age)

# df["Age"]= modified_age

print(df)

# filling null values in multiple columns
df = df.fillna({"Age" : df["Age"].mean(), "Salary" : df["Salary"].median()})

print(df)
