"""
using intepolate() method we can fill the null values by the estimate values in the dataset. 

Benifits of interpolation
1 -> preserve data integrity
2 -> Smooth trends
3 -> Avoid data loss 

interpolation methods 
1 -> Linear, 2 -> polynomial, 3 -> time, 4 -> cubic, 5 -> qudratic, 6 -> nearest,
7 -> spline, 8 -> index,9 -> values, 10 -> pad, 11 -> backfill, 12 -> bfill

it does not change the original data but it creates a new column with the filled values.

it does change the first and last null values because it does not have any values to estimate the null values.

"""
import pandas as pd 

data = {
    "Time":[1,2,None,4,5,None,7,8], 
    "Values":[28,None,22,30,None,40,None,32]
    
}

df = pd.DataFrame(data)
print("Original Dataframe...")
print(df)

# method 0ne to fill null values by interpolation method
# df["Values"] = df["Values"].interpolate(method = "linear")

# another metohd to fill null values by interpolation method
df.interpolate(method="linear", axis=0, inplace=True)

print("After filling null values by interpolation method...")
print(df)

