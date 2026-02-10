"""
aggregation is the process of combining multiple values into a single value. It is used to summarize data and to find patterns in data.
aggregation methods
1 -> sum, 2 -> mean, 3 -> median, 4 -> min, 5 -> max, 6 -> count, 7 -> std, 8 -> var 
groupby() method is used to group the data by a specific column and then apply the aggregation method on the grouped data.  
df.groupby("column name").agg({"column name" : "aggregation method"})   

"""

import pandas as pd

data = {
    "Name": ["Ram", "Sham", "Dhansham", "Ghansham", "Aditi", "Jagdish","Raj", "Sitaram"],
    "Age": [28, 24, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 40000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Department": ["HR", "IT", "IT", "HR", "Finance", "Finance", "IT", "HR"] 
}

df = pd.DataFrame(data) 
print("Original Dataframe...")
print(df)   

# group by department and calculate the mean salary of each department
print("Mean Salary of each department...")  
grouped = df.groupby("Department")["Salary"]
mean_salary = grouped.mean()
print(mean_salary)

# groupby multiple columns and calculate the mean salary of each department and age group
print("Mean Salary of each department and age group...")

grouped = df.groupby(["Department", "Age"])["Salary"]
mean_salary = grouped.mean()
print(mean_salary)


