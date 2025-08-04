#TV Shows
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("TV_Shows.csv")

 
# Count the number of TV shows for each provider
provider_counts = df['Netflix'].value_counts().get(1, 0), df['Hulu'].value_counts().get(1, 0), df['Prime Video'].value_counts().get(1, 0), df['Disney+'].value_counts().get(1, 0)
providers = ['Netflix', 'Hulu', 'Prime Video', 'Disney+']

 
# Create a bar chart to visualize the comparison
plt.figure(figsize=(10, 6))
plt.bar(providers, provider_counts, width=0.5, color=['red', 'green', 'blue', 'purple'])
plt.xlabel('Providers')
plt.ylabel('Number of TV Shows')
plt.title('Number of TV Shows by Platform')
plt.show()