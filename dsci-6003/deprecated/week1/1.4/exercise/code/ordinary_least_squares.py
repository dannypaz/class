import numpy as np

class OrdinaryLeastSquares(object):

    def __init__(self):
        # Initialize coefficients in run method once you know how many features
        # you have.
        self.coeffs = None

    def compute_cost(self, X, y):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: float
        Calculate the Sum of Squared Errors for the hypothesis line given by
        coeffs.
        '''
        pass

    def compute_r2(self, X, y):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: float
        Calculate the R^2 value for the hypothesis line given by coeffs.
        '''
        pass

    def hypothesis(self, X):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: numpy array
        Use coeffs instance variable to compute the y_hat prediction for X.
        '''
        pass