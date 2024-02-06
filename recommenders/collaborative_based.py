"""

    Collaborative-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `collab_model` !!

    You must however change its contents (i.e. add your own collaborative
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline collaborative
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import pandas as pd
import numpy as np
import pickle
import copy
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
movies_df = pd.read_csv('resources/data/movies.csv',sep = ',')
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
model=pickle.load(open('resources/models/SVD.pkl', 'rb'))

def prediction_item(item_id):
    """Map a given favourite movie to users within the
       MovieLens dataset with the same preference.

    Parameters
    ----------
    item_id : int
        A MovieLens Movie ID.

    Returns
    -------
    list
        User IDs of users with similar high ratings for the given movie.

    """
    # Data preprosessing
    reader = Reader(rating_scale=(0, 5))
    load_df = Dataset.load_from_df(ratings_df,reader)
    a_train = load_df.build_full_trainset()

    predictions = []
    for ui in a_train.all_users():
        predictions.append(model.predict(iid=item_id,uid=ui, verbose = False))
    return predictions

def pred_movies(movie_list):
    """Maps the given favourite movies selected within the app to corresponding
    users within the MovieLens dataset.

    Parameters
    ----------
    movie_list : list
        Three favourite movies selected by the app user.

    Returns
    -------
    list
        User-ID's of users with similar high ratings for each movie.

    """
    # Store the id of users
    id_store = set()  # Use a set to ensure unique user IDs
    # For each movie selected by a user of the app,
    # predict corresponding users within the dataset with the highest ratings
    for movie_id in movie_list:
        predictions = prediction_item(item_id=movie_id)
        predictions.sort(key=lambda x: x.est, reverse=True)
        # Take the top 10 user IDs from each movie with highest rankings
        for pred in predictions[:10]:
            id_store.add(pred.uid)
    # Return a list of unique user IDs
    return list(id_store)

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def collab_model(movie_list,top_n=10):
    """Performs Collaborative filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """

    indices = pd.Series(movies_df['title'])
    movie_ids = pred_movies(movie_list)

    print(f'movies {movie_ids}')

    df_init_users = ratings_df[ratings_df['userId']==movie_ids[0]]
    for i in movie_ids :
        #df_init_users=df_init_users.append(ratings_df[ratings_df['userId']==i])
        df_init_users=pd.concat([df_init_users, ratings_df[ratings_df['userId']==i]])

    
    print(f'init users {df_init_users}')

    # Getting the cosine similarity matrix
    cosine_sim = cosine_similarity(np.array(df_init_users), np.array(df_init_users))

    
    print(f'cosine sim {cosine_sim}'))

    idx_1 = indices[indices == movie_list[0]].index[0]
    idx_2 = indices[indices == movie_list[1]].index[0]
    idx_3 = indices[indices == movie_list[2]].index[0]
    # Creating a Series with the similarity scores in descending order

    print("Movie List:", movie_list)
    print("Movies DataFrame Titles:", movies_df['title'])

    if movie_list[0] not in movies_df['title']:
        print(f"{movie_list[0]} not found in movies_df['title']")
    if movie_list[1] not in movies_df['title']:
        print(f"{movie_list[1]} not found in movies_df['title']")
    if movie_list[2] not in movies_df['title']:
        print(f"{movie_list[2]} not found in movies_df['title']")

    print("Index of movie_list[0]:", idx_1)
    print("Index of movie_list[1]:", idx_2)
    print("Index of movie_list[2]:", idx_3)

    print(f'idx 1 {idx_1}')
    print(f'idx 2 {idx_2}')
    print(f'idx 3 {idx_3}')

    rank_1 = cosine_sim[idx_1]
    rank_2 = cosine_sim[idx_2]
    rank_3 = cosine_sim[idx_3]

    print(f'rank 1 {rank_1}')
    print(f'rank 2 {rank_2}')
    print(f'rank 3 {rank_3}')

    # Calculating the scores
    score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
    score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
    score_series_3 = pd.Series(rank_3).sort_values(ascending = False)

    print(f'score 1 {score_series_1}')
    print(f'score 2 {score_series_2}')
    print(f'score 3 {score_series_3}')

     # Appending the names of movies
    #listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)
    listings = pd.concat([score_series_1, score_series_2, score_series_3])

    print(f'listings {listings}')

    recommended_movies = []
    # Choose top 50
    top_50_indexes = list(listings.iloc[1:50].index)

    print(f'top 50 indexes {top_50_indexes}')

    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])

    print(f'top indexes {top_indexes}')

    for i in top_indexes[:top_n]:
        recommended_movies.append(list(movies_df['title'])[i])
    return recommended_movies
