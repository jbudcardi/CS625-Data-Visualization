import pandas as pd

# Read in target csv
data = pd.read_csv("movies-cleaned-final.csv")

df = pd.DataFrame(data)

df['VOTES'] = df['VOTES'].astype(int)

# Sum 'VOTES' column grouped by 'GENRE'
result = df.groupby('GENRE')['VOTES'].sum().reset_index()
sorted_df = result.sort_values(by='VOTES')

sorted_df.to_csv('votes_by_genre.txt', sep='\t', index=False)