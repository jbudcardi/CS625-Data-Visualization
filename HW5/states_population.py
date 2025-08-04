import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Load the Excel file
xls = 'dataset_1.xls'
df = pd.read_excel(xls, na_values=['NaN'])

# print(df.columns)

# Drop regional entries from State column
regions = df[((df.State == 'Northeast') | (df.State == 'Midwest') | (df.State == 'South') | (df.State == 'West '))].index
df.drop(regions, inplace=True)

df = df.replace(',', '', regex=True)

# Task 1: Create boxplots for 1970, 1985, 1995, and 2009
df.boxplot(column=['1970 (April)', '1985 (July)', '1995 (July)', '2009 (July)'])

# Display plot
plt.title('Boxplot of Population for 1970, 1985, 1995, and 2009')
plt.ylabel('Population')
plt.show()

# Task 2: Create histogram for state populations in the year 2002
# Assign 2002 column to list
pop_values = df['2002 (July)']

# Define bin numbers
bin_num = 20

# Create bin ranges
bins = np.linspace(400, 35000, bin_num + 1)

# Create histogram
plt.hist(pop_values, bins=bins, edgecolor='black')
plt.xlabel('Population')
plt.ylabel('Number of States')
plt.title('2002 Population Histogram')
plt.show()

# Task 3: Population distributions in 1992 and 2009
# Create lists from year columns
year_1992 = df['1992 (July)']
year_2009 = df['2009 (July)']

# Create np arrays
year_1 = np.array(year_1992)
year_2 = np.array(year_2009)

# Sort the data
sorted_year_1 = np.sort(year_1)
sorted_year_2 = np.sort(year_2)

# Compute eCDF values
cdf_year_1 = np.arange(1, len(sorted_year_1) + 1) / len(sorted_year_1)
cdf_year_2 = np.arange(1, len(sorted_year_2) + 1) / len(sorted_year_2)

# Plot the eCDFs
plt.plot(sorted_year_1, cdf_year_1, marker='o', label='1992', linestyle='-', alpha=0.4)
plt.plot(sorted_year_2, cdf_year_2, marker='o', label='2009', linestyle='-', alpha=0.4)
plt.xlabel('Population')
plt.ylabel('Cumulative Probability')
plt.title('eCDF Comparison of Population Between 1992 & 2009')
plt.legend()
plt.grid(True)
plt.show()