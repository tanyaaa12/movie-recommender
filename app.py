import streamlit as st #To make frontend / website
import pickle          #To load pre-trained data
import pandas as pd    #For working with movie data (tables)

#Load the pre-trained data
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

#paste recommend function from jupyter nb
#CHANGE THE RECOMMEND FUNCTION FOR app.py?
#1. Because → Streamlit is UI → No Print Statements Allowed!
#In Notebook → print() is fine.

#In app.py → print() shows nothing to the user.

#2. In Streamlit → You Return Stuff → Not Print"""
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



#Adds a beautiful big heading.
st.title('Movie Recommender 🍿 ')

#Create a dropdown with all the movie names, you can select from here

selected_movie = st.selectbox('Select a movie to get recommendations:',
                              movies['title'].values)

#Button to Trigger Recommendation
if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie)
    st.subheader("Here are your Top Picks!")
    for i in recommendations:
        st.write(i)

