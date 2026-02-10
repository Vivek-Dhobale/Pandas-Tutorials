"""
filtering rows / boolean indexing 

1 -> based on a single condition 
filtered_rows = df[df["Salary"] > 50000 ]

2 -> based on multiple conditions
filtered_rows = df[(df["Salary"] > 50000) & (df["Salary"] < 80000)]

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

# Filtering Rows Based on Single Condition
print("\nPersons who's Salary greater than 50000")

filtered_rows = df[df["Salary"] > 50000]

print(filtered_rows)

# Filtering Rows Based on Multiple Conditions
print("\nPersons who's Age are Greater than 30 & Performance Score Greater than 80")

filtered_rows2 = df[(df["Age"] > 30) & (df["Performance Score"] > 80)]

print(filtered_rows2, end="\n\n")

# Using OR Condition
filtered_or = df[(df["Age"] > 30) | (df["Performance Score"] > 90)]
print(filtered_or)
