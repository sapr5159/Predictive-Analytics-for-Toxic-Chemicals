import pandas as pd
import numpy as np
data=pd.read_csv('combined_tri_data_2014_2023.csv',low_memory=False)
#Merging Underground class values to get total quantity of the chemical injected on site at the facility into underground injection wells.
data['54. 5.4 - UNDERGROUND'] = data['55. 5.4.1 - UNDERGROUND CL I'] + data['56. 5.4.2 - UNDERGROUND C II-V']
#Merging LANDFILLS class values to get total quantity of the chemical released to landfills at the facility
data['57. 5.5.1 - LANDFILLS'] = data['58. 5.5.1A - RCRA C LANDFILL'] + data['59. 5.5.1B - OTHER LANDFILLS']
# Let's remove the "Not Needed" columns from the dataset.

not_needed_columns = [
    '3. FRS ID',
 '5. STREET ADDRESS',
 '7. COUNTY',
 '9. ZIP',
 '10. BIA',
 '11. TRIBE',
 '14. HORIZONTAL DATUM',
 '17. STANDARD PARENT CO NAME',
 '18. FOREIGN PARENT CO NAME',
 '19. FOREIGN PARENT CO DB NUM',
 '20. STANDARD FOREIGN PARENT CO NAME',
 '24. PRIMARY SIC',
 '25. SIC 2',
 '26. SIC 3',
 '27. SIC 4',
 '28. SIC 5',
 '29. SIC 6',
 '30. PRIMARY NAICS',
 '31. NAICS 2',
 '32. NAICS 3',
 '33. NAICS 4',
 '34. NAICS 5',
 '35. NAICS 6',
 '36. DOC_CTRL_NUM',
 '38. ELEMENTAL METAL INCLUDED',
 '39. TRI CHEMICAL/COMPOUND ID',
 '40. CAS#',
 '41. SRS ID',
 '49. FORM TYPE',
 '55. 5.4.1 - UNDERGROUND CL I',
 '56. 5.4.2 - UNDERGROUND C II-V',
 '58. 5.5.1A - RCRA C LANDFILL',
 '59. 5.5.1B - OTHER LANDFILLS',
 '62. 5.5.3A - RCRA SURFACE IM',
 '63. 5.5.3B - OTHER SURFACE I',
 '69. 6.2 - M10',
 '70. 6.2 - M41',
 '71. 6.2 - M62',
 '72. 6.2 - M40 METAL',
 '73. 6.2 - M61 METAL',
 '74. 6.2 - M71',
 '75. 6.2 - M81',
 '76. 6.2 - M82',
 '77. 6.2 - M72',
 '78. 6.2 - M63',
 '79. 6.2 - M66',
 '80. 6.2 - M67',
 '81. 6.2 - M64',
 '82. 6.2 - M65',
 '83. 6.2 - M73',
 '84. 6.2 - M79',
 '85. 6.2 - M90',
 '86. 6.2 - M94',
 '87. 6.2 - M99',
 '89. 6.2 - M20',
 '90. 6.2 - M24',
 '91. 6.2 - M26',
 '92. 6.2 - M28',
 '93. 6.2 - M93',
 '95. 6.2 - M56',
 '96. 6.2 - M92',
 '98. 6.2 - M40 NON-METAL',
 '99. 6.2 - M50',
 '100. 6.2 - M54',
 '101. 6.2 - M61 NON-METAL',
 '102. 6.2 - M69',
 '103. 6.2 - M95',
]

# Remove the unnecessary columns from the dataset
cleaned_data = data.drop(columns=not_needed_columns, errors='ignore')

# Show the cleaned dataset columns
cleaned_data_columns = cleaned_data.columns.tolist()
cleaned_data_columns, len(cleaned_data_columns)  # List of remaining columns and count
# Save the cleaned dataset to a CSV file
# cleaned_data.to_csv('cleaned_2012_us.csv', index=False)
# cleaned_data.columns.tolist()
cleaned_data_u = cleaned_data.copy()
cleaned_data_u.columns = cleaned_data.columns.str.replace(r'^\d+\.\s*', '', regex=True)
cleaned_data_u.columns = cleaned_data_u.columns.str.replace(r'^\d+(\.\d+)*\s*-\s*', '', regex=True)
# import pandas as pd
# df=pd.read_csv("cleaned_removed_num_2014_to_2023_us.csv", low_memory=False)
new_column_names = {
    '8.1A - ON-SITE CONTAINED': 'ON-SITE CONTAINED',
    '8.1B - ON-SITE OTHER': 'ON-SITE OTHER',
    '8.1C - OFF-SITE CONTAIN': 'OFF-SITE CONTAIN',
    '8.1D - OFF-SITE OTHER R': 'OFF-SITE OTHER RELEASES',
    'PRODUCTION WSTE (8.1-8.7)':'PRODUCTION WASTE'
}
cleaned_data_u = cleaned_data_u.rename(columns=new_column_names)
cleaned_data_u.shape
cleaned_data_u.columns.tolist()
columns_to_convert = [
    'FUGITIVE AIR',
    'STACK AIR',
    'WATER',
    'UNDERGROUND',
    'LANDFILLS',
    'LAND TREATMENT',
    'SURFACE IMPNDMNT',
    'OTHER DISPOSAL',
    'ON-SITE RELEASE TOTAL',
    'POTW - TRNS RLSE',
    'POTW - TRNS TRT',
    'POTW - TOTAL TRANSFERS',
    'OFF-SITE RELEASE TOTAL',
    'OFF-SITE RECYCLED TOTAL',
    'OFF-SITE ENERGY RECOVERY T',
    'OFF-SITE TREATED TOTAL',
    'UNCLASSIFIED',
    'TOTAL TRANSFER',
    'TOTAL RELEASES',
    'RELEASES',
    'ON-SITE CONTAINED',
    'ON-SITE OTHER',
    'OFF-SITE CONTAIN',
    'OFF-SITE OTHER RELEASES',
    'ENERGY RECOVER ON',
    'ENERGY RECOVER OF',
    'RECYCLING ON SITE',
    'RECYCLING OFF SIT',
    'TREATMENT ON SITE',
    'TREATMENT OFF SITE',
    'PRODUCTION WASTE',
    'ONE-TIME RELEASE',
]


for i in range(len(cleaned_data_u)):
    if cleaned_data_u.loc[i, 'UNIT OF MEASURE'] == 'Grams':
        cleaned_data_u.loc[i, 'UNIT OF MEASURE']='Pounds'
        for col in columns_to_convert:
            cleaned_data_u.loc[i, col] = cleaned_data_u.loc[i,col]/453.6
subset_columns = ['YEAR', 'TRIFD', 'FACILITY NAME', 'CITY', 'ST', 'LATITUDE',
                  'LONGITUDE', 'PARENT CO NAME', 'PARENT CO DB NUM', 'FEDERAL FACILITY',
                  'INDUSTRY SECTOR CODE', 'INDUSTRY SECTOR', 'CHEMICAL']

# Identify the columns to sum values for
columns_to_sum = ['FUGITIVE AIR', 'STACK AIR', 'WATER', 'UNDERGROUND', 'LANDFILLS',
                  'LAND TREATMENT', 'SURFACE IMPNDMNT', 'OTHER DISPOSAL',
                  'ON-SITE RELEASE TOTAL', 'POTW - TRNS RLSE', 'POTW - TRNS TRT',
                  'POTW - TOTAL TRANSFERS', 'OFF-SITE RELEASE TOTAL',
                  'OFF-SITE RECYCLED TOTAL', 'OFF-SITE ENERGY RECOVERY T',
                  'OFF-SITE TREATED TOTAL', 'UNCLASSIFIED', 'TOTAL TRANSFER',
                  'TOTAL RELEASES', 'RELEASES', 'ON-SITE CONTAINED',
                  'ON-SITE OTHER', 'OFF-SITE CONTAIN', 'OFF-SITE OTHER RELEASES',
                  'ENERGY RECOVER ON', 'ENERGY RECOVER OF', 'RECYCLING ON SITE',
                  'RECYCLING OFF SIT', 'TREATMENT ON SITE', 'TREATMENT OFF SITE',
                  'PRODUCTION WASTE', 'ONE-TIME RELEASE','PRODUCTION RATIO']

# Identify duplicate rows based on key subset columns
duplicates = cleaned_data_u[cleaned_data_u.duplicated(subset=subset_columns, keep=False)]
print(duplicates.shape)
summed_duplicates = duplicates.groupby(subset_columns)[columns_to_sum].sum().reset_index()
#mean_df = duplicates.groupby(subset_columns).mean().reset_index()
# Drop the original duplicate rows from the DataFrame
cleaned_data_u = cleaned_data_u.drop_duplicates(subset=subset_columns, keep=False)

# Append the summed duplicates back into the original DataFrame
cleaned_data_u = pd.concat([cleaned_data_u, summed_duplicates], ignore_index=True)
cleaned_data_u.shape
cleaned_data_u.to_csv('cleaned_removed_num_2014_to_2023_us.csv', index=False)
missing_values = data.isnull().sum()
print("Missing Values",missing_values)
data = cleaned_data_u
df = data.copy()
df = df.drop(columns=['TRIFD', 'FACILITY NAME', 'CITY', 'LATITUDE', 'LONGITUDE', 
                      'PARENT CO NAME', 'PARENT CO DB NUM', 'ONE-TIME RELEASE', 
                      'PROD_RATIO_OR_ ACTIVITY', 'ST', 'FEDERAL FACILITY'])
# Fill categorical missing values with 'Unknown'
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna('Unknown', inplace=True)

# Fill numeric missing values with the column mean
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
df.to_csv('cleaned_data_for_models.csv', index=False)


print("Total number of rows and columns after exploration: ",df.shape)
df.head()