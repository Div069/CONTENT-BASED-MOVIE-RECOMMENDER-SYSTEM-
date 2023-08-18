#author:div

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):

      response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=446f92e119b4273c6fcffb2ed06bba04'.format(movie_id))
      data = response.json()
      return "https://image.tmdb.org/t/p/original" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommend_movies=[]
    recommended_movies_posters=[]
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')
selected_movie_name = st.selectbox(
    'Enter the title',
    movies['title'].values)

if st.button('RECOMMEND'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

st.text('Author-Diyansh Gupta')




