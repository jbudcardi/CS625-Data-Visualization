import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Load the Excel file
xls = 'dataset_1.xls'
df = pd.read_excel(xls, na_values=['NaN'])

# Additional analysis
# Comparing growth of American regions

# Filter rows for American regions
comparison_regions = ['Northeast', 'Midwest', 'South', 'West']
df['State'] = df['State'].astype(str).str.strip()

selected_states = df[df['State'].isin(comparison_regions)]
selected_states = selected_states.drop(columns=['Post office abbreviation', '2-digit ANSI code', '1990 (April) Census', '1990 (April) \\2 Estimates base', '2000 (April) Census', '2000 (April) \\3 Estimates base'])

# Ensure column names (years) are strings before transposing
selected_states.columns = selected_states.columns.astype(str)

# Reshape data using melt and clean
long_df = pd.melt(selected_states, id_vars=['State'], var_name='Year', value_name='Population')
long_df['Year'] = long_df['Year'].astype(str)
long_df['Population'] = pd.to_numeric(long_df['Population'], errors='coerce') 
long_df = long_df.dropna(subset=['Population'])

plt.figure(figsize=(14,7))
sns.lineplot(data=long_df, x='Year', y='Population', hue='State', marker='o')

# Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population of American Regions, 1960-2009')

# Shorten x-tick labels to the first 4 characters
original_xticks = plt.gca().get_xticklabels()  
shortened_labels = [label.get_text()[:4] for label in original_xticks]  
plt.xticks(ticks=plt.gca().get_xticks(), labels=shortened_labels)
plt.xticks(rotation=45) 

# Grid and Legend
plt.grid(True)
plt.legend(title='Regions')

# Display the chart
plt.show()