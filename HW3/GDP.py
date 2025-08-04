import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("GDP.csv")

# Select the countries of interest
countries_of_interest = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
filtered_df = df[df['country'].isin(countries_of_interest)]

# Conver years to integer and exlude all years before 1990
filtered_df['year'] = filtered_df['year'].astype(int)
filtered_df = filtered_df[filtered_df['year'] >= 1990]

# Create the multiple line chart using Seaborn
plt.figure(figsize=(12, 7))
sns.lineplot(data=filtered_df, x='year', y='gdp', hue='country')

# Plot labels and legend
plt.title('BRICS GDP from 1990 to 2020')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.legend(title='BRICS Countries')

# Bounding GDP amount limits
plt.ylim(20000000, 15000000000000)
plt.xticks(rotation=45)

# Enforce grid and tight layout
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()