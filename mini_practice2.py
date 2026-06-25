#1. Create a messy DataFrame with missing values, wrong data types, typos, extra columns, and duplicates.
#2. Clean it step-by-step using what you learned:
#       -  Handle missing values
#       -  Change data types
#       -  Replace incorrect values
#       -  Drop unnecessary rows/columns
#       -  Remove duplicates




import pandas as pd
import numpy as np

# 1. Create a messy DataFrame
data = {
    "Name": ["Alice", "Bob", "Chrlie", "David", "Alice", None],
    "Age": ["25", "30", None, "40", "25", "30"],                           # ages stored as strings, with missing value
    "City": ["Delhi", "Mumbai", "Pun", "Bangalore", "Delhi", "Mumbai"],    # typo: "Pun" -> "Pune"
    "Score": [85, None, 78, 88, 85, 91],                                   # missing value in Score
    "Extra": ["x", "y", "z", "x", "y", "z"]                                # extra column we don't really need
}

df = pd.DataFrame(data)

#print("Original messy DataFrame:")
#print(df)


# 2. Handle missing values Fill or drop as needed

df['Name'] = df['Name'].fillna('Unknown',inplace=True)
df['Age'] = df['Age'].fillna(0,inplace=True)
df['Score'] = df['Score'].fillna(df['Score'].mean(),inplace=True)
                                 

# 3. Change data types Convert Age to float, Score to int, etc.

df["Age"] = df["Age"].astype(int)
df["Score"] = df["Score"].astype(float)


# 4. Replace incorrect values
# Fix 'Pun' -> 'Pune', maybe unify Name spellings if needed

df['City'].replace('Pun','Pune',inplace=True)


# 5. Drop unnecessary rows/columns
# Remove 'Extra' or any row you don't want

df.drop('Extra',axis=1, inplace=True)
df.drop(index=2,axis=0,inplace=True)


# 6. Remove duplicates
# Use duplicated() and drop_duplicates()

print(df.duplicated())
print(df.drop_duplicates(inplace=True))


# 7. Final clean DataFrame
# Print the cleaned DataFrame and check info()

print(df)
df.info()