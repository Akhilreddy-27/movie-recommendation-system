🎬 Movie Recommendation System

This is a content-based movie recommendation system built with Python and Streamlit.
It recommends similar movies based on a selected title using machine learning and natural language processing techniques.

🚀 Features

Search and select a movie

Get top 5 similar movies as recommendations

Uses cosine similarity on movie features

Interactive Streamlit web app

Easy to extend with more datasets

🛠️ Tech Stack

Python (pandas, numpy, scikit-learn)

Streamlit (for UI)

Pickle (for saving models/data)

📂 Project Structure
├── app.py               # Main Streamlit app
├── movies.pkl           # Preprocessed movie metadata
├── similarity.pkl       # Precomputed similarity matrix
├── movie_dict.pkl       # Dictionary version of movie dataset
└── README.md            # Project documentation

⚡ Installation & Usage

Clone the repo:

git clone https://github.com/Akhilreddy-27/movie-recommendation-system.git
cd movie-recommendation-system


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Open in browser:

http://localhost:8501

📊 Dataset

Movies metadata and credits dataset from TMDb (The Movie Database).

Preprocessed and stored in movies.pkl.

🔮 Future Improvements

Add collaborative filtering (user-based recommendations)

Integrate real-time TMDb API for movie posters and info

Deploy on Streamlit Cloud / Heroku

📸 Demo
<img width="1919" height="831" alt="Screenshot 2025-08-17 194319" src="https://github.com/user-attachments/assets/2b8cc735-7ca5-43b4-b6a0-8f6060daf724" />
