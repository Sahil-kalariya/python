import pandas as pd
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        'Value': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print("\nGroup by 'Category' and 'Type':")
grouped = df.groupby(['Category', 'Type']).sum()
print(grouped)
