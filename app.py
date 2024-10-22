import pandas as pd
import streamlit as st
import pickle
import os

def recommend_manga(manga_name):
    manga_index = st.session_state.manga[st.session_state.manga['title'] == manga_name].index[0]
    distances = st.session_state.manga_similarity[manga_index] #array
    manga_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x:x[1])[1:46] #gives manga index along with distance
    recommendations = []
    recommendations_rating = []
    for i in manga_list:
        recommendations.append(st.session_state.manga.iloc[i[0]]['title'])
        recommendations_rating.append(st.session_state.manga.iloc[i[0]]['rating'])
    return recommendations, recommendations_rating

def recommend_anime(anime_name):
    anime_index = st.session_state.anime[st.session_state.anime['Name'] == anime_name].index[0]
    distances = st.session_state.anime_similarity[anime_index] #array
    anime_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x:x[1])[1:46] #gives anime index along with distance

    recommendations = []
    recommendations_rating = []
    
    for i in anime_list:
        recommendations.append(st.session_state.anime.iloc[i[0]]['Name'])
        recommendations_rating.append(st.session_state.anime.iloc[i[0]]['Rating'])
        
    return recommendations, recommendations_rating       

if os.path.exists("manga_similarity.pkl"):
    found = "found"
else:
    import pkl_file_creator
    print("pkl files created successfully")
 
 

if 'manga' not in st.session_state:
    manga_dict = pickle.load(open('manga_dict.pkl', 'rb'))
    st.session_state.manga = pd.DataFrame(manga_dict)
    print("manga_dict.pkl is loaded")

if 'manga_similarity' not in st.session_state:
    st.session_state.manga_similarity = pickle.load(open('manga_similarity.pkl', 'rb'),)
    print("manga_similarity is loaded")
    
if 'anime' not in st.session_state:
    anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
    st.session_state.anime = pd.DataFrame(anime_dict)
    print("anime_dict is loaded")
    
if 'anime_similarity' not in st.session_state:
    st.session_state.anime_similarity = pickle.load(open('anime_similarity.pkl', 'rb'))
    print("anime_similarity is loaded")



def main_container(recommendations, rating, count):
    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    for col in row1 + row2+ row3:
        tile = col.container(height=240)
        tile.text(count)
        tile.link_button(recommendations[count-1], f"https://www.google.com/search?q={recommendations[count-1].replace(' ', '+')}")
        tile.write(":blue[Rating :]")
        tile.text(rating[count-1])
        count+=1   
    
on = st.toggle("Manga")


if on:
    st.title('Manga Recommender System')
    
    selected_manga = st.selectbox(
        'Enter manga name',
        st.session_state.manga['title'].values,
        placeholder="manga name",
        index = None
    )
    if st.button('Recommend'):
        st.write("\n")
        st.write("\n")
        st.write("\n")

        if selected_manga is None:
            st.title(":red[Please select an manga!]")
        else:
            recommendations, rating = recommend_manga(selected_manga)
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["            1            ", "            2            ", "            3            ", "            4            ", "            5            "])
            with tab1:
                main_container(recommendations, rating, 1)  
            with tab2:
                main_container(recommendations, rating, 10)
            with tab3:
                main_container(recommendations, rating, 19)
            with tab4:
                main_container(recommendations, rating, 28)
            with tab5:
                main_container(recommendations, rating, 37)

 
                        
else:
    st.title('Anime Recommender System')

    selected_anime = st.selectbox(          
        'Enter anime name',
        st.session_state.anime['Name'].values,
        placeholder="Anime name",
        index = None
    )


    if st.button('Recommend'):
        st.write("\n")
        st.write("\n")
        st.write("\n")

        if selected_anime is None:
            st.title(":red[Please select an anime!]")
        else:
            recommendations, rating = recommend_anime(selected_anime)
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["            1            ", "            2            ", "            3            ", "            4            ", "            5            "])
            with tab1:
                main_container(recommendations, rating, 1)  
            with tab2:
                main_container(recommendations, rating, 10)
            with tab3:
                main_container(recommendations, rating, 19)
            with tab4:
                main_container(recommendations, rating, 28)
            with tab5:
                main_container(recommendations, rating, 37)

                
