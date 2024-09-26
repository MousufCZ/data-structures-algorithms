import pandas as pd
import sqlite3
import os

class CSVtoSQLiteConverter:
    def __init__(self, csv_dir, db_dir):
        self.csv_dir = csv_dir  # Directory where CSV files are stored
        self.db_dir = db_dir    # Directory where .db files will be created
   
    def convert_all_csvs_to_db(self):
        # Loop through all files in the CSV directory
        for file_name in os.listdir(self.csv_dir):
            # Check if the file is a .csv file
            if file_name.endswith('.csv'):
                try:
                    # Define the full CSV file path
                    csv_file = os.path.join(self.csv_dir, file_name)
                    
                    # Read the CSV into a pandas DataFrame
                    df = pd.read_csv(csv_file)
                    
                    # Create a corresponding database name (replace .csv with .db)
                    db_name = file_name.replace('.csv', '.db')
                    db_path = os.path.join(self.db_dir, db_name)
                    
                    # Connect to the SQLite database
                    conn = sqlite3.connect(db_path)
                    
                    # Use the CSV file name (without '.csv') as the table name
                    table_name = file_name.replace('.csv', '')
                    
                    # Write the DataFrame to an SQLite table
                    df.to_sql(table_name, conn, if_exists='replace', index=False)
                    
                    # Print progress
                    print(f"Successfully written {file_name} to {db_name} as table {table_name}.")
                    
                    # Close the connection
                    conn.close()
                except Exception as e:
                    print(f"Error processing {file_name}: {e}")

    # Optional: Add a method to ensure the DB directory exists
    def ensure_db_directory(self):
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)
            print(f"Created directory {self.db_dir}")

# Driver function
def main():
    # Define paths for the CSV and DB directories
    csv_directory = '/home/mousuf/dsa/database/formula1/f1/'
    db_directory = './database/formula1/db/'

    # Instantiate the CSV to SQLite converter class
    converter = CSVtoSQLiteConverter(csv_directory, db_directory)
    
    # Ensure the database directory exists
    converter.ensure_db_directory()
    
    # Convert all CSV files to SQLite databases
    converter.convert_all_csvs_to_db()

# Run the driver function
if __name__ == "__main__":
    main()