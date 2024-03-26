# Testing Snowflake connection and data extraction from a table in Snowflake
import snowflake.connector


# Establish a connection to Snowflake
sf_credentials = {
    'account': '',
    'user': '',
    'password': '',
    'warehouse': 'ETL1',
    'database': 'ETL1',
    'schema': 'ETL',
    'role': 'ACCOUNTADMIN'
}

con = snowflake.connector.connect(**sf_credentials)
cur = con.cursor()

try:
    cur.execute("SELECT * FROM EVPDATA1") # Fetch all rows from the table in Snowflake
    df = cur.fetch_pandas_all() # Fetch the result of the query and store it in a pandas dataframe
    
except Exception as e: # Catch any exception and print it
    print(e)
    
finally: # Close the cursor and connection
    cur.close()
    con.close()
    
#print(df)