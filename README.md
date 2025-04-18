# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System**!  
This app suggests similar movies based on your favorite movie using **content-based filtering** and a user-friendly **Streamlit web interface**.

---

## 📌 Features

- 🔍 Search for a movie and get top 5 similar movie suggestions.
- 💡 Uses NLP and cosine similarity for recommendations.
- 🎨 Custom-designed UI with background image and animations.
- 📷 Developer profile & links in sidebar.

---

## 🧠 How It Works

1. The app uses preprocessed data (`movie_list.pkl`, `similarity.pkl`) created from the [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-dataset).
2. Movie titles and metadata are vectorized using TF-IDF or other NLP techniques.
3. Cosine similarity is computed to find movies most similar to the input.
4. Streamlit provides an interactive front-end for easy use.

---

## 🗂 Dataset Used

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Download from Kaggle: [TMDb Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-dataset)

---

## 🚀 Getting Started
1. Clone the Repository:- git clone https://github.com/yourusername/movie-recommendation-system.git
2. Change the directory, type this command in cmd:- cd movie-recommendation-system
3. After changing the directory, create a virtual env in the project folder and install the required libraries
4. to create the virtual env:- python -m venv venv
5. Activate it using this command:- venv\Scripts\activate
6. After the activation you can install the libraries.

6. After installing all the required libraries and loding the project, Run this code in command prompt(cmd):- streamlit run movie_app.py

### Note:
you need to install the libraries in the virtual env project folder to execute the project, only then you can run it successfully or you will get errors.
