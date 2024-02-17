import pandas as pd

data = pd.read_csv('ETL-1\data\Electric_Vehicle_Population_Data.csv', low_memory=False) # Load the data

data.isna().sum() # Check for missing values

#data = data.fillna(data.mean()) # Fill missing values with the mean of the column
#data = data.drop_duplicates() # Remove duplicates

#data.to_csv('/data/Electric_Vehicle_Population_Data.csv', index=False) # Save the data to the same file, overwriting the original