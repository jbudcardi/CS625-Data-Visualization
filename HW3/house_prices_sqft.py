import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data into a DataFrame
df = pd.read_csv("house price.csv")

# Create the scatterplot
plt.figure(figsize=(12, 7))
plt.scatter(df['price'], df['sqft_living'], alpha=0.45, color='green')

# Scatterplot Labels
plt.title('Price by Living Square Footage in Washington State')
plt.xlabel('House Price')
plt.ylabel('Square Footage')

# Rotate xlabels for better readability
plt.xticks(rotation=45)

# Bound x and y values to exclude deadspace/extreme outliers
plt.xlim(100000, 1000000)
plt.ylim(0, 8000)

# Prevent scientific notation
plt.ticklabel_format(style='plain')

# Enforce grid, not necessary but optional for looks
# plt.grid(True)

# Tight layour for padding
plt.tight_layout()

# Display plot
plt.show()
