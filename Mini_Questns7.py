#                   mini-project

#   Converting columns to datetime (pd.to_datetime)
#   Setting a DateTime index & resampling



# 1️. Create a dataset of website visits (string dates + visit counts)

import pandas as pd

data = {
    "VisitDate": [
        "2026-06-01",      
        "02/06/2026",      
        "June 3, 2026",    
        "04-Jun-2026",     
        "2026/06/05",      
        "06-06-2026",     
        "Jun 07 2026",     
        "2026.06.08",      
        "9 June 2026",     
        "Invalid Date"     
    ],
    "Visits": [120, 150, 135, 180, 170, 200, 190, 210, 220, 205]
}

df = pd.DataFrame(data)
print(df)


# 2️. Convert VisitDate to datetime
df['VisitDate'] = pd.to_datetime(df['VisitDate'],format='mixed',errors='coerce')


# 3️. Set VisitDate as the index
df_idx = df.set_index('VisitDate')


# 4️. Resample to get total visitors per month
df_idx.resample('M')['Visits'].sum()


# 5️.  Resample to get average visitors per week
df_idx.resample('W')['Visits'].mean()
