import sqlite3



import os
import django


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

import os
from django.conf import settings
from django.db import connection

# Configure settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kararaeats_web.settings')

def drop_unique_constraint():
    with connection.cursor() as cursor:
        # Rename the original table
        cursor.execute("ALTER TABLE accounts_customuser RENAME TO accounts_customuser_oldd;")

        # Create a new table without the unique constraint on 'address'
        cursor.execute("""
        CREATE TABLE accounts_customuser (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL,
            last_login DATETIME,
            is_superuser BOOLEAN NOT NULL,
            username TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            is_staff BOOLEAN NOT NULL,
            is_active BOOLEAN NOT NULL,
            date_joined DATETIME NOT NULL,
            address TEXT,
            whatsapp_num TEXT
        );
        """)

        # Copy data from the old table to the new one
        cursor.execute("""
        INSERT INTO accounts_customuser (
            id, password, last_login, is_superuser, username, first_name, last_name,
            email, is_staff, is_active, date_joined, address, whatsapp_num
        )
        SELECT
            id, password, last_login, is_superuser, username, first_name, last_name,
            email, is_staff, is_active, date_joined, address, whatsapp_num
        FROM accounts_customuser_old;
        """)

        # Drop the old table
        cursor.execute("DROP TABLE accounts_customuser_old;")
        print("Constraint on 'address' dropped successfully.")

# Call the function
if __name__ == '__main__':
    # Replace 'your_project.settings' with the actual path to your settings file
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kararaeats_web.settings')

    # Initialize Django
    django.setup()
    from whatsapp_manager.views import customers_without_orders
    from datetime import datetime

    # Define the range for created_at
    start_date = datetime(2024, 1, 29)  # Start date
    end_date = datetime(2024, 12, 31)  # End date
    orders = customers_without_orders(start_date, end_date)
    #for order in orders:
    #    print(order)
    #for order in orders:
    #    print(f"Order ID: {order['id']}, WhatsApp: {order['user__whatsapp_num']}, User: {order['user__username']}")

    #drop_unique_constraint()


    # Replace 'your_database.db' with the path to your SQLite database file
    #db_path = 'db.sqlite3'
    #read_sqlite_db(db_path)
