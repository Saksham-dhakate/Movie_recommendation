import streamlit as st
import pickle 

data = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    movie_index = data[data["title_x"].str.lower() == movie.lower()].index[0]
    
    movie_similarity = list(
        enumerate(similarity[movie_index])
    )
    movie_similarity = sorted(
        movie_similarity,
        key = lambda x: x[1],
        reverse = True
    )
    recommended = []

    for index, score in movie_similarity[1:6]:
        recommended.append(
            data.iloc[index]["title_x"]
            )
    return recommended

st.title("MOVIE RECOMMENDATION SYSTEM")

selected_movie = st.selectbox(
    "Select a movie",
    data["title_x"].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader(
        f"Movies similar to {selected_movie} are : "
    )
    for movie in recommendations:
        movie_details = data[
            data["title_x"] == movie
            ]

        overview = movie_details.iloc[0]["overview"]
        st.subheader(movie)
        st.write(overview)
        st.write(movie)

