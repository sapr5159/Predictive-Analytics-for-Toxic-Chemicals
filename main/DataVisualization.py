import pandas as pd
import os
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.ticker as mtick
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


# # 8. Pairplot of release categories
# sns.pairplot(data[[
#     'FUGITIVE AIR', 'STACK AIR', 'WATER', 'UNDERGROUND', 'LANDFILLS',
#     'LAND TREATMENT', 'SURFACE IMPNDMNT', 'OTHER DISPOSAL'
# ]])
# plt.show()


# 9. Barplot of releases by State
plt.figure(figsize=(12, 6))
sns.countplot(x='ST', data=data)
plt.title('Number of Facilities by State')
plt.xticks(rotation=90)
plt.show()

# 10. Releases by State (Total Releases)
state_releases = data.groupby('ST')['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='ST', y='TOTAL RELEASES', data=state_releases)
plt.title('Total Releases by State')
plt.xticks(rotation=90)
plt.show()

# # 11. Releases by Facility Type
# plt.figure(figsize=(12, 6))
# sns.countplot(x='FACILITY TYPE', data=data)
# plt.title('Number of Facilities by Type')
# plt.xticks(rotation=90)
# plt.show()

# # 12. Total Releases by Facility Type
# facility_releases = data.groupby('FACILITY TYPE')['TOTAL RELEASES'].sum().reset_index()
# plt.figure(figsize=(12, 6))
# sns.barplot(x='FACILITY TYPE', y='TOTAL RELEASES', data=facility_releases)
# plt.title('Total Releases by Facility Type')
# plt.xticks(rotation=90)
# plt.show()

# 13. Line plot of total releases over the years
plt.figure(figsize=(10, 6))
sns.lineplot(x='YEAR', y='TOTAL RELEASES', data=data)
plt.title('Total Releases Over Time')
plt.show()

# # 14. Releases by Chemical and Year
# plt.figure(figsize=(12, 6))
# sns.lineplot(x='YEAR', y='TOTAL RELEASES', hue='CHEMICAL', data=data)
# plt.title('Total Releases by Chemical Over Time')
# plt.xticks(rotation=90)
# plt.show()

# 15. Stacked barplot of releases by different release categories
release_categories = ['FUGITIVE AIR', 'STACK AIR', 'WATER', 'UNDERGROUND', 'LANDFILLS']
release_data = data[release_categories].sum()
plt.figure(figsize=(10, 6))
release_data.plot(kind='bar', stacked=True)
plt.title('Total Releases by Release Category')
plt.show()

# 16. Boxplot of releases by different release categories
plt.figure(figsize=(10, 6))
sns.boxplot(data=data[release_categories])
plt.title('Distribution of Releases by Release Category')
plt.show()

# # 17. Violin plot of releases by different release categories
# plt.figure(figsize=(10, 6))
# sns.violinplot(data=data[release_categories])
# plt.title('Distribution of Releases by Release Category')
# plt.show()

# 18.  Releases by Industry and Year
industry_year_releases = data.groupby(['INDUSTRY SECTOR', 'YEAR'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='YEAR', y='TOTAL RELEASES', hue='INDUSTRY SECTOR', data=industry_year_releases)
plt.title('Total Releases by Industry Over Time')
plt.show()

# 19.  Releases by State and Year
state_year_releases = data.groupby(['ST', 'YEAR'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='YEAR', y='TOTAL RELEASES', hue='ST', data=state_year_releases)
plt.title('Total Releases by State Over Time')
plt.show()


# 20.  Releases by Chemical and Industry
chemical_industry_releases = data.groupby(['CHEMICAL', 'INDUSTRY SECTOR'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='CHEMICAL', y='TOTAL RELEASES', hue='INDUSTRY SECTOR', data=chemical_industry_releases)
plt.title('Total Releases by Chemical and Industry')
plt.xticks(rotation=90)
plt.show()

federal_vs_non_federal = data['FEDERAL FACILITY'].value_counts()

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(federal_vs_non_federal, labels=federal_vs_non_federal.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart for Federal vs. Non-Federal Facilities')
plt.axis('equal')
plt.show()

onsite_releases = data['ON-SITE RELEASE TOTAL'].sum()
offsite_releases = data['OFF-SITE RELEASE TOTAL'].sum()

# Create the pie chart
labels = ['On-Site Releases', 'Off-Site Releases']
sizes = [onsite_releases, offsite_releases]
explode = (0.1, 0)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart for On-Site vs. Off-Site Release Methods')
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

# Get the top 10 chemicals based on total releases
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

variable_to_analyze = data['TOTAL RELEASES']

# Generate the QQ plot
sm.qqplot(variable_to_analyze, line='s')
plt.title('QQ Plot of Total Releases')
plt.show()

# Plotting number of facilities by state
plt.figure(figsize=(12, 8))
sns.countplot(y='ST', data=data, order=data['ST'].value_counts().index)
plt.title("Number of Facilities by State")
plt.xlabel("Count")
plt.ylabel("State")
plt.show()

# Relationship between CARCINOGEN and TOTAL RELEASES
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='CARCINOGEN', y='TOTAL RELEASES')
plt.title("Total Releases by Carcinogen Classification")
plt.show()

industry_trends = data.groupby(['YEAR', 'INDUSTRY SECTOR CODE'])['TOTAL RELEASES'].sum().reset_index()
plt.figure(figsize=(12, 8))
sns.lineplot(data=industry_trends, x='YEAR', y='TOTAL RELEASES', hue='INDUSTRY SECTOR CODE')
plt.title('Trend of Toxic Releases by Industry (2003 - Present)')
plt.ylabel('Total Release Amount')
plt.xlabel('Year')
plt.legend(title='Industry Sector', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

df = data.copy()

# Combine 'FUGITIVE AIR' and 'STACK AIR' into a single column
df['AIR RELEASES'] = df['FUGITIVE AIR'] + df['STACK AIR']

# Combine 'UNDERGROUND', 'LANDFILLS', 'LAND TREATMENT', 'SURFACE IMPNDMNT' into a single column
df['LAND RELEASES'] = df['UNDERGROUND'] + df['LANDFILLS'] + df['LAND TREATMENT'] + df['SURFACE IMPNDMNT']



# Combine 'ON-SITE RELEASE TOTAL', 'TREATMENT ON SITE','ENERGY RECOVER ON', 'RECYCLING ON SITE' into 'TOTAL ON-SITE'
df['TOTAL ON-SITE'] = df['ON-SITE RELEASE TOTAL'] + df['TREATMENT ON SITE'] + df['ENERGY RECOVER ON'] + df['RECYCLING ON SITE']

columns_to_combine = ['ENERGY RECOVER ON', 'ENERGY RECOVER OF', 'RECYCLING ON SITE',
                     'RECYCLING OFF SIT', 'TREATMENT ON SITE', 'TREATMENT OFF SITE']
df['ON-SITE OTHER TREATMENT'] = df['ENERGY RECOVER ON']+df['RECYCLING ON SITE']+df['TREATMENT ON SITE']

df['OFF-SITE OTHER TREATMENT']=df['ENERGY RECOVER OF']+df['RECYCLING OFF SIT']+df['TREATMENT OFF SITE']

df['TOTAL OTHER TREATMENT'] = df[columns_to_combine].sum(axis=1)

df = df.drop(columns=columns_to_combine, errors='ignore')
carcinogens_yes = df[df['CARCINOGEN'] == 'YES']['CHEMICAL'].unique()
carcinogens_no = df[df['CARCINOGEN'] == 'NO']['CHEMICAL'].unique()
for chemical in carcinogens_yes:
    df.loc[df['CHEMICAL'] == chemical, 'CARCINOGEN'] = df.loc[df['CHEMICAL'] == chemical, 'CARCINOGEN'].fillna('YES')

for chemical in carcinogens_no:
    df.loc[df['CHEMICAL'] == chemical, 'CARCINOGEN'] = df.loc[df['CHEMICAL'] == chemical, 'CARCINOGEN'].fillna('NO')

df.head()

df = df[(df['TOTAL OTHER TREATMENT'] != 0) | (df['TOTAL RELEASES'] != 0)]

columns_to_remove = ['TRIFD','PBT', 'PFAS', 'UNDERGROUND', 'LANDFILLS', 'LAND TREATMENT','LATITUDE','LONGITUDE',
       'SURFACE IMPNDMNT','METAL', 'METAL CATEGORY',
       'POTW - TRNS RLSE', 'POTW - TRNS TRT', 'POTW - TOTAL TRANSFERS','UNIT OF MEASURE',
        'OFF-SITE RECYCLED TOTAL',
       'OFF-SITE ENERGY RECOVERY T', 'OFF-SITE TREATED TOTAL', 'UNCLASSIFIED','RELEASES', 'ON-SITE CONTAINED',
       'ON-SITE OTHER', 'OFF-SITE CONTAIN', 'OFF-SITE OTHER RELEASES','PRODUCTION WASTE', 'ONE-TIME RELEASE', 'PROD_RATIO_OR_ ACTIVITY',
       'PRODUCTION RATIO','FUGITIVE AIR', 'STACK AIR','PARENT CO NAME', 'PARENT CO DB NUM', 'FEDERAL FACILITY',
       'INDUSTRY SECTOR CODE','CLEAN AIR ACT CHEMICAL','CLEAN AIR ACT CHEMICAL','CLASSIFICATION']

df = df.drop(columns=columns_to_remove, errors='ignore')

print(df.shape)
df.head()

release_summary = df['TOTAL RELEASES'].describe()
treatment_summary = df['TOTAL OTHER TREATMENT'].describe()

print("Summary of Total Releases:")
print(release_summary)

print("\nSummary of Total Treatment:", treatment_summary)
pd.set_option('display.float_format', '{:,.0f}'.format)
columns_to_analyze = [ 'TOTAL OTHER TREATMENT','TOTAL TRANSFER',
                      'TOTAL RELEASES', 'TOTAL ON-SITE',]

# Get descriptive statistics
desc_stats = df[columns_to_analyze].describe()

# Print the descriptive statistics
print(desc_stats)

grouped_df = df.groupby(['YEAR', 'INDUSTRY SECTOR'])['TOTAL RELEASES'].sum().unstack()

ax = grouped_df.plot(kind='bar', stacked=True, figsize=(12, 6))


plt.xlabel('Year')
plt.ylabel('Total Releases')
plt.title('Total Releases by Industry Sector')
plt.legend(title='Industry Sector', loc='center left', bbox_to_anchor=(1, 0.5))
plt.xticks(rotation=45, ha='right')
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
# Show the plot
plt.tight_layout()
plt.show()

grouped_df = df.groupby('YEAR')[['AIR RELEASES', 'LAND RELEASES', 'WATER', 'OTHER DISPOSAL']].sum()


ax = grouped_df.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')

# Add Chart Details
ax.set_title('Releases by Disposal Method and Year', fontsize=14)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Releases (in Pounds)', fontsize=12)

ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

# Add Legend and Layout Adjustments
plt.legend(title='Disposal Method', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show Plot
plt.show()


grouped_df = df.groupby('YEAR')[['TOTAL RELEASES', 'TOTAL TRANSFER', 'TOTAL OTHER TREATMENT']].sum()

ax = grouped_df.plot(kind='bar', stacked=False, figsize=(10, 6), colormap='viridis')

# Add Chart Details
ax.set_title('Total Transfers, Releases, and Other Treatment by Year', fontsize=14)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Quantity ', fontsize=12)

ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

# Add Legend and Layout Adjustments
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show Plot
plt.show()
carcinogen_counts_unique = df.groupby(['YEAR', 'CARCINOGEN'])['CHEMICAL'].nunique().unstack(fill_value=0).reset_index()
plt.figure(figsize=(10, 6))

# Plotting the bar plot
carcinogen_counts_unique.set_index('YEAR').plot(kind='bar', stacked=False, figsize=(10, 6))

# Add titles and labels
plt.title('Carcinogenic vs Non-Carcinogenic Chemicals by Year')
plt.xlabel('Year')
plt.ylabel('Number of Unique Chemicals')
plt.xticks(rotation=0)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
df_2023 = df[df['YEAR'] == 2023]
grouped_df_2023 = df_2023.groupby('YEAR')[[ 'TOTAL RELEASES', 'TOTAL OTHER TREATMENT']].sum()


values = grouped_df_2023.iloc[0].values

# Create the labels for the pie chart
labels = grouped_df_2023.columns

# Create the pie chart
plt.figure(figsize=(6, 6))  # Adjust figure size as needed
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Total Releases, and Other Treatment in 2023')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
df_2023 = df[df['YEAR'] == 2023]

# Calculate totals for 2023
totals_2023 = df_2023[['ON-SITE RELEASE TOTAL', 'OFF-SITE RELEASE TOTAL',
                       'ON-SITE OTHER TREATMENT', 'OFF-SITE OTHER TREATMENT']].sum()

# Plot pie chart
totals_2023.plot.pie(autopct='%1.1f%%', figsize=(6, 6), startangle=90)
plt.title('Proportion of Release and Treatment Types - 2023')
plt.ylabel('')  # Remove y-axis label for clarity
plt.show()


# Yearly trends for different numerical variables
yearly_trends = df.groupby('YEAR')[['ON-SITE RELEASE TOTAL', 'OFF-SITE RELEASE TOTAL',
                                    'ON-SITE OTHER TREATMENT', 'OFF-SITE OTHER TREATMENT']].sum()
# Plot the trends
ax = yearly_trends.plot(figsize=(10, 6), marker='o')
plt.title('Yearly Trends of Total Releases, Other Treatment, and Transfers')
plt.ylabel('Total (in Billions)')
plt.xlabel('Year')

# Format y-axis to display values in billions
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x/1e9:.1f}B'))

# Adjust legend and add grid
plt.legend(title='Category', loc='center left', bbox_to_anchor=(1, 0.5))  # Legend outside
plt.grid(True)  # Optional grid for better readability
plt.show()
unique_chemical_counts = df.groupby('YEAR')['CHEMICAL'].nunique().reset_index()
unique_chemical_counts.rename(columns={'CHEMICAL': 'Unique Chemical Count'}, inplace=True)

plt.figure(figsize=(10, 6))
sns.barplot(data=unique_chemical_counts, x='YEAR', y='Unique Chemical Count', color='skyblue')
plt.title('Unique Chemical Counts by Year')

plt.title('Unique Chemical Counts by Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Unique Chemicals', fontsize=12)
plt.xticks(rotation=45)
plt.show()
# Group by year and sum release types
release_trends = df.groupby('YEAR')[['AIR RELEASES', 'WATER', 'LAND RELEASES']].sum()

# Plot
release_trends.plot(kind='area', stacked=True, figsize=(12, 6), alpha=0.7, cmap='viridis')
plt.title('Trend of Air, Water, and Land Releases Over Time', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Releases', fontsize=12)
plt.legend(title='Category', loc='center left', bbox_to_anchor=(1, 0.5))  # Legend outside
plt.grid(True)
plt.show()
