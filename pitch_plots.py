import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Load the data
wwrem_p_gdp = pd.read_csv('world_economic_indicators.csv')
gini_coeff = pd.read_csv('Gini_Coefficient_code.csv')
gdp_pcppp = pd.read_csv('GDP_percapita_PPP.csv')

# Limiting to relevant data
wwrem_first_4_columns = wwrem_p_gdp.iloc[:, 0:4]

# Limitation to the interval from 1990 to 2020
wwrem_first_4_columns_90to20 = wwrem_first_4_columns[(wwrem_first_4_columns['Year'] >= 1990) & (wwrem_first_4_columns['Year'] <= 2020)]

# Summation of all remittances of all countries on each separate year
sum_per_year = wwrem_first_4_columns_90to20.groupby('Year')['Personal remittances, received (% of GDP)'].mean()

# Plot 1
plt.figure(figsize=(10, 6))
plt.plot(sum_per_year.index, sum_per_year.values, marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Sum of Remittances, received (% of GDP)')
plt.title('Sum of Remittances, received (% of GDP) over years')
plt.grid(True)
plt.tight_layout()
plt.show()

# Adjusting WWREM for 1995 and 2015
wwrem_first_4_columns_1995 = wwrem_first_4_columns[(wwrem_first_4_columns['Year'] == 1995)]
wwrem_first_4_columns_2015 = wwrem_first_4_columns[(wwrem_first_4_columns['Year'] == 2015)]

# Adjusting GDP per capita PPP over the needed years
gdp_pcppp_95 = gdp_pcppp[['Country Code', '1995']]
gdp_pcppp_15 = gdp_pcppp[['Country Code', '2015']]

# Merging without gini
first_merge_95 = pd.merge(wwrem_first_4_columns_1995, gdp_pcppp_95, on='Country Code')
first_merge_15 = pd.merge(wwrem_first_4_columns_2015, gdp_pcppp_15, on='Country Code')

# Merging with gini
final_merge_95 = pd.merge(first_merge_95, gini_coeff, on='Country Code')
final_merge_15 = pd.merge(first_merge_15, gini_coeff, on='Country Code')

# Tidying our df's
columns_to_keep1 = ['Country Code', 'Personal remittances, received (% of GDP)', 'giniCIA', '1995']
columns_to_keep2 = ['Country Code', 'Personal remittances, received (% of GDP)', 'giniCIA', '2015']
final_merge_95_almost_tidy = final_merge_95[columns_to_keep1]
final_merge_15_almost_tidy = final_merge_15[columns_to_keep2]

# Rename the confusingly named columns
final_merge_95_tidy = final_merge_95_almost_tidy[['Country Code', 'Personal remittances, received (% of GDP)', 'giniCIA', '1995']].copy()
final_merge_15_tidy = final_merge_15_almost_tidy[['Country Code', 'Personal remittances, received (% of GDP)', 'giniCIA', '2015']].copy()
final_merge_95_tidy.rename(columns={'1995': 'GDP per capita (PPP)'}, inplace=True)
final_merge_15_tidy.rename(columns={'2015': 'GDP per capita (PPP)'}, inplace=True)

# PLOT 2
# Convert 'giniCIA' column to numeric if it's not already
final_merge_95_tidy['giniCIA'] = pd.to_numeric(final_merge_95_tidy['giniCIA'], errors='coerce')

# Plotting
plt.figure(figsize=(12, 8))

# Scatter plot with color mapping based on Gini coefficient
sc = plt.scatter(final_merge_95_tidy['Personal remittances, received (% of GDP)'],
                 final_merge_95_tidy['GDP per capita (PPP)'],
                 c=final_merge_95_tidy['giniCIA'],
                 cmap='inferno',  # Choose a sequential colormap
                 alpha=0.8  # Adjust transparency
                 )

# Adding color bar
cbar = plt.colorbar(sc)
cbar.set_label('Gini Coefficient')

# Adding labels and title
plt.title('GDP per Capita (PPP) vs Personal Remittances in 1995 for all countries worldwide')
plt.xlabel('Personal Remittances (% of GDP)')
plt.ylabel('GDP per Capita (PPP) in nominal US$')

# Setting axis limits
plt.ylim(0, 150000)
plt.xlim(0, 150)

# Adding grid
plt.grid(True)

# Show plot
plt.show()

# PLOT 2.1
# Convert 'giniCIA' column to numeric if it's not already
final_merge_15_tidy['giniCIA'] = pd.to_numeric(final_merge_15_tidy['giniCIA'], errors='coerce')

# Plotting
plt.figure(figsize=(12, 8))

# Scatter plot with color mapping based on Gini coefficient
sc = plt.scatter(final_merge_15_tidy['Personal remittances, received (% of GDP)'],
                 final_merge_15_tidy['GDP per capita (PPP)'],
                 c=final_merge_15_tidy['giniCIA'],
                 cmap='inferno',  # Choose a sequential colormap
                 alpha=0.8  # Adjust transparency
                 )

# Adding color bar
cbar = plt.colorbar(sc)
cbar.set_label('Gini Coefficient')

# Adding labels and title
plt.title('GDP per Capita (PPP) vs Personal Remittances in 2015 for all countries worldwide')
plt.xlabel('Personal Remittances (% of GDP)')
plt.ylabel('GDP per Capita (PPP) in nominal US$')

# Setting axis limits
plt.ylim(0, 150000)
plt.xlim(0, 150)

# Adding grid
plt.grid(True)

# Show plot
plt.show()

# PLOT 2.2
# Convert 'giniCIA' column to numeric if it's not already
final_merge_95_tidy['giniCIA'] = pd.to_numeric(final_merge_95_tidy['giniCIA'], errors='coerce')

# Plotting
plt.figure(figsize=(12, 8))

# Scatter plot with color mapping based on Gini coefficient
sc = plt.scatter(final_merge_95_tidy['Personal remittances, received (% of GDP)'],
                 final_merge_95_tidy['GDP per capita (PPP)'],
                 c=final_merge_95_tidy['giniCIA'],
                 cmap='inferno',
                 alpha=0.8)

# Adding color bar
cbar = plt.colorbar(sc)
cbar.set_label('Gini Coefficient')

# Adding labels and title
plt.title('GDP per Capita (PPP) vs Personal Remittances in 1995 for all countries worldwide')
plt.xlabel('Personal Remittances (% of GDP)')
plt.ylabel('GDP per Capita (PPP) in nominal US$')

# Setting axis limits
plt.ylim(0, 50000)
plt.xlim(0, 35)

# Adding grid
plt.grid(True)

# Create an inset of the zoomed-in region
ax_inset = inset_axes(plt.gca(), width="40%", height="30%", loc='upper right', borderpad=2)

# Plotting the inset
ax_inset.scatter(final_merge_95_tidy['Personal remittances, received (% of GDP)'],
                 final_merge_95_tidy['GDP per capita (PPP)'],
                 c=final_merge_95_tidy['giniCIA'],
                 cmap='inferno',
                 alpha=0.8)

# Set limits for the inset
ax_inset.set_xlim(0, 8)
ax_inset.set_ylim(0, 12000)
ax_inset.set_xticks([0, 2, 4, 6, 8])
ax_inset.set_yticks([0, 4000, 8000, 12000])
ax_inset.grid(True)

# Show plot
plt.show()

# PLOT 2.3
# Convert 'giniCIA' column to numeric if it's not already
final_merge_15_tidy['giniCIA'] = pd.to_numeric(final_merge_15_tidy['giniCIA'], errors='coerce')

# Plotting
plt.figure(figsize=(12, 8))

# Scatter plot with color mapping based on Gini coefficient
sc = plt.scatter(final_merge_15_tidy['Personal remittances, received (% of GDP)'],
                 final_merge_15_tidy['GDP per capita (PPP)'],
                 c=final_merge_15_tidy['giniCIA'],
                 cmap='inferno',
                 alpha=0.8)

# Adding color bar
cbar = plt.colorbar(sc)
cbar.set_label('Gini Coefficient')

# Adding labels and title
plt.title('GDP per Capita (PPP) vs Personal Remittances in 2015 for all countries worldwide')
plt.xlabel('Personal Remittances (% of GDP)')
plt.ylabel('GDP per Capita (PPP) in nominal US$')

# Setting axis limits
plt.ylim(0, 50000)
plt.xlim(0, 35)

# Adding grid
plt.grid(True)

# Show plot
plt.show()
