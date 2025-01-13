import mysql.connector
import data_read
import database_initialization
import queries

def empty_tables(cursor):
    tables = [
        "Movie", "Person", "Staff_Movie", 
        "Country", "Movie_Country", "Language", "Movie_Language"
    ]
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        for table in tables:
            cursor.execute(f"TRUNCATE TABLE {table};")  # Use DELETE FROM {table}; if you prefer
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        print("Tables emptied successfully.")
    except mysql.connector.Error as err:
        print(f"Error while emptying tables: {err}")

import mysql.connector

def retrieve_table(cursor, table_name):
    try:
        # Execute the SELECT query
        cursor.execute(f"SELECT * FROM {table_name}")
        
        # Fetch all rows
        rows = cursor.fetchall()
        
        # Get column names
        column_names = [desc[0] for desc in cursor.description]
        
        # Print the column names
        print(f"Table: {table_name}")
        print(" | ".join(column_names))
        print("-" * 50)
        
        # Print each row
        for row in rows:
            print(" | ".join(str(value) for value in row))
            
    except mysql.connector.Error as err:
        print(f"Error retrieving table {table_name}: {err}")

if __name__ == "__main__":
    # Connect to the database
    con = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = con.cursor()

    # Retrieve and print a specific table
    retrieve_table(cursor, "Movie")  # Replace "Movie" with your table name

    #

if __name__ == "__main__":
    # Connect to the database

    con = mysql.connector.connect(
        host="localhost",
        user="mohamedj",
        password="moh5969",
    )

    cursor = con.cursor()

    retrieve_table(cursor, "Movie")  # Replace "Movie" with your table name
    # Create tables
    #database_initialization.create_tables(con, cursor)

    #clear tables
    empty_tables(cursor)
    # Insert data into tables
    data_read.insert_data(con, cursor)
    
    # Query the database
    
