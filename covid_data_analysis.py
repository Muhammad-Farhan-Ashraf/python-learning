import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""Load Data"""
df=pd.read_csv("covid-data.csv")
df["date"]=pd.to_datetime(df["date"])

"""Data Cleaning
Handle missing values
Filter countries of interest
Convert dates to datetime type"""

df=df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
df=df.fillna(0)
"""# Filter out non-country entries"""
non_countries=("World","High-income countries", "Asia", "Europe","Upper-middle-income countries","European Union (27)","South America","North America","United States","Lower-middle-income countries")
df_countries = df[~df['location'].isin(non_countries)]
top_countries=df_countries.groupby("location")['total_cases'].max().sort_values(ascending=False).head(10)
print(top_countries)

"""Visualize top countries"""

plt.figure(figsize=(12,8))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.show()