#                                   Mini Practice


#1. Build a DataFrame with columns: Name, Age, Score, Height.
#2. Sort the data by Score (descending).
#3. Get mean, median, mode, and std of numeric columns.
#4. Use value_counts on Name or any categorical column.
#5. Compute corr() and cov() for all numeric columns.


# 1. Build a DataFrame with columns: Name, Age, Score, Height

import pandas as pd
data = {
    "Name" : ['Aditi','Aadi','Rishi','Aarya'],
    "Age" : [18,20,25,21],
    "Score" : [95,85,84,97],
    "Height" : [5.6,6.0,6.2,5.2]
}
df = pd.DataFrame(data)
print(df)

# 2. Sort the data by Score (descending)

print(df.sort_values(by='Score', ascending=False))

# 3. Get mean, median, mode, and std of numeric columns

print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))
print(df.mode(numeric_only=True))
print(df.std(numeric_only=True))

# 4. Use value_counts on Name or any categorical column

print(df['Name'].value_counts())

# 5. Compute corr() and cov() for all numeric columns

print(df.corr(numeric_only=True))
print(df.cov(numeric_only=True))