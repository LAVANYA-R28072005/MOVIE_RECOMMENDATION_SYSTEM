import streamlit as st
import pickle
import base64

# Load movie data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found. Please try another title."]
    
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommendations = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommendations

# Function to encode the image in Base64
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    return encoded_img

# Apply background image
def set_background(image_path):
    encoded_img = get_base64_encoded_image(image_path)
    bg_css = f"""
    <style>
        .stApp {{
            background: url("data:image/jpeg;base64,{encoded_img}") no-repeat center center fixed;
            background-size: cover;
        }}
        .movie-title {{
            font-size: 22px;
            font-weight: bold;
            color: white;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }}
        .input-label {{
            font-size: 18px;
            font-weight: bold;
            color: white;
            animation: fadeIn 2s ease-in-out;
        }}
        .stTextInput {{
            font-size: 16px;
            color: black;
            animation: fadeIn 2s ease-in-out;
        }}
        .recommend-btn {{
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 8px 16px;
            border: none;
            animation: fadeIn 2s ease-in-out;
        }}
        .recommend-btn:hover {{
            background-color: #e63946;
        }}
        .profile-photo {{
            border-radius: 40%;
            width: 90px;
            height: 90px;
            margin: 20px auto;
            animation: zoomIn 2s ease-in-out;
        }}
        .recommendations {{
            animation: slideIn 1s ease-out;
        }}

        /* Keyframes for animations */
        @keyframes fadeIn {{
            0% {{
                opacity: 0;
            }}
            100% {{
                opacity: 1;
            }}
        }}
        @keyframes zoomIn {{
            0% {{
                transform: scale(0);
                opacity: 0;
            }}
            100% {{
                transform: scale(1);
                opacity: 1;
            }}
        }}
        @keyframes slideIn {{
            0% {{
                transform: translateY(50px);
                opacity: 0;
            }}
            100% {{
                transform: translateY(0);
                opacity: 1;
            }}
        }}
     </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Set the background image
set_background(r"C:\Users\lavan\Downloads\vantharr data science study materials\PROJECTS\Movie recomendation project\background-1.jpg")

# Display Profile Photo
profile_img_path = r"C:\Users\lavan\Downloads\vantharr data science study materials\PROJECTS\Movie recomendation project\profile- photo.png"  # Provide the path to your profile image
profile_img_base64 = get_base64_encoded_image(profile_img_path)
st.markdown(f'<img src="data:image/png;base64,{profile_img_base64}" class="profile-photo">', unsafe_allow_html=True)

# Display Profile Photo in the sidebar
#st.sidebar.image(profile_img_path, width=200)  # You can set the desired width
sidebar_img_path = r"C:\Users\lavan\Downloads\vantharr data science study materials\PROJECTS\Movie recomendation project\sidebar image.png"
st.sidebar.image(sidebar_img_path, use_container_width=True)


# Add information to the sidebar
st.sidebar.markdown("## About this App")
st.sidebar.write("""
    🎬 This is a Movie Recommendation System that suggests similar movies based on the movie you input. 
    The recommendations are generated using a content-based filtering approach.
""")

# Add developer information
st.sidebar.markdown("## About the Developer")
st.sidebar.write("""
    Developer: Lavanya.R,
    Passionate about building recommendation systems and data science projects.
    Feel free to reach out via email: lavanaya.rk1924@gmail.com
""")

# Add links (for example, GitHub, Portfolio, etc.)
st.sidebar.markdown("## Links")
st.sidebar.write("[GitHub](https://github.com/LAVANYA-R28072005)")
st.sidebar.write("[Portfolio](file:///C:/Users/lavan/OneDrive/Desktop/portfolio%20website/index.html#projects)")

# Streamlit UI
st.markdown("<h1 class='movie-title' style='color: yellow;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

# Input field
st.markdown("<label class='input-label' style='color:yellow; font-weight:bold;'>Enter a movie name:</label>", unsafe_allow_html=True)
movie_name = st.text_input("", key="movie_input", placeholder="Type a movie name here")

# Recommend button
if st.button("Recommend", key="recommend_btn"):
    recommendations = recommend(movie_name)

    st.markdown("<h3 class='recommendations' style='color:yellow;'>Recommended Movies:</h3>", unsafe_allow_html=True)
    for rec in recommendations:
        st.markdown(f"<li style='color:white;'>✅ {rec}</li>", unsafe_allow_html=True)