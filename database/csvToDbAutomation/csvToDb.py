import pandas as pd
import sqlite3
import os
'''
class CSVtoSQLiteConverter:
    def __init__(self, csv_dir, db_path):
        self.csv_dir = csv_dir
        self.db_path = db_path

    def convert_all_csvs_to_db(self):
        try:
            conn = sqlite3.connect(self.db_path)

            for file_name in os.listdir(self.csv_dir):
                if file_name.endswith('.cvs'):
                    csv_file = os.path.join(self.csv_dir, file_name)
                    
                    df = pd.read_csv(csv_file)

                    table_name = file_name.replace('.csv', '')

                    df.to_sql(table_name, conn, if_exists='replace', index=False, )
                    print(f"Successfully written {file_name} to {self.db_path} as table {table_name}.")

                    conn.close()

        except Exception as e:
            print(f"Error processing CSV file: {e} ")


    # Optional: Add a method to ensure the DB directory exists
    def ensure_db_directory(self):
        db_dir = os.path.dirname(self.db_path)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)
            print(f"Created directory {db_dir}")
'''

class CSVtoSQLiteConverter:
    def __init__(self, csv_dir, db_path):
        self.csv_dir = csv_dir  # Directory where CSV files are stored
        self.db_path = db_path  # Path to the .db file where all tables will be stored
   
    def convert_all_csvs_to_db(self):
        try:
            # Create a connection to the SQLite database
            conn = sqlite3.connect(self.db_path)

            # Loop through all files in the CSV directory
            for file_name in os.listdir(self.csv_dir):
                # Check if the file is a .csv file
                if file_name.endswith('.csv'):
                    # Define the full CSV file path
                    csv_file = os.path.join(self.csv_dir, file_name)

                    # Read the CSV into a pandas DataFrame
                    df = pd.read_csv(csv_file)

                    # Use the CSV file name (without '.csv') as the table name
                    table_name = file_name.replace('.csv', '')

                    # Write the DataFrame to an SQLite table
                    df.to_sql(table_name, conn, if_exists='replace', index=False)

                    # Print progress
                    print(f"Successfully written {file_name} to {self.db_path} as table {table_name}.")
            
            # Close the connection after all tables are written
            conn.close()

        except Exception as e:
            print(f"Error processing CSV files: {e}")

    # Optional: Add a method to ensure the DB directory exists
    def ensure_db_directory(self):
        db_dir = os.path.dirname(self.db_path)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)
            print(f"Created directory {db_dir}")

# Driver function
def main():
    # Define paths for the CSV directory and the single DB file
    csv_directory = './database/formula1/f1Database/f1csvs/'
    db_path = './database/formula1/f1Database/formula1_data2.db'  # Single .db file for all tables

    # Instantiate the CSV to SQLite converter class
    converter = CSVtoSQLiteConverter(csv_directory, db_path)
    
    # Ensure the database directory exists
    converter.ensure_db_directory()
    
    # Convert all CSV files to tables in a single SQLite database
    converter.convert_all_csvs_to_db()

# Run the driver function
if __name__ == "__main__":
    main()