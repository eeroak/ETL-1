import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector

df = pd.read_csv('ETL-1\\data\\EVPData_Clean.csv', low_memory=False)
df = df.drop(columns='State ') # too lazy to edit my table in the database, so I just removed the column
df.columns = df.columns.str.strip() # Remove leading and trailing whitespaces

df = df.rename(columns={'VIN (1-10)': 'VIN', # Rename columns to match the Snowflake table and better readability
                        'County': 'COUNTY',
                        'City': 'CITY',
                        'Postal Code': 'POSTALCODE',
                        'Make': 'MAKE',
                        'Model': 'MODEL',
                        'Model Year': 'MODELYEAR',
                        'Electric Vehicle Type': 'EVTYPE',
                        'Clean Alternative Fuel Vehicle (CAFV) Eligibility': 'CAFV',
                        'Electric Range': 'ELERANGE',
                        'Base MSRP': 'MSRP',
                        'Legislative District': 'LEGISLATIVEDISTRICT',
                        'DOL Vehicle ID': 'DOLID',
                        'Vehicle Location': 'LOCATION',
                        'Electric Utility': 'ELEUTILITY',
                        '2020 Census Tract': 'CENSUSTRACT',})

df = df.astype(str) # Convert all columns to string
print(df.columns)

# Snowflake connection parameters (had to remove the actual values for security reasons, but it works)
sf_credentials = {
    'account': '',
    'user': '',
    'password': '',
    'warehouse': 'ETL1',
    'database': 'ETL1',
    'schema': 'ETL',
    'role': 'ACCOUNTADMIN'
}

# Establish a connection
conn = snowflake.connector.connect(**sf_credentials)
# Write the DataFrame to Snowflake
success, nchunks, nrows, _ = write_pandas(conn, df, 'EVPDATA1')