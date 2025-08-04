import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
url1 = 'dataset_1.xls'
df = pd.read_excel(url1, na_values=['NaN'])

#print(df.columns)
df['States'] = df['States'].astype(str)
df['States'] = df['States'].str.strip()
column_states = df['States']
column_states_new = [x for x in column_states if x!='nan' and x!='*']

column_abbrev = df['PO Abbreviation'].dropna()
column_abbrev_new = [x for x in column_abbrev if x!='nan' and x!='*']
#print(column_abbrev_new)

# Getting rid of commas in numerical values
df['Total Square Mile '] = df['Total Square Mile '].replace(',', '', regex=True)
df['Land Square Mile '] = df['Land Square Mile '].replace(',', '', regex=True)
df['Water Square Mile '] = df['Water Square Mile '].replace(',', '', regex=True)

# Convert to string to parse out NaN values
df['Total Square Mile '] = df['Total Square Mile '].astype(str)
df['Land Square Mile '] = df['Land Square Mile '].astype(str)
df['Water Square Mile '] = df['Water Square Mile '].astype(str)

# Create new lists after parsing out NaN values
column_total = df['Total Square Mile ']
column_land = df['Land Square Mile ']
column_water = df['Water Square Mile ']
column_total_new = [x for x in column_total if x!='nan']
column_land_new = [x for x in column_land if x!='nan']
column_water_new = [x for x in column_water if x!='nan']

# Create new dataframe with cleaned, relevant columns
updated_df = pd.DataFrame({'State': column_states_new, 'Abbreviation': column_abbrev_new, 'TotalArea': column_total_new, 'LandArea': column_land_new, 'WaterArea' : column_water_new})

# Convert column values to float type
updated_df['TotalArea'] = updated_df['TotalArea'].astype(float)
updated_df['LandArea'] = updated_df['LandArea'].astype(float)
updated_df['WaterArea'] = updated_df['WaterArea'].astype(float)

# Print to test
'''
print(updated_df['TotalArea'].values)
print(updated_df['LandArea'].values)
print(updated_df['WaterArea'].values)
'''

# Q1: Show the relationship between land area and water area
plt.figure(figsize=(14, 7))
plt.scatter(updated_df['LandArea'], updated_df['WaterArea'], color='blue', label='States')

# Highlight interesting outliers
outliers = updated_df[(updated_df['WaterArea'] > 20000) | (updated_df['LandArea'] > 200000)]
plt.scatter(outliers['LandArea'], outliers['WaterArea'], color='red', label='Outliers')

for i, state in outliers.iterrows():
  plt.text(state['LandArea'], state['WaterArea'], state['Abbreviation'])
  
# Annotate non-outlier blue points
non_outliers = updated_df[~updated_df.index.isin(outliers.index)]
for i, state in non_outliers.iterrows():
    plt.text(state['LandArea'], state['WaterArea'], state['Abbreviation'], fontsize=8, alpha=0.7)

# Label and show plot
plt.xlabel('Land Area (sq miles)')
plt.ylabel('Water Area (sq miles)')
plt.title('Relationship between Land Area and Water Area for US States')
plt.legend()
plt.grid(True)
plt.show()

# Q2: Compare the proportion of total area that is land and water for 10 states
# Choosing 10 states with the largest total area
selected_states = updated_df.nlargest(10, 'TotalArea')
selected_states['LandProportion'] = selected_states['LandArea'] / selected_states['TotalArea']
selected_states['WaterProportion'] = selected_states['WaterArea'] / selected_states['TotalArea']

# Plotting the comparison
selected_states.plot(x='State', y=['LandProportion', 'WaterProportion'], kind='bar', figsize=(14, 7), color=['green', 'blue'])
plt.xlabel('State')
plt.ylabel('Proportion of Total Area')
plt.title('Proportion of Land and Water Area for Selected States')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.show()

# Print the selected states and their proportions
print(selected_states[['State', 'LandProportion', 'WaterProportion']])