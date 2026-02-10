"""
merging and joining are two powerful techniques in pandas for combining DataFrames based on common columns or indices.

Merging Syntax.,
pd.merge(df1, df2, how='type of join', on='column_name')
- df1 and df2: The DataFrames to be merged.
- how: The type of merge to be performed. It can be 'inner', 'outer', 'left', or 'right'.
- on: The column name(s) to join on. This should be a common column in both DataFrames. 

Types of Merges:
1. Inner Join: Returns only the rows that have matching values in both DataFrames.
2. Outer Join: Returns all rows from both DataFrames, filling in NaN for missing matches.
3. Left Join: Returns all rows from the left DataFrame and the matched rows from the    right DataFrame. If there is no match, the result will contain NaN for the right DataFrame's columns.
4. Right Join: Returns all rows from the right DataFrame and the matched rows from the left DataFrame. If there is no match, the result will contain NaN for the left DataFrame's columns.


"""

import pandas as pd

df1 = pd.DataFrame({
    'Name': ['ram', 'shyam', 'hari', 'gopal'],
    'Age': [25, 30, 35, 40],
    'City': ['mumbai', 'delhi', 'kolkata', 'chennai']   
})

df2 = pd.DataFrame({
    'Name': ['ram', 'shyam', 'hari', 'gopal'],
    'Salary': [50000, 60000, 70000, 80000],
    'Department': ['HR', 'IT', 'Finance', 'Marketing']   
})

# Merging on the 'Name' column inner join
print("\nInner Join:")
merged_df = pd.merge(df1, df2, on='Name', how='inner')
print(merged_df)

# outer join
print("\nOuter Join:")
outer_merged_df = pd.merge(df1, df2, on='Name', how='outer')
print(outer_merged_df)

# Left join
print("\nLeft Join:")
left_merged_df = pd.merge(df1, df2, on='Name', how='left')
print(left_merged_df)   

# Right join
print("\nRight Join:")
right_merged_df = pd.merge(df1, df2, on='Name', how='right')
print(right_merged_df)  


