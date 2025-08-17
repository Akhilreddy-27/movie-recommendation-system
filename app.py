import streamlit as st
import pickle
import pandas as pd
import requests

# -------------------- Page Config --------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# -------------------- Custom CSS --------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #141e30, #243b55);
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #141e30, #243b55);
    }

    .hero-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: -10px;
        background: linear-gradient(90deg, #ff512f, #dd2476);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-tagline {
        text-align: center;
        font-size: 18px;
        font-weight: 400;
        color: #ddd;
        margin-bottom: 30px;
    }

    .movie-card {
        padding: 15px;
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        text-align: center;
        transition: all 0.4s ease-in-out;
        box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    }
    .movie-card:hover {
        background: rgba(255,255,255,0.18);
        transform: scale(1.07);
        box-shadow: 0 12px 28px rgba(0,0,0,0.75);
    }
    .movie-poster {
        border-radius: 12px;
        transition: transform 0.3s ease;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.6);
    }
    .movie-poster:hover {
        transform: scale(1.05);
    }
    .movie-title {
        font-size: 16px;
        font-weight: 600;
        margin-top: 6px;
        color: #fff;
    }
    .movie-info {
        font-size: 13px;
        color: #ccc;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #ff512f, #dd2476);
        color: white;
        font-size: 16px;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 4px 15px rgba(255, 87, 87, 0.6);
    }
    </style>
""", unsafe_allow_html=True)


# -------------------- TMDB Fetch --------------------
API_KEY = st.secrets["TMDB_API_KEY"]

def fetch_movie_details(movie_title):
    """Fetch poster, year, rating from TMDB"""
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get('results'):
            movie = data['results'][0]
            poster_path = movie.get('poster_path')
            poster_url = (
                "https://image.tmdb.org/t/p/w500" + poster_path if poster_path else
                "https://via.placeholder.com/200x300.png?text=" + movie_title.replace(" ", "+")
            )
            release_date = movie.get('release_date', 'N/A')
            year = release_date.split("-")[0] if release_date else "N/A"
            rating = movie.get('vote_average', 'N/A')
            return poster_url, year, rating
    except Exception as e:
        print("⚠️ Error fetching from TMDB:", e)

    return (
        "https://via.placeholder.com/200x300.png?text=" + movie_title.replace(" ", "+"),
        "N/A",
        "N/A"
    )


# -------------------- Recommend --------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies, posters, years, ratings = [], [], [], []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        poster, year, rating = fetch_movie_details(movie_title)
        recommended_movies.append(movie_title)
        posters.append(poster)
        years.append(year)
        ratings.append(rating)

    return recommended_movies, posters, years, ratings


# -------------------- Load Data --------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


# -------------------- UI --------------------
st.markdown("<h1 class='hero-title'>🍿 Movie Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-tagline'>Find your next favorite movie with AI-powered suggestions 🎬</p>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    '🎥 Choose a movie:',
    movies['title'].values
)

if st.button('🚀 Recommend'):
    recommendations, posters, years, ratings = recommend(selected_movie_name)

    st.markdown("## ✨ Recommended For You")
    cols = st.columns(5, gap="large")
    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"""
                <div class="movie-card">
                    <img src="{posters[idx]}" class="movie-poster" width="100%">
                    <div class="movie-title">{recommendations[idx]}</div>
                    <div class="movie-info">📅 {years[idx]} | ⭐ {ratings[idx]}</div>
                </div>
            """, unsafe_allow_html=True)
