#1.  Build a DataFrame with columns such as Name, Age, City, Score.
#2.  Use boolean indexing to select rows where Age > 25.
#3.  Filter rows where City is either 'Delhi' or 'Mumbai'.
#4.  Use query() to find rows with Score >= 85 and Age < 35.
#5.  Clean a text column using str.replace or str.lower.



import pandas as pd

# 1. Build a DataFrame with columns: Name, Age, City, Score

data = {
    'Name' : ['Aditi','Aadi','Adarsh','Ansh','Rishi'],
    'Age' : [18,22,25,26,28],
    'City' :  ['Delhi','Bhopal','Indore','Pune','Mumbai'],
    'Score' : [90,85,65,45,70]
}

df = pd.DataFrame(data)
print(df)

# 2. Use boolean indexing to select rows where Age > 25
print(df['Age'] > 25)                        # gives True/False
print(df[df['Age'] > 25])                    # gives rows


# 3. Filter rows where City is either 'Delhi' or 'Mumbai'
print(df[(df['City'] == 'Delhi') | (df['City'] == 'Mumbai')])


# 4. Use query() to find rows with Score >= 85 and Age < 35
print(df.query("Score >= 85 and Age < 35"))


# 5. Clean a text column using str.replace or str.lower
# Example: convert City names to lowercase or replace "delhi" with "New Delhi"
print(df['City'].str.replace('Delhi','New Delhi'))
print(df['City'].str.lower())