import streamlit as st #To make frontend / website
import pickle          #To load pre-trained data
import pandas as pd    #For working with movie data (tables)
import requests # To fetch posters
import os
import gdown

# Download similarity.pkl only if it doesn't already exist
if not os.path.exists('similarity.pkl'):
    url = 'https://drive.google.com/uc?id=1STeY__63rEb38euW1fUPfQ7Of_NmFZmA'
    output = 'similarity.pkl'
    gdown.download(url, output, quiet=False)

# Load the locally uploaded movies.pkl
movies = pickle.load(open('movies.pkl', 'rb'))

# Load the downloaded similarity.pkl
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API Key and Base URL
API_KEY = '849eba4a24b45ce1786271471c56746a'  
BASE_URL = "https://api.themoviedb.org/3"

# Function to fetch poster using TMDB API
def get_poster(movie_title):
    query = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_title}&language=en-US"
    response = requests.get(query)

    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        if results and results[0].get('poster_path'):
            poster_path = results[0]['poster_path']
            full_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_url
        else:
            return None  # No poster_path found
    else:
        return None  # In case of an API error



#  recommendation function to return recommendations
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Streamlit frontend UI
st.image("https://imgur.com/SD93b1P.png", use_container_width=True)
st.title('Movie Recommender 🍿')
st.markdown("#### Feeling lost on what to watch next? Let us help you out! 🎬")

# Dropdown menu to select a movie
selected_movie = st.selectbox('Select a movie to get recommendations:', movies['title'].values)

## Button to trigger recommendations
if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie)
    st.subheader("Here are your Top Picks!")

    # Create 2 columns to display movie posters and titles neatly
    col1, col2 = st.columns(2)

    # Loop through the recommended movies
    for i, movie_title in enumerate(recommendations):
        # Fetch the poster for each movie recommendation
        poster_url = get_poster(movie_title)

        # Assign columns dynamically based on index (Alternating between 2 columns)
        col = [col1, col2][i % 2]

        # Display the poster and movie title in the assigned column
        with col:
            if poster_url:
                st.image(poster_url, use_container_width=True)
            else:
                
                st.image("https://imgur.com/undefined.png", use_container_width=True)

        
            st.markdown(f"### {movie_title}")





