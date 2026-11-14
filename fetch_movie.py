# Importing libraries

import requests
import time
import psycopg2

# Acessing Using API

tocken_tmdb = "tmdb_token(not included)"
Db_password = "password(not included)"

headers = {
    "Authorization" : f"Bearer {tocken_tmdb}",
    "accept" : "application/json"
}

#Connecting The Cursor and forming the connection

conn = psycopg2.connect(
    dbname = "movies_db",
    user = "postgres",
    password = Db_password,
    host = "localhost",
    port = "5432"
)

cursor = conn.cursor()

# Inserting the Structure of the Data

insert_data = """
INSERT INTO movies (
    id, title, overview, release_date, genres, runtime, cast_member,
    director, keywords, rating, vote_count, popularity, poster
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (id) DO NOTHING;
"""

#Creating Session

count = 0

with requests.Session() as session:
    session.headers.update(headers)

    #Preparing The Data

    for page in range(1,50):
        url = "https://api.themoviedb.org/3/discover/movie"

        try:
            res = session.get(url, params={"page" : page}, timeout=30)
            movies = res.json().get("results", [])
        except requests.RequestException as e:
            print(f"failed to the input the data {page} : e")
            continue

        #Inserting The Data

        for movie in movies:
            movie_id = movie.get("id")
            url = f"https://api.themoviedb.org/3/movie/{movie_id}"

            try:
                detail = session.get(
                    url,
                    params={"append_to_response" : "credits,keywords"},
                    timeout=30
                )
                detail.raise_for_status()
                details = detail.json()
            except requests.RequestException as e:
                print(f"Skipping movie {movie_id} due to error : {e}")
                continue

            #Extracting The Lists

            credits = details.get("credits", {})
            keywords = details.get("keywords", {})

            director = [
                person["name"]
                for person in credits.get("crew",[])
                if person.get("job") == "Director"
            ]

            cast = [
                person["name"]
                for person in credits.get("cast",[])[:10]
            ]

            genres = [
                genre["name"]
                for genre in details.get("genres",[])
            ]

            keywords = [
                kw["name"]
                for kw in keywords.get("keywords",[])
            ]

            #Forming The Table

            movie_data = (
                movie_id,
                details.get("title"),
                details.get("overview"),
                details.get("release_date"),
                genres,
                details.get("runtime"),
                cast,
                director,
                keywords,
                details.get("vote_average"),
                details.get("vote_count"),
                details.get("popularity"),
                details.get("poster_path")
            )

            # Closing The Process

            cursor.execute(insert_data, movie_data)
            count += 1
            print(f"Movies Saved : {details.get('title')}")

            time.sleep(0.05)

            conn.commit()
            print(f"Pages Saved : {page}")

cursor.close()
conn.close()
print("Successfully Stored The Data")
