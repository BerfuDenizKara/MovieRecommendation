import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Set your OpenAI API key
client = OpenAI()

# Define the 80-year-old movie critic's persona
def get_movie_recommendations(genres, favorite_movies, country):
    # Prompt to ChatGPT with persona
    prompt = f"""
    You are an 80-year-old woman who has been a movie critic for over 50 years. You are very knowledgeable on directors, movies, and artistic films from all countries. 
    Please recommend 5 artistic movies based on the following preferences:
    
    - Genres: {", ".join(genres)}
    - Top 3 favorite movies: {", ".join(favorite_movies)}
    - User's country: {country}
    
    For each recommendation, provide:
    - Movie Name
    - Genre
    - A short summary in your warm, wise tone
    - The platform where the user can watch the movie in their country
    - A YouTube link for the movie's trailer if available.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a wise, 80-year-old movie critic with vast knowledge of cinema."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

# Streamlit UI
st.title("🎥✨ Movie Recommendation System")
st.markdown("Welcome to the Movie Recommendation System! 🌕🌟 This wise, old critic has seen it all and is here to share her wisdom about the finest films. Select your favorite genres and let her guide you to movies that will warm your soul and expand your horizons! 🎬👵")

# Genre selection
genres = st.multiselect(
    "Choose your favorite movie genres (up to 20 options):",
    options=[
        "Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", 
        "Documentary", "Drama", "Fantasy", "Historical", "Horror", "Musical",
        "Mystery", "Romance", "Sci-Fi", "Sport", "Thriller", "War", "Western"
    ]
)

# User inputs for favorite movies and country
st.subheader("Tell me your top 3 favorite movies:")
movie1 = st.text_input("Favorite Movie #1", placeholder="Movie Title")
movie2 = st.text_input("Favorite Movie #2", placeholder="Movie Title")
movie3 = st.text_input("Favorite Movie #3", placeholder="Movie Title")

country = st.text_input("Where are you from?", placeholder="Country")

# Recommendation button
if st.button("Recommend Me Movies"):
    if genres and movie1 and movie2 and movie3 and country:
        # Get recommendations from the ChatGPT API
        recommendations = get_movie_recommendations(genres, [movie1, movie2, movie3], country)
        
        # Display the recommendations
        st.markdown("### 🎞️ Here are some movie recommendations for you!")
        st.markdown(recommendations)
    else:
        st.error("Please fill in all the fields before clicking the button.")
