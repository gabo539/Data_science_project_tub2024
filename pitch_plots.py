import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wwrem_p_gdp = pd.read_csv('world_economic_indicators.csv')
gini_coeff = pd.read_csv('Gini_Coefficient_code.csv')
gdp_pcppp = pd.read_csv('GDP_percapita_PPP.csv')



#Limiting to relevant data
wwrem_first_4_columns = wwrem_p_gdp.iloc[:, 0:4]

#Limitation to the intervall from 1990 to 2020
wwrem_first_4_columns_90to20 = wwrem_first_4_columns[(wwrem_first_4_columns['Year'] >= 1990) & (wwrem_first_4_columns['Year'] <= 2020)]


#Summation of all remittances of all countries on each seperate year
sum_per_year = wwrem_first_4_columns_90to20.groupby('Year')['Personal remittances, received (% of GDP)'].mean()


#Plot 1
plt.figure(figsize=(10, 6))
plt.plot(sum_per_year.index, sum_per_year.values, marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Sum of Remittances, received (% of GDP)')
plt.title('Sum of Remittances, received (% of GDP) over years')
plt.grid(True)
plt.tight_layout()
plt.show()

#Adjusting WWREM for 1995 and 2015
wwrem_first_4_columns_1995 = wwrem_first_4_columns[(wwrem_first_4_columns['Year'] == 1995)]
wwrem_first_4_columns_2015 = wwrem_first_4_columns[(wwrem_first_4_columns['Year'] == 2015)]

#Adjusting GDP per capita PPP over the needed years
gdp_pcppp_95 = gdp_pcppp[['Country Code','1995']]
gdp_pcppp_15 = gdp_pcppp[['Country Code','2015']]




#Plot 2









