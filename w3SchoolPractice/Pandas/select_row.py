import pandas as pd

df = pd.DataFrame({
    'A': [1, 6, 8, 3, 7],
    'B': [5, 2, 9, 4, 1]
})

result = df[df['A'] > 4]
print(result)
