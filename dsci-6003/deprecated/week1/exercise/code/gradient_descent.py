import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from linear_regression_functions import compute_cost, compute_r2

class GradientDescent(object):

    def __init__(self, model):
        '''
        INPUT: GradientDescent
        OUTPUT: None
        Initialize class variables.
        '''
        self.model = model

    def cost(self, X, y):
        '''
        INPUT: Gradient Descent, 2 dimensional numpy array, numpy array
        OUTPUT: float
        Compute the cost function evaluated using coeffs instance variable.
        '''
        pass

    def score(self, X, y):
        '''
        INPUT: 2 dimensional numpy array, numpy array
        OUTPUT: float
        Compute the R^2 value using coeffs instance variable.
        '''
        pass

    def gradient(self, X, y):
        '''
        INPUT: GradientDescent, 2 dimensional numpy array, numpy array
        OUTPUT: numpy array
        Compute the gradient of the cost function evaluated using coeffs
        instance variable.
        '''
        pass

    def run(self, X, y, alpha=0.01, num_iterations=10000):
        '''
        INPUT: GradientDescent, 2 dimensional numpy array, numpy array
               float, int
        OUTPUT: None
        Run the gradient descent algorithm for num_iterations repititions. Use
        the gradient method and the learning rate alpha to update the
        coefficients at each iteration.
        '''
        pass

    def predict(self, X):
        '''
        INPUT: GradientDescent, 2 dimesional numpy array
        OUTPUT: numpy array
        Use coeffs instance variable to compute the prediction for X.
        '''
        pass