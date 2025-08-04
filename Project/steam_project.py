import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv('steam.csv')
df.columns = df.columns.str.strip()

# Pre-Processing
df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
df = df.dropna(subset=['release_year'])
df['release_year'] = df['release_year'].astype(int)

# Stacked Bar Chart
# Split genres into multiple rows
df['genres_split'] = df['genres'].str.split(';')
df['genre_count'] = df['genres_split'].apply(len)
df_exploded = df.explode('genres_split')
df_exploded['genres_split'] = df_exploded['genres_split'].str.strip()

# Genres to exclude
excluded_genres = {'Violent', 'Gore', 'Nudity', 'Sexual Content', 'Documentary', 'Accounting',
                   'Animation & Modeling', 'Video Production', 'Utilities', 'Web Publishing',
                   'Game Development', 'Design & Illustration', 'Photo Editing', 'Audio Production',
                   'Software Training', 'Tutorial', 'Education'}

# Filter unwanted genres
df_filtered = df_exploded[~df_exploded['genres_split'].isin(excluded_genres)].copy()

# Recalculate fraction to ensure proper weighting after exclusion
df_filtered['fraction'] = 1 / df_filtered.groupby(df_filtered.index)['genre_count'].transform('sum')

# Compute fractional counts
genre_fractional_counts = (
    df_filtered.groupby(['release_year', 'genres_split'])['fraction'].sum().reset_index(name='count')
)

# Normalize data to get proportions (i.e. each year sums to 1.0 i.e. 100%)
pivot_frac = genre_fractional_counts.pivot(index='release_year', columns='genres_split', values='count').fillna(0)
pivot_frac_normalized = pivot_frac.div(pivot_frac.sum(axis=1), axis=0)  # Normalize rows to sum to 1 (proportions)

 
# Convert pivot table to long format for Plotly
pivot_frac_long = pivot_frac_normalized.reset_index().melt(id_vars='release_year',
                                                           var_name='genre', value_name='proportion')

# Plot the normalized stacked bar chart using Plotly
fig_bar = px.bar(pivot_frac_long, x='release_year', y='proportion', color='genre',
                 title="Indies Took the Lead in Steam Game Genres by end of the 2010's",
                 color_discrete_sequence=['salmon', 'skyblue', 'mediumseagreen', 'gold', 
                         'mediumorchid', 'darkorange', 'lightcoral', 'steelblue', 
                         'plum', 'turquoise', 'burlywood', 'silver', 'dimgray'],
                 labels={'release_year': 'Year', 'proportion': 'Proportion of Titles'},
                 barmode='stack')

# Show all x-axis ticks, center title
fig_bar.update_layout(
    xaxis=dict(tickmode='linear'),
    title=dict(
        x=0.5,
        xanchor='center'
    )
)

fig_bar.show()

# Scatterplot
fig_scatter = px.scatter(df, x='achievements', y='median_playtime',
                         title='Litle to No Correlation Between Median Playtime and Number of Achievements for Steam Games',
                         labels={'achievements': 'Number of Achievements',
                                 'median_playtime': 'Median Playtime (minutes)'},
                         opacity=0.7)

# Set x and y limits, center title
fig_scatter.update_layout(xaxis=dict(range=[0, 800]),
                          yaxis=dict(range=[0, 10000]),
                          title=dict(
                            x=0.5,
                            xanchor='center'
                          )
    )

fig_scatter.show()