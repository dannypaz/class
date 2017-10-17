import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity


def get_ratings_data():
    ratings_contents = pd.read_table("data/u.data",
                                     names=["user", "movie", "rating",
                                            "timestamp"])
    highest_user_id = ratings_contents.user.max()
    highest_movie_id = ratings_contents.movie.max()
    ratings_as_mat = sparse.lil_matrix((highest_user_id, highest_movie_id))
    for _, row in ratings_contents.iterrows():
        # subtract 1 from id's due to match 0 indexing
        ratings_as_mat[row.user - 1, row.movie - 1] = row.rating
    return ratings_contents, ratings_as_mat


def make_cos_sim_and_neighborhoods(ratings_mat, neighborhood_size):
    items_cos_sim = cosine_similarity(ratings_mat.T)
    least_to_most_sim_indexes = np.argsort(items_cos_sim, 1)
    neighborhood = least_to_most_sim_indexes[:, -neighborhood_size:]
    return items_cos_sim, neighborhood


def pred_one_user(items_cos_sim, neighborhoods, ratings_mat, user_id):
    n_items = ratings_mat.shape[1]
    items_rated_by_this_user = ratings_mat[user_id].nonzero()[1]
    # Just initializing so we have somewhere to put rating preds
    output = np.zeros(n_items)
    for item_to_rate in range(n_items):
        relevant_items = np.intersect1d(neighborhoods[item_to_rate],
                                        items_rated_by_this_user,
                                        assume_unique=True)
                                    # assume_unique speeds up intersection op
        output[item_to_rate] = ratings_mat[user_id, relevant_items] * \
            items_cos_sim[item_to_rate, relevant_items] / \
            items_cos_sim[item_to_rate, relevant_items].sum()
    return output


if __name__ == '__main__':
    ratings_data_contents, ratings_mat = get_ratings_data()
    cos_sim, nbrhoods = make_cos_sim_and_neighborhoods(ratings_mat,
                                                       neighborhood_size=75)
    user_1_preds = pred_one_user(cos_sim, nbrhoods, ratings_mat, user_id=1)
    # Show predicted ratings for user #1
    print user_1_preds
