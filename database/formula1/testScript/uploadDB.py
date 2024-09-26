import pandas as pd
import sqlite3

# Specify the CSV file
csv_file = '/home/mousuf/dsa/database/formula1/f1/circuits.csv'

# Read the CSV into a pandas DataFrame
df = pd.read_csv(csv_file)

# Create a connection to the SQLite database
conn = sqlite3.connect('./database/formula1/db/circuits.db')

# Write the DataFrame to an SQLite table
df.to_sql('circuits', conn, if_exists='replace', index=False)

# Close the connection
conn.close()