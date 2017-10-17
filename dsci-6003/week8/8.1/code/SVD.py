import math
import numpy as np
import pandas as pd
from scipy import sparse

class MatrixFactorizationRecommender():
    """Basic framework for a matrix factorization class.

    You may find it useful to write some additional internal  methods for purposes
    of code cleanliness etc.
    """
    
    def __init__(self):
        """Init should set all of the parameters of the model
        so that they can be used in other methods.
        """

    def fit(self):
        """Like the scikit learn fit methods, this method 
        should take the ratings data as an input and should
        compute and store the matrix factorization. It should assign
        some class variables like n_users, which depend on the
        ratings_mat data.

        It can return nothing
        """
        pass
    
    def pred_one_user(self):
        """Returns the predicted rating for a single
        user.
        """
        pass
    
    def pred_all_users(self):
        """Returns the predicted rating for all users/items.
        """
        pass

    def top_n_recs(self):
        """Returns the top n recs for a given user.
        """
        pass
