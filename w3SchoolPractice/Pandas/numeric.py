import pandas as pd
data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
df = pd.DataFrame(data)
transposed_df = df.T
print(transposed_df)
