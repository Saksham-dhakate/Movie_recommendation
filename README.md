Movie Recommendation System

A Content-Based Movie Recommendation Engine built with Python, PostgreSQL, and Machine Learning (TF-IDF & Cosine Similarity) using live data from the TMDB API.

Features
Automated Database Setup: Programmatic schema initialization in PostgreSQL using psycopg2.
Native SQL Arrays: Stores genres, cast, and keywords using PostgreSQL's TEXT[] array type.
Data Ingestion Pipeline: Fetches movie metadata from TMDB API with duplicate prevention (ON CONFLICT (id) DO NOTHING).
Content-Based ML Engine: Combines plot, genres, cast, director, and keywords into a feature soup, then ranks similar movies using TF-IDF and Cosine Similarity.

Tech Stack
Language: Python
Database: PostgreSQL
Libraries: Pandas, Scikit-learn, Psycopg2, Requests

File Structure
setup_db.py: Creates the movies_db database and movies table.
fetch_movie.py: Extracts movie data from TMDB API and inserts it into PostgreSQL.
reccommend.py: Computes TF-IDF vectorization and outputs top 5 movie recommendations.

Quick Start
1. Install Dependencies
bash
pip install psycopg2-binary pandas scikit-learn requests
2. Setup Database

Update your PostgreSQL password in setup_db.py, then run:

bash
python setup_db.py
3. Fetch Movies

Populate the database with movies from TMDB:

bash
python fetch_movie.py
4. Run Recommendations
bash
python reccommend.py
Example
text
Enter a movie name: Resident Evil
Recommendations for 'Resident Evil':
1. 28 Days Later
2. 28 Years Later
3. Weapons
4. Beware Boiúna
5. Train to Busan
