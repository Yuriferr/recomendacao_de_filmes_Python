import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD
import numpy as np

ratings = pd.read_csv("./ml-latest-small/ratings.csv")
movies = pd.read_csv("./ml-latest-small/movies.csv")

# Merge dos dataframes de ratings e de filmes
data = pd.merge(ratings, movies, on='movieId')


# Normalização das avaliações
user_ratings_mean = data.groupby(['userId'])['rating'].mean()
data = pd.merge(data, pd.DataFrame(user_ratings_mean), on='userId')
data['rating_norm'] = data['rating_x'] - data['rating_y']

# Criação da matriz esparsa
ratings_mat = csr_matrix((data['rating_norm'], (data['userId'], data['movieId'])))

# Criação do modelo SVD
svd = TruncatedSVD(n_components=10, random_state=42)
svd.fit(ratings_mat)

# Função de recomendação
def recommend_movies(user_id, num_recommendations=10):
    # Obtém as previsões do modelo para o usuário
    user_ratings = ratings_mat[user_id,:]
    user_ratings_pred = svd.predict(user_ratings)

    # Obtém os filmes ainda não avaliados pelo usuário
    user_ratings_mask = user_ratings.toarray().reshape(-1) == 0
    user_unrated_movies = np.where(user_ratings_mask)[0]

    # Obtém os IDs dos filmes recomendados
    movie_ids = np.arange(ratings_mat.shape[1])
    unrated_movie_ids = np.intersect1d(user_unrated_movies, movie_ids)
    movie_preds = [(idx, pred) for idx, pred in zip(unrated_movie_ids, user_ratings_pred[unrated_movie_ids])]
    movie_preds_sorted = sorted(movie_preds, key=lambda x:x[1], reverse=True)
    recommended_movie_ids = [x[0] for x in movie_preds_sorted[:num_recommendations]]

    # Obtém os nomes dos filmes recomendados
    recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)]['title'].tolist()

    return recommended_movies





