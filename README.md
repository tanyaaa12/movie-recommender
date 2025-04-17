# 🎬 Movie Recommendation System using NLP and Streamlit
Overview
This is a Movie Recommendation System built using Natural Language Processing (NLP) and Streamlit. The system suggests movies based on the user's input movie title by utilizing content-based filtering.

Trained on the TMDB (The Movie Database) dataset, this app fetches similar movie recommendations based on movie genres, keywords, and overviews.

Features
Similar Movie Recommendations: Get a list of movies similar to the selected movie.

Clean User Interface: Built using Streamlit, offering a simple and intuitive user experience.

Poster Display: Movie posters are shown for each recommendation.

Real-Time Recommendations: Dynamically fetches results based on user input.

Tech Stack
Backend:

Python

Pandas (for data manipulation)

Sklearn (for cosine similarity and vectorization)

NLTK (Natural Language Toolkit for text processing)

Frontend:

Streamlit (for building the app UI)

Others:

Requests (for fetching movie posters)

Google Drive (for storing and retrieving large pre-trained files)

How it Works
User Input: Select a movie title from the dropdown list.

Recommendation Engine: Based on the selected movie, the system computes cosine similarity and fetches the top 10 similar movies.

UI Display: The recommendations are shown with their posters and titles for easy browsing.
