import pandas as pd 

data = {
    "Name":["Ram", "Sham", "Dhansham", "Ghansham", "Aditi", "Jagdish","Raj", "Sitaram"], 
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

print("Original Dataframe...")
print(df)


# # df.drop(columns = ["Performace Score"], inplace=True)
# # Removing Single Column from dataframe 

# print("Single Column Removed...")
# df.drop(columns = ["Performance Score"], inplace=True)
# print(df)


# Removing Multiple Columns from Dataframe
print("Multiple Columns Removed...")
df.drop(columns = ["Performance Score","Age"], inplace=True)
print(df)