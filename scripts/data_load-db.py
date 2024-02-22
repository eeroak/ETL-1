from sqlalchemy import create_engine
import pandas as pd

# Function to load the data into the ETL-1 PostgreSQL database

def data_load_db(table_name):
    
    # Load the data from the csv file
    df = pd.read_csv('ETL-1\data\EVPData_Clean.csv', low_memory=False)
    # Create a connection to the database
    engine = create_engine('postgresql://postgres:1234@localhost:5432/ETL-1')
    # Load the data into the database
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    return df
data_load_db('Electric_Vehicle_Population_Data')

