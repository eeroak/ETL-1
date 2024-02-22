import psycopg2 as pg2
import pandas as pd

# Extract data from the database using psycopg2, as in the loading phase i used SQLalchemy

def extract_data():
    # Connect to the database
    conn = pg2.connect(database='ETL-1', user='postgres', password='1234')
    # Create a cursor
    cur = conn.cursor()
    # Execute the query
    cur.execute('SELECT * FROM "Electric_Vehicle_Population_Data"')
    # Fetch the data in to a pandas dataframe, column names are taken from the description of the cursor
    data = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description]) # <- list comprehension to get the column names

    print(data.head(2)) # Returns the first 2 rows of the dataframe, and 17 columns
    
    # Close, commit the connection and cursor
    conn.commit()
    cur.close()
    conn.close()

extract_data()