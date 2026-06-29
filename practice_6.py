#                                        Mini practice

#1. Create three DataFrames: Products, Sales, and Revenue.
#2. Concatenate them vertically and horizontally.
#3. Merge Sales and Revenue using different join types.
#4. Join Products with Sales based on index or a key.
#5. Analyze missing values after joins.




# 1. Create three DataFrames: Products, Sales, and Revenue

import pandas as pd

# products
df1 = pd.DataFrame({
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"]
})

# sales
df2 = pd.DataFrame({
    "Product_ID": [101, 102, 103, 106],
    "Units_Sold": [20, 50, 35, 15],
    "Salesperson": ["Aman", "Riya", "Karan", "Neha"]
})

# revenue
df3 = pd.DataFrame({
    "Product_ID": [101, 103, 104, 107],
    "Revenue": [1200000, 175000, 600000, 90000],
    "Region": ["North", "South", "West", "East"]
})


# 2. Concatenate them vertically and horizontally
pd.concat([df1,df2,df3],ignore_index=True)
pd.concat([df1,df2,df3],axis=1)


# 3. Merge Sales and Revenue using different join types (inner, left, right, outer)
pd.merge(df2,df3,how="inner")
pd.merge(df2,df3,how="left")
pd.merge(df2,df3,how="right")
pd.merge(df2,df3,how="outer")


# 4. Join Products with Sales based on index or a key
p_index = df1.set_index("Product_ID")
s_index = df2.set_index("Product_ID")
joined = p_index.join(s_index)
joined


# 5. Analyze missing values after joins
# Use isna(), info(), or describe() to explore gaps
joined.isna().sum()
joined.info()
joined.describe()