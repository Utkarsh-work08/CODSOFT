import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie data
data = {
    'movieId': [1, 2, 3, 4, 5],
    'title': ['Toy Story', 'Jumanji', 'Grumpier Old Men', 'Waiting to Exhale', 'Father of the Bride Part II'],
    'genres': ['Adventure|Animation|Children|Comedy|Fantasy',
               'Adventure|Children|Fantasy',
               'Comedy|Romance',
               'Comedy|Drama|Romance',
               'Comedy']
}

df = pd.DataFrame(data)
df['genres'] = df['genres'].str.replace('|', ' ', regex=False)

# TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genres'])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Mapping of movie titles to indices
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# Recommendation function
def recommend(title, num_recommendations=3):
    if title not in indices:
        return "Movie not found."
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Test
if __name__ == "__main__":
    print("Recommendations for 'Toy Story':")
    print(recommend('Toy Story'))
