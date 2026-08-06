FEATURES-
Searchable Movie Selection
Case Insensitive
Top 5 Similar Movie
4803 Movies Data Set

TECHNOLOGY USED-
pandas
numpy
sckit-learn
python
CountVectorizer
Cosine Similarity
Pickle 
Streamlit

DATASET
- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

WORKING PROCESS
1. Merge the movies and credits datasets.
2. Select important features:
   - Genres
   - Keywords
   - Cast
   - Crew
   - Overview
3. Combine these features into a single text column ('tags').
4. Convert the text into numerical vectors using CountVectorizer.
5. Compute cosine similarity between every pair of movies.
6. Recommend the five most similar movies to the selected movie.

PROJECT STRUCTURE
Movie_recommendation-
├── app.py
├── movie_recommendation_system.ipynb
├── movies.pkl
├── requirements.txt
├── README.md
└── similarity.pkl

The file 'similarity.pkl' is not included in this repository because it exceeds GitHub's file size limit. Generate it locally by running the Jupyter notebook before starting the Streamlit application.

AUTHOR - 
SAKSHAM DHAKATE

github - https://github.com/Saksham-dhakate
