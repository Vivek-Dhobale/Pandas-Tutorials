# accesing specific cell and can perform modifications which do you want using .loc[] method.
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

#df.loc[row_index, "Column_name"] = new_data

#specific cell Updation
df.loc[0, "Salary"] = 55000
print("Specific Cell Updation...")
print(df)

#Entire Column Updation
print("Entire column 'Salary' Updation by 5% ...")
df["Salary"] = df["Salary"] * 1.05
print(df)

