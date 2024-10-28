import sqlite3


def read_sqlite_db(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query to get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Print the tables and their entries
    for table_name in tables:
        table_name = table_name[0]
        print(f"Table: {table_name}")

        # Query to get all entries from the table
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        # Get column names
        column_names = [description[0] for description in cursor.description]

        # Print column names
        print("Columns: " + ", ".join(column_names))

        # Print rows
        for row in rows:
            print(row)

        print("\n")

    # Close the connection
    conn.close()


# Replace 'your_database.db' with the path to your SQLite database file
db_path = 'db.sqlite3'
read_sqlite_db(db_path)
