import pandas as pd
# sorting data in dataframe
# sort_values() method is used to sort the data in dataframe by the values of a specific column
# df.sort_values(by = "column name", ascending = True/False, inplace = True)

data = {
    "Name": ["Ram", "Sham", "Dhansham", "Ghansham", "Aditi", "Jagdish","Raj", "Sitaram"],
    "Age": [28, 24, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 40000, 45000, 52000, 49000, 70000, 48000, 58000]
}

df  = pd.DataFrame(data)
print("Original Dataframe...")
print(df)

# print("Sorting by Age in ascending order...")
# df.sort_values(by="Age", ascending = True, inplace = True)
# print(df)

# sorting by multiple columns
print("Sorting by Salary in descending order and Age in ascending order...")
df.sort_values (by=["Salary", "Age"], ascending  = [False, True], inplace = True)
print(df)