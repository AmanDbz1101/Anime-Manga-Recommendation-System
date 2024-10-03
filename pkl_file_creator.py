import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    
    return " ".join(y)

ps = PorterStemmer()
cv = CountVectorizer(max_features= 5000, stop_words='english')

#For anime
print("Creating anime_dict and anime_similarity...")

anime = pd.read_csv('Cleaned_Anime.csv')
pickle.dump(anime.to_dict(), open('anime_dict.pkl', 'wb')) #first pkl file

vectors = cv.fit_transform(anime['Tags']).toarray()

anime['Tags'] = anime['Tags'].apply(stem)

similarity = cosine_similarity(vectors)

pickle.dump(similarity, open('anime_similarity.pkl', 'wb'))#second pkl file creator

#For manga
print("creating manga_dict and manga_similarity...")

manga = pd.read_csv('Cleaned_Manga.csv')
pickle.dump(manga.to_dict(), open('manga_dict.pkl', 'wb')) #first pkl file

vectors = cv.fit_transform(manga['tags']).toarray()

manga['tags'] = manga['tags'].apply(stem)

similarity = cosine_similarity(vectors)

pickle.dump(similarity, open('manga_similarity.pkl', 'wb'))#second pkl file creator
