import pandas as pd
import os
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import numpy as np
data=pd.read_csv('cleaned_removed_num_2014_to_2023_us.csv',low_memory=False)

# 1. Total Releases by Year
plt.figure(figsize=(10, 6))
sns.barplot(x='YEAR', y='TOTAL RELEASES', data=data)
plt.title('Total Releases by Year')
plt.show()

# 2. Total Releases by Industry (using 'INDUSTRY SECTOR')
plt.figure(figsize=(12, 6))
sns.barplot(x='INDUSTRY SECTOR', y='TOTAL RELEASES', data=data)
plt.title('Total Releases by Industry Sector')
plt.xticks(rotation=90)
plt.show()

# 3. Total Releases by Chemical
plt.figure(figsize=(12, 6))
sns.barplot(x='CHEMICAL', y='TOTAL RELEASES', data=data)
plt.title('Total Releases by Chemical')
plt.xticks(rotation=90)
plt.show()


# 4. Distribution of Total Releases
plt.figure(figsize=(8, 6))
sns.histplot(data['TOTAL RELEASES'], bins=20)
plt.title('Distribution of Total Releases')
plt.show()

# 5. Boxplot of Total Releases by Industry Sector
plt.figure(figsize=(12, 6))
sns.boxplot(x='INDUSTRY SECTOR', y='TOTAL RELEASES', data=data)
plt.title('Total Releases by Industry Sector (Boxplot)')
plt.xticks(rotation=90)
plt.show()


# 6. Scatter plot of Total Releases vs. On-site Releases
plt.figure(figsize=(8, 6))
sns.scatterplot(x='ON-SITE RELEASE TOTAL', y='TOTAL RELEASES', data=data)
plt.title('Total Releases vs. On-site Releases')
plt.show()

# 7. Heatmap of Correlation between release categories
plt.figure(figsize=(12, 10))
correlation_matrix = data[[
    'FUGITIVE AIR', 'STACK AIR', 'WATER', 'UNDERGROUND', 'LANDFILLS',
    'LAND TREATMENT', 'SURFACE IMPNDMNT', 'OTHER DISPOSAL'
]].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation between Release Categories')
plt.show()



# 8. Barplot of releases by State
plt.figure(figsize=(12, 6))
sns.countplot(x='ST', data=data)
plt.title('Number of Facilities by State')
plt.xticks(rotation=90)
plt.show()

# 9. Releases by State (Total Releases)
state_releases = data.groupby('ST')['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='ST', y='TOTAL RELEASES', data=state_releases)
plt.title('Total Releases by State')
plt.xticks(rotation=90)
plt.show()

# 10. Total Releases by Year
plt.figure(figsize=(10, 6))
sns.lineplot(x='YEAR', y='TOTAL RELEASES', data=data)
plt.title('Total Releases Over Time')
plt.show()

# 11. Stacked barplot of releases by different release categories
release_categories = ['FUGITIVE AIR', 'STACK AIR', 'WATER', 'UNDERGROUND', 'LANDFILLS']
release_data = data[release_categories].sum()
plt.figure(figsize=(10, 6))
release_data.plot(kind='bar', stacked=True)
plt.title('Total Releases by Release Category')
plt.show()


# 12. Boxplot of releases by different release categories
plt.figure(figsize=(10, 6))
sns.boxplot(data=data[release_categories])
plt.title('Distribution of Releases by Release Category')
plt.show()


# 13.  Releases by Industry and Year
industry_year_releases = data.groupby(['INDUSTRY SECTOR', 'YEAR'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='YEAR', y='TOTAL RELEASES', hue='INDUSTRY SECTOR', data=industry_year_releases)
plt.title('Total Releases by Industry Over Time')
plt.show()

# 14.  Releases by State and Year
state_year_releases = data.groupby(['ST', 'YEAR'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='YEAR', y='TOTAL RELEASES', hue='ST', data=state_year_releases)
plt.title('Total Releases by State Over Time')
plt.show()


# 15.  Releases by Chemical and Industry
chemical_industry_releases = data.groupby(['CHEMICAL', 'INDUSTRY SECTOR'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='CHEMICAL', y='TOTAL RELEASES', hue='INDUSTRY SECTOR', data=chemical_industry_releases)
plt.title('Total Releases by Chemical and Industry')
plt.xticks(rotation=90)
plt.show()

#16. Federal vs. Non-Federal Facilities
federal_vs_non_federal = data['FEDERAL FACILITY'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(federal_vs_non_federal, labels=federal_vs_non_federal.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart for Federal vs. Non-Federal Facilities')
plt.axis('equal')
plt.show()

#17.On-Site vs. Off-Site Release 
onsite_releases = data['ON-SITE RELEASE TOTAL'].sum()
offsite_releases = data['OFF-SITE RELEASE TOTAL'].sum()

labels = ['On-Site Releases', 'Off-Site Releases']
sizes = [onsite_releases, offsite_releases]
explode = (0.1, 0)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart for On-Site vs. Off-Site Release')
plt.axis('equal')
plt.show()

# 18.  Releases by Industry and Year
industry_year_releases = data.groupby(['INDUSTRY SECTOR', 'YEAR'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(24, 12))
sns.lineplot(x='YEAR', y='TOTAL RELEASES', hue='INDUSTRY SECTOR', data=industry_year_releases)
plt.title('Total Releases by Industry Over Time')
plt.show()

# 19.  Releases by State and Year
state_year_releases = data.groupby(['ST', 'YEAR'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(24, 12))
sns.lineplot(x='YEAR', y='TOTAL RELEASES', hue='ST', data=state_year_releases)
plt.title('Total Releases by State Over Time')
plt.show()


chemical_industry_releases = data.groupby(['CHEMICAL', 'INDUSTRY SECTOR'])['TOTAL RELEASES'].sum().reset_index()

# 20. Top 10 chemicals based on total releases
top_10_chemicals = chemical_industry_releases.groupby('CHEMICAL')['TOTAL RELEASES'].sum().sort_values(ascending=False).head(10).index.tolist()

chemical_industry_releases_top_10 = chemical_industry_releases[chemical_industry_releases['CHEMICAL'].isin(top_10_chemicals)]

plt.figure(figsize=(16, 8))
sns.barplot(x='CHEMICAL', y='TOTAL RELEASES', hue='INDUSTRY SECTOR', data=chemical_industry_releases_top_10)
plt.title('Total Releases by Chemical and Industry (Top 10 Chemicals)')
plt.xlabel('Chemical')
plt.ylabel('Total Releases')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Industry Sector', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#21. Total Releases

variable_to_analyze = data['TOTAL RELEASES']
sm.qqplot(variable_to_analyze, line='s')
plt.title('QQ Plot of Total Releases')
plt.show()