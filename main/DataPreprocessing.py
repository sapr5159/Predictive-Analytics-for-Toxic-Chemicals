import pandas as pd
import os
import requests
base_url = "https://data.epa.gov/efservice/downloads/tri/mv_tri_basic_download/"
suffix_url = "_US/csv"

output_dir = 'tri_data_2014_2023'
os.makedirs(output_dir, exist_ok=True)

for year in range(2014, 2024):
    download_url = f"{base_url}{year}{suffix_url}"
    file_name = f"tri_data_{year}.csv"
    file_path = os.path.join(output_dir, file_name)
    response = requests.get(download_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download data for {year}, status code: {response.status_code}")

input_dir = 'tri_data_2014_2023'
dataframes = []
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_dir, filename)
        df = pd.read_csv(file_path, low_memory=False)
        dataframes.append(df)
combined_df = pd.concat(dataframes, ignore_index=True)
combined_csv_path = 'combined_tri_data_2014_2023.csv'
combined_df.to_csv(combined_csv_path, index=False)
print(f"Combined CSV saved to {combined_csv_path}")

