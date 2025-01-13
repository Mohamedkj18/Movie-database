"""
username: mohamedj
database_name: mohamedj
password: moh5969
"""

import mysql.connector
from mysql.connector import errorcode

def create_tables(con, cursor):
    tables = {}

    # Define tables 
    tables['Movie'] = (
        "CREATE TABLE `Movie` ("
        " `title` VARCHAR(255) NOT NULL,"
        " `average_rating` FLOAT,"
        " `release_date` DATE,"
        " `budget` INT,"
        " `revenue` BIGINT,"
        " `runtime` FLOAT,"
        " `meta_score` INT,"
        " PRIMARY KEY (`title`)"
        ")"
    )

    tables['Person'] = (
        "CREATE TABLE `Person` ("
        " `name` VARCHAR(255) NOT NULL,"
        " PRIMARY KEY (`name`)"
        ")"
    )

    tables['Staff_Movie'] = (
        "CREATE TABLE `Staff_Movie` ("
        " `person_name` VARCHAR(255) NOT NULL,"
        " `movie_title` VARCHAR(255) NOT NULL,"
        " `role` ENUM('actor', 'writer', 'director'),"
        " FOREIGN KEY (`person_name`) REFERENCES `Person`(`name`),"
        " FOREIGN KEY (`movie_title`) REFERENCES `Movie`(`title`)"
        ")"
    )

    tables['Country'] = (
        "CREATE TABLE `Country` ("
        " `country_name` VARCHAR(255) NOT NULL,"
        " PRIMARY KEY (`country_name`)"
        ")"
    )

    tables['Movie_Country'] = (
        "CREATE TABLE `Movie_Country` ("
        " `movie_title` VARCHAR(255) NOT NULL,"
        " `country_name` VARCHAR(255) NOT NULL,"
        " FOREIGN KEY (`movie_title`) REFERENCES `Movie`(`title`),"
        " FOREIGN KEY (`country_name`) REFERENCES `Country`(`country_name`)"
        ")"
    )

    tables['Language'] = (
        "CREATE TABLE `Language` ("
        " `language_name` VARCHAR(255) NOT NULL,"
        " PRIMARY KEY (`language_name`)"
        ")"
    )

    tables['Movie_Language'] = (
        "CREATE TABLE `Movie_Language` ("
        " `movie_title` VARCHAR(255) NOT NULL,"
        " `language_name` VARCHAR(255) NOT NULL,"
        " FOREIGN KEY (`movie_title`) REFERENCES `Movie`(`title`),"
        " FOREIGN KEY (`language_name`) REFERENCES `Language`(`language_name`)"
        ")"
    )

    # Execute the table creation queries
    for table_name, table_description in tables.items():
        try:
            print(f"Creating table {table_name}: ", end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(f"Error: {err.msg}")
        else:
            print("OK")

    # Commit changes to the database
    con.commit()
