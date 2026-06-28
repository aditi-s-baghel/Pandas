#                                      Mini Practice
#1. Create a DataFrame with columns: Department, Employee, Salary, Age, City.
#2. Group by Department to get average Salary and max Age.
#3. Apply multiple aggregations using agg().
#4.  Create a pivot_table to see mean Salary by Department and City.
#5. Build a crosstab for Department vs City.




# 1. Create a DataFrame with columns: Department, Employee, Salary, Age, City

import pandas as pd
data = {
    "Employee": ["John", "Sarah", "Mike", "Anna", "Tom", "Laura", "Steve", "Kate"],
    "Department": ["HR", "IT", "IT", "Finance", "Finance", "HR", "IT", "Finance"],
    "Salary": [50000, 70000, 72000, 65000, 60000, 52000, 75000, 58000],
    "Age": [28, 32, 30, 27, 35, 29, 31, 26],
    "City" : ["Delhi","Mumbai","Indore","Bhopal","Pune","Raipur","Satna","Rewa"]
}
df = pd.DataFrame(data)
print(df)


# 2. Group by Department to get average Salary and max Age
df.groupby('Department').agg({'Salary':'mean','Age':'max'})


# 3. Apply multiple aggregations using agg()
# Example: mean Salary, max Age per Department
df.groupby('Department').agg({'Salary':['mean'],'Age':['max']})


# 4. Create a pivot_table to see mean Salary by Department and City
df.pivot_table(index='Department', columns='City', values=['Salary'], aggfunc='mean')


# 5. Build a crosstab for Department vs City
pd.crosstab(df['Department'],df['City'])