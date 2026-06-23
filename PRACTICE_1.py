#                                         MINI PRACTICE 1



#1. Create a DataFrame with at least 5 rows and 4 columns (mix of numeric + text).
#2. Show the first 3 rows, last 2 rows, and the info.
#3. Select a sub-DataFrame with only 2 columns.
#4. Rename one column and set any column as index, then reset it back.
#5. Print df.shape, df.dtypes, and df.columns.




import pandas as pd

# Create a DataFrame with at least 5 rows & 4 columns (mix of numbers + text)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 40, 22],
    "City": ["Delhi", "Mumbai", "Pune", "Bangalore", "Chennai"],
    "Score": [85, 91, 78, 88, 95]
}

d = pd.DataFrame(data)


# Show the first 3 rows, last 2 rows, and info

d.head(3)
d.tail(2)
d.info()


# Select a sub-DataFrame with only 2 columns
print(d[['Age','City']])


# Rename one column and set any column as index, then reset it back
d.rename(columns={'Score':'Marks'}, inplace = True)
print (d)

d.set_index('Name', inplace = True)
print(d)

d.reset_index(inplace = True)
print(d)


# Print df.shape, df.dtypes, and df.columns

print(d.shape)
print(d.dtypes)
print(d.columns)

