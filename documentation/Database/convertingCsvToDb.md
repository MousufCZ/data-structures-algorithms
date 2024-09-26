Ah, so you're looking to automate the process of converting multiple `.csv` files into corresponding SQLite `.db` files. That's a neat task, and definitely something that can be done efficiently in Python! I'll help you modify your script to handle this in a loop, ensuring it reads all `.csv` files in a directory, creates matching `.db` files, and writes the data to SQLite tables.

Here's a step-by-step breakdown of how the modified script will work:

1. **List all `.csv` files** in a specified directory.
2. **Iterate** through each file.
3. **Read** each `.csv` file into a pandas DataFrame.
4. **Create an SQLite database** with the same name as the `.csv` file.
5. **Write the DataFrame** to the corresponding `.db` file as a table.
6. **Close** the SQLite connection.

Now, here's the updated version of your script:

```python
import pandas as pd
import sqlite3
import os

# Specify the directory containing the CSV files
csv_dir = '/home/mousuf/dsa/database/formula1/f1/'

# Loop through all files in the directory
for file_name in os.listdir(csv_dir):
    # Check if the file is a .csv file
    if file_name.endswith('.csv'):
        # Define the full file path
        csv_file = os.path.join(csv_dir, file_name)
        
        # Read the CSV into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Create a connection to the SQLite database with the same name as the .csv file
        # Remove the '.csv' extension from the file name to create the database name
        db_name = file_name.replace('.csv', '.db')
        db_path = os.path.join('./database/formula1/db/', db_name)
        
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)

        # Write the DataFrame to an SQLite table
        # Use the CSV file name (without '.csv') as the table name
        table_name = file_name.replace('.csv', '')
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        # Print progress
        print(f"Successfully written {file_name} to {db_name} as table {table_name}.")

        # Close the connection
        conn.close()
```

### Explanation of Changes:
1. **`os.listdir(csv_dir)`**: This function lists all files in the specified directory.
2. **`if file_name.endswith('.csv'):`**: This ensures that only `.csv` files are processed.
3. **`db_name = file_name.replace('.csv', '.db')`**: This converts the `.csv` file name to a `.db` file name.
4. **`df.to_sql(table_name, conn, if_exists='replace', index=False)`**: This writes the pandas DataFrame to a table in the SQLite database. The table name is based on the CSV file name (without `.csv`).

### What this script does:
- For every `.csv` file in the `/home/mousuf/dsa/database/formula1/f1/` directory, it:
  - Reads the `.csv` file into a pandas DataFrame.
  - Creates a corresponding `.db` file in the `./database/formula1/db/` directory.
  - Writes the DataFrame to a table in the SQLite database, with the table name matching the `.csv` file name (without the `.csv` extension).
  - Closes the connection to the SQLite database after writing each file.

### Notes:
- **Directory Paths**: Ensure that the directories exist (`./database/formula1/db/`). If they don't, you may need to create them using `os.makedirs()` or manually.
- **Error Handling**: You may want to add error handling (e.g., using `try-except`) in case there are issues reading certain `.csv` files or connecting to the SQLite database.

### Optional Additions:
- If you'd like to log errors or handle specific exceptions, you can wrap the core functionality of reading/writing in a `try-except` block.

Let me know if you have more questions or if something doesn't work as expected.


# In a class
Sure! I'll encapsulate the logic in a class and create a driver function to execute the functionality. Here's how you can structure your code:

### Steps:
1. Create a class called `CSVtoSQLiteConverter`.
2. Inside the class, define a method called `convert_all_csvs_to_db` to handle the conversion process.
3. Use a driver function `main()` to execute the class.

### Code Implementation:

```python
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
```

### Explanation:

1. **`CSVtoSQLiteConverter` class:**
   - The `__init__` method takes two parameters: the CSV directory (`csv_dir`) and the directory where the SQLite databases (`db_dir`) will be stored.
   - The method `convert_all_csvs_to_db` handles reading the CSV files, creating SQLite databases, and writing tables.
   - `ensure_db_directory` ensures that the database directory exists. If it doesn't, it creates the directory.

2. **Driver function `main()`:**
   - Sets the paths for the CSV and database directories.
   - Instantiates the `CSVtoSQLiteConverter` class.
   - Ensures the database directory exists.
   - Calls the `convert_all_csvs_to_db` method to start the conversion process.

3. **Error Handling:**
   - I've added a `try-except` block inside the `convert_all_csvs_to_db` method to catch and print any errors that occur during the CSV to SQLite conversion process.

### How to Run:
- Place your CSV files in the directory specified in `csv_directory` (e.g., `/home/mousuf/dsa/database/formula1/f1/`).
- The SQLite databases will be saved in the `db_directory` (e.g., `./database/formula1/db/`).
- Simply run the script, and it will convert each CSV to its corresponding `.db` file and table.

Let me know if you need further customization or any clarification!