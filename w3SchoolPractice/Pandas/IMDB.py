import pandas as pd
df = pd.read_csv('movies_metadata.csv' , 'utf-8')
n = 500
small_df = df[['title', 'vote_count']]
result = small_df[small_df['vote_count'] >= n]
print("List of movies longer than 30 minutes and shorter than 360 minutes:")
print(result)