import numpy as np


class GradientDescent(object):

    def __init__(self, cost, gradient, predict):
        '''
        INPUT: GradientDescent, function, function, function
        OUTPUT: None

        Initialize class variables. Takes three functions:
        cost: the cost function to be minimized
        gradient: function to calculate the gradient of the cost function
        predict: function to calculate the predicted values (0 or 1) for 
        the given data
        '''
        # Initialize coefficients in run method once you know how many features
        # you have.
        self.coeffs = None
        self.cost = cost
        self.gradient = gradient
        self.predict = predict

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
        INPUT: GradientDescent, 2 dimensional numpy array
        OUTPUT: numpy array (ints)

        Use the coeffs to compute the prediction for X. Return an array of 0's
        and 1's.
        '''
        pass
