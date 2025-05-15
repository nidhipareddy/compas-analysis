import sqlite3
import pandas as pd

def inspect_sqlite_db(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    print("Tables in the database:")
    for name in table_names:
        print(f"  - {name}")

    print("\nSchema and sample data:")
    for table in table_names:
        print(f"\nTable: {table}")
        # Print schema
        cursor.execute(f"PRAGMA table_info({table});")
        schema = cursor.fetchall()
        print("Schema:")
        for col in schema:
            print(f"  - {col[1]} ({col[2]})")

        # Preview first 5 rows
        try:
            df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 5;", conn)
            print("\nSample data:")
            print(df)
        except Exception as e:
            print(f"  Could not fetch data: {e}")

    # Close the connection
    conn.close()

def count_unique_ids_in_people(db_path):
    """
    Connects to a SQLite database and returns the number of unique IDs in the 'people' table.

    Parameters:
        db_path (str): Path to the SQLite database file.

    Returns:
        int: Count of unique IDs in the 'id' column of the 'people' table.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(DISTINCT id) FROM people;")
    result = cursor.fetchone()[0]

    conn.close()
    print(result)
    return result

# Example usage
db_path = "/Users/blag/Documents/UChicago MS/2025 Spring/Machine Learning 2/compas-analysis-master/compas.db"  
inspect_sqlite_db(db_path)
count_unique_ids_in_people(db_path)