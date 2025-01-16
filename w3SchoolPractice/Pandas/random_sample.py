import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("Original Dataframe:")
print(diamonds.head())
print("\nSample 5 rows from the DataFrame without replacement:")
print(diamonds.sample(n=3))
