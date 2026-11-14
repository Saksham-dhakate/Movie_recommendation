# Importing Libraries
import pandas as pd
import psycopg2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading The dataset
conn = psycopg2.connect(
    dbname="movies_db",
    user="postgres",
    password="Saksham@22",
    host="localhost",
    port="5432"
)

# Creating Queries
query = "SELECT id, title, overview, genres, cast_member, director, keywords, poster FROM movies;"
df = pd.read_sql(query, conn)
conn.close()

# Converting List to String and removing Spaces
def list_to_string(lst):
    if isinstance(lst, list):
        return " ".join([item.replace(" ", "") for item in lst])
    return ""

df["genres_fixed"] = df["genres"].apply(list_to_string)
df["cast_fixed"] = df["cast_member"].apply(list_to_string)
df["director_fixed"] = df["director"].apply(list_to_string)
df["keywords_fixed"] = df["keywords"].apply(list_to_string)
df["overview_fixed"] = df["overview"].fillna("")

# Creating Tags
df["tags"] = (
    df["overview_fixed"] + " " + 
    df["genres_fixed"] + " " + 
    df["cast_fixed"] + " " + 
    df["director_fixed"] + " " +
    df["keywords_fixed"]
)

df["tags"] = df["tags"].str.lower()

# Vectorization & Similarity
tf_idf = TfidfVectorizer(stop_words="english", max_features=5000)
vectors = tf_idf.fit_transform(df["tags"])
similarity = cosine_similarity(vectors)

# Recommendation System
def recommend(movie_name):
    matches = df[df["title"].str.lower() == movie_name.strip().lower()]

    if matches.empty:
        print(f"\nMovie '{movie_name}' not found in database!")
        print("Sample movies you can try:")
        print(df["title"].sample(5).values)
        return

    idx = matches.index[0]

    scores = list(enumerate(similarity[idx]))
    final_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommendations for '{df.iloc[idx]['title']}':\n")
    count = 0
    for i, score in final_scores:
        if i == idx:
            continue
        print(f"{count + 1}. {df.iloc[i]['title']}")
        count += 1
        if count == 5:
            break

if __name__ == "__main__":
    movie = input("Enter a movie name: ")
    recommend(movie)
