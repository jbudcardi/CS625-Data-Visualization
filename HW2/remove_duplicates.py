import pandas as pd

# Read in target csv
data = pd.read_csv("movies_working.csv")

# Drop duplicate movie title rows
data = data.drop_duplicates(subset="MOVIES")

# Save new csv
data.to_csv("movies_edited.csv", index=False)