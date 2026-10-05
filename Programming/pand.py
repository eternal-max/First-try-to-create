import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [50000, 60000, 55000], 
    'Job': ['Junior', 'Senior', 'Middle']
}

df = pd.DataFrame(data)
print(df.shape)
print(df) 