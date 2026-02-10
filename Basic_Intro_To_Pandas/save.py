import pandas as pd

data = {
    "Name" : ["Ram", "Sham", "Dhansham"], 
    "Age" : [10,20,30],
    "City" : ["Nagpur", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

print(df)

df.to_csv("output.csv", index=False)  # index = false used to avoid index in the seved file 
df.to_excel("output.xlsx", index=False)  
df.to_json("output.json", index=False)   
df.to_html("output.html", index=False)   


