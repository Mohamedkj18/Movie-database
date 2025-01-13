import mysql.connector
import pandas as pd
import json

def insert_data(con, cursor):
    file_path = "IMDB_Movies_Dataset.csv"
    df = pd.read_csv(file_path)
    print("here")
    movie_title = df['Title'].tolist()
    average_rating = df['Average Rating'].tolist()
    directors = df['Director'].tolist()
    writers = df['Writer'].tolist()
    meta_score = df['Metascore'].tolist()
    cast = df['Cast'].tolist()
    release_date = df['Release Date'].tolist()
    country = df['Country of Origin'].tolist()
    languages = df['Languages'].tolist()
    budget = df['Budget'].tolist()
    revenue = df['Worldwide Gross'].tolist()
    runtime = df['Runtime'].tolist()

    # Insert data into the Movie table
    for i in range(len(movie_title)):
        try:
            cursor.execute(
                """
                INSERT INTO Movie (title, average_rating, release_date, budget, revenue, runtime, meta_score)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (movie_title[i], average_rating[i], release_date[i], budget[i], revenue[i], runtime[i], meta_score[i])
            )
        except mysql.connector.Error as err:
            print(f"Error inserting into Movie: {err}")

    # Insert data into Person table (Actors, Writers, Directors)
    all_persons = set([d for director in directors for d in director.split(", ")] + [w for writer in writers for w in writer.split(", ")] + [actor for actors in cast for actor in actors.split(", ")])
    for person in all_persons:
        try:
            cursor.execute(
                """
                INSERT IGNORE INTO Person (name)
                VALUES (%s)
                """,
                (person,)
            )
        except mysql.connector.Error as err:
            print(f"Error inserting into Person: {err}")

    # Insert data into Staff_Movie table
    for i in range(len(movie_title)):
        # Insert actors
        for actor in cast[i].split(", "):
            try:
                cursor.execute(
                    """
                    INSERT INTO Staff_Movie (person_name, movie_title, role)
                    VALUES (%s, %s, %s)
                    """,
                    (actor, movie_title[i], 'actor')
                )
            except mysql.connector.Error as err:
                print(f"Error inserting actor into Staff_Movie: {err}")

        # Insert directors
        for dir_name in directors[i].split(", "):
            try:
                cursor.execute(
                    """
                    INSERT INTO Actor_Movie (person_name, movie_title, role)
                    VALUES (%s, %s, %s)
                    """,
                    (dir_name, movie_title[i], 'director')
                )
            except mysql.connector.Error as err:
                print(f"Error inserting director into Staff_Movie: {err}")

        # Insert writers
        for writer_name in writers[i].split(", "):
            try:
                cursor.execute(
                    """
                    INSERT INTO Actor_Movie (person_name, movie_title, role)
                    VALUES (%s, %s, %s)
                    """,
                    (writer_name, movie_title[i], 'writer')
                )
            except mysql.connector.Error as err:
                print(f"Error inserting writer into Staff_Movie: {err}")

    # Insert data into Country and Movie_Country tables
    for i in range(len(movie_title)):
        for country_name in country[i].split(", "):
            try:
                cursor.execute(
                    """
                    INSERT IGNORE INTO Country (country_name)
                    VALUES (%s)
                    """,
                    (country_name,)
                )
                cursor.execute(
                    """
                    INSERT INTO Movie_Country (movie_title, country_name)
                    VALUES (%s, %s)
                    """,
                    (movie_title[i], country_name)
                )
            except mysql.connector.Error as err:
                print(f"Error inserting country or Movie_Country: {err}")

    # Insert data into Language and Movie_Language tables
    for i in range(len(movie_title)):
        for language_name in languages[i].split(", "):
            try:
                cursor.execute(
                    """
                    INSERT IGNORE INTO Language (language_name)
                    VALUES (%s)
                    """,
                    (language_name,)
                )
                cursor.execute(
                    """
                    INSERT INTO Movie_Language (movie_title, language_name)
                    VALUES (%s, %s)
                    """,
                    (movie_title[i], language_name)
                )
            except mysql.connector.Error as err:
                print(f"Error inserting language or Movie_Language: {err}")

    # Commit changes
    con.commit()
    print("Data inserted successfully!")

