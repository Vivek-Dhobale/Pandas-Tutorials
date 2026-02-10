import pandas as pd

data = {
    "Name":["Ram", "Sham", "Dhansham", "Ghansham", "Aditi", "Jagdish","Raj", "Sitaram"], 
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

print("Before Inserting Column...")
print(df)

# inserting data into dataframe using squre brackets df["column"] = some data 
df["Bonus"] = df["Salary"] * 0.1
df["Bonus"].astype("Int64")
print("After Inserting Column...")
print(df)

# Inserting data into dataframe using insert() method syntax., insert(index where you want to insert, column name, some data)
df.insert(0, "Employee ID", [10,20,30,40,50,60,70,80])

print(df)