import pandas as pd

# Read in target csv
data = pd.read_csv("movies_edited.csv")

df = pd.DataFrame(data)

# Function to determine Verdict
def determine_verdict(rating):
    if rating == 0:
        return "Not known"
    elif rating > 0 and rating <= 4.5:
        return "Flop"
    elif rating > 4.5 and rating <= 6.5:
        return "Average"
    elif rating > 6.5 and rating <= 8.0:
        return "Hit"
    elif rating > 8:
        return "Super Hit"

# Apply function to Verdict column
df['Verdict'] = df['RATING'].apply(determine_verdict)

# Save new csv
df.to_csv("movies-cleaned-final.csv", index=False)