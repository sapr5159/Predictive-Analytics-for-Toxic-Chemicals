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