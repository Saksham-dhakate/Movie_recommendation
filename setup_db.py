#Importing Libraries

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#Setting Password

Db_password = "password"

# Creating Connection

conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = Db_password,
    host = "localhost",
    port = "5432"
)

#Enable Autocommit

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

#Checking if the database exist
cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'movies_db'")

if not cursor.fetchone():
    cursor.execute("CREATE DATABASE movies_db")
    print("Database 'movies_db' created successfully!")

else:
    print("Database 'movies_db' already exists.")

#Close Connection

cursor.close()
conn.close()

#Connect Directly to movies_db

conn = psycopg2.connect(
    dbname = "movies_db",
    user = "postgres",
    password = Db_password,
    host = "localhost",
    port = "5432"
)

cursor = conn.cursor()

#Structure The Movies Table

create_table_query = """
CREATE TABLE IF NOT EXISTS movies(
    id INT PRIMARY KEY,
    title VARCHAR(255),
    overview TEXT,
    release_date VARCHAR(50),
    genres TEXT[],
    runtime INT,
    cast_member TEXT[],
    director TEXT[],
    keywords TEXT[],
    rating FLOAT,
    vote_count INT,
    popularity FLOAT,
    poster VARCHAR(255)
);
"""

#Execution of the Database

cursor.execute(create_table_query)
conn.commit()

print("Table 'movies' created successfully!")

#Close Connection

cursor.close()
conn.close()
