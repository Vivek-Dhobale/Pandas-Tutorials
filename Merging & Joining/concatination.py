"""
concat Syntax .,
pd.concat([df1, df2], axis=0, ignore_index=True)
- [df1 and df2]: The DataFrames to be concatenated.as a list.
- ignore_index: If True, the resulting DataFrame will have a new integer index.
- if False, the original indices will be retained. Default is False.   
- axis: The axis along which to concatenate. 0 for rows (default) and 1 for columns.


"""
import pandas as pd

df1 = pd.DataFrame({
    'Name': ["ram", "shyam", "hari", "gopal"],
    'Age': [25, 30, 35, 40],
    'City': ["mumbai", "delhi", "kolkata", "chennai"]
})

df2 = pd.DataFrame({
    'Name': ["ram", "shyam", "hari", "gopal"],
    'Salary': [50000, 60000, 70000, 80000], 
    'Department': ['HR', 'IT', 'Finance', 'Marketing']
})


# Concatenating along rows (default)
print("\nConcatenating along rows:")    
concat_rows = pd.concat([df1, df2], axis=0, ignore_index=True)
print(concat_rows)

# Concatenating along columns
print("\nConcatenating along columns:") 
concat_columns = pd.concat([df1, df2], axis=1, ignore_index=False)
print(concat_columns)