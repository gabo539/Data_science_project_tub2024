import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wwrem_p_gdp = pd.read_csv('world_economic_indicators.csv')

#pro jahr summierter anteil am gdp
first_4_columns =wwrem_p_gdp.iloc[:, 0:4]
#print(first_4_columns)

selected_rows = first_4_columns[(first_4_columns['Year'] >= 1990) & (first_4_columns['Year'] <= 2020)]
#print(selected_rows)

sum_per_year = selected_rows.groupby('Year')['Personal remittances, received (% of GDP)'].sum()
#print(sum_per_year)

plt.figure(figsize=(10, 6))
plt.plot(sum_per_year.index, sum_per_year.values, marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Sum of Remittances')
plt.title('Sum of Remittances Over Years')
plt.grid(True)
plt.tight_layout()
plt.show()


