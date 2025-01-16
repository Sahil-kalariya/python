import pandas as pd

# Create a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'C', 'B', 'A'],
        'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]}

df = pd.DataFrame(data)

cross_tab = pd.crosstab(df['Category'], df['Value'])

print(cross_tab)