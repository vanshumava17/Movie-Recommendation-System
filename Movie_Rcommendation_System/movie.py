import pickle
import streamlit as st
import requests

st.title("Movie Recommendation System")
with open("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title_x'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_actors = []
    recommended_movie_genres = []
    recommended_movie_imdb_rating = []
    recommended_movie_year_of_release = []
    for i in distances[0:7]:
        current_movie_name = movie
        # movie_id = movies.iloc[i[0]].imdb_id
        recommended_movie_posters.append(movies.iloc[i[0]].poster_path)
        # recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title_x)
        recommended_movie_actors.append(movies.iloc[i[0]].actors[0:2])
        recommended_movie_genres.append(movies.iloc[i[0]].genres[0:3])
        recommended_movie_imdb_rating.append(movies.iloc[i[0]].imdb_rating)
        recommended_movie_year_of_release.append(movies.iloc[i[0]].year_of_release)

        

        # print(movies.iloc[i[0]].runtime)
        # print(movies.iloc[i[0]].year_of_release)
    return recommended_movie_names,recommended_movie_posters,recommended_movie_actors,recommended_movie_genres, recommended_movie_imdb_rating,current_movie_name,recommended_movie_year_of_release

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title_x'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    # recommendation = recommend(selected_movie)
    # for i in recommendation:
    #     st.write(i)
    recommended_movie_names,recommended_movie_posters,recommended_movie_actors,recommended_movie_genres,recommended_movie_imdb_rating,current_movie_name,recommended_movie_year_of_release = recommend(selected_movie)

    st.markdown(f"<p class=text>{'You Searched Movie'}</p>",unsafe_allow_html=True)
    st.text(current_movie_name)

    st.markdown(f"<p class=text>{'Recommended Movie'}</p>",unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    
    
    
    # with col1:
    #     st.warning(recommended_movie_names[0])
    #     st.image(recommended_movie_posters[0])
    #     st.text(recommended_movie_genres[0])
    #     st.text(recommended_movie_acto
    # rs[0])
    #     st.markdown(f"<p class=rating>{recommended_movie_imdb_rating[0]}</p>",unsafe_allow_html=True)
    #     st.markdown(f"<p class=year_of_release>{recommended_movie_year_of_release[0]}</p>",unsafe_allow_html=True)

    with col1:
        st.warning(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        # st.text(recommended_movie_genres[1])
        st.write("Genres: ",', '.join(recommended_movie_genres[1]))
        st.write("Actors: ",', '.join(recommended_movie_actors[1]))
        st.markdown(f"<p class=rating>{recommended_movie_imdb_rating[1]}</p>",unsafe_allow_html=True)
        st.markdown(f"<p class=year_of_release>{recommended_movie_year_of_release[1]}</p>",unsafe_allow_html=True)

    with col2:
        st.warning(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.write("Genres: ",', '.join(recommended_movie_genres[2]))
        st.write("Actors: ",', '.join(recommended_movie_actors[2]))
        st.markdown(f"<p class=rating>{recommended_movie_imdb_rating[2]}</p>",unsafe_allow_html=True)
        st.markdown(f"<p class=year_of_release>{recommended_movie_year_of_release[2]}</p>",unsafe_allow_html=True)

    with col3:
        st.warning(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.write("Genres: ",', '.join(recommended_movie_genres[3]))
        st.write("Actors: ",', '.join(recommended_movie_actors[3]))
        st.markdown(f"<p class=rating>{recommended_movie_imdb_rating[3]}</p>",unsafe_allow_html=True)
        st.markdown(f"<p class=year_of_release>{recommended_movie_year_of_release[3]}</p>",unsafe_allow_html=True)

    with col4:
        st.warning(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.write("Genres: ",', '.join(recommended_movie_genres[4]))
        st.write("Actors: ",', '.join(recommended_movie_actors[4]))
        st.markdown(f"<p class=rating>{recommended_movie_imdb_rating[4]}</p>",unsafe_allow_html=True)
        st.markdown(f"<p class=year_of_release>{recommended_movie_year_of_release[4]}</p>",unsafe_allow_html=True)

    with col5:
        st.warning(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
        st.write("Genres: ",', '.join(recommended_movie_genres[5]))
        st.write("Actors: ",', '.join(recommended_movie_actors[5]))
        st.markdown(f"<p class=rating>{recommended_movie_imdb_rating[5]}</p>",unsafe_allow_html=True)
        st.markdown(f"<p class=year_of_release>{recommended_movie_year_of_release[5]}</p>",unsafe_allow_html=True)

    with col6:
        st.warning(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
        st.write("Genres: ",', '.join(recommended_movie_genres[6]))
        st.write("Actors: ",', '.join(recommended_movie_actors[6]))
        st.markdown(f"<p class=rating>{recommended_movie_imdb_rating[6]}</p>",unsafe_allow_html=True)
        st.markdown(f"<p class=year_of_release>{recommended_movie_year_of_release[6]}</p>",unsafe_allow_html=True)