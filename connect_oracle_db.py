# Script to help  me connect to an Oracle database and query data
import cx_Oracle
import pandas as pd 

cx.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_9"

connection=cx.connect(user="yourusername",password="yourpassword",dns="yourdns")

# Create a cursor object to execute queries
cursor = connection.cursor()

# Define your SQL query
sql_query = 'SELECT * FROM your_table_name'

df = pd.read_sql(query, con=connection)

# Print the data frame
df

connection.close()
