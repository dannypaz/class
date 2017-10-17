import numpy as np
from gradient_descent import GradientDescent
from math import e

__author__ = "Jonathan Hilgart"

class LogisticRegression(object):

    def __init__(self, fit_intercept = True, scale = True, norm = "L2"):
        '''
        INPUT: GradientDescent, function, function, function
        OUTPUT: None

        Initialize class variables. Takes three functions:
        cost: the cost function to be minimized
        gradient: function to calculate the gradient of the cost function
        predict: function to calculate the predicted values (0 or 1) for
        the given data
        '''



        gradient_choices = {None: self.cost_gradient, "L1": self.cost_gradient_lasso, "L2": self.cost_gradient_ridge}


        # * You'll need to initialize alpha, gama, and the weights (coefficients for the regression)
        self.coeffs = None
        self.alpha = None
        self.gamma = None

        # * You'll also need to store the number of iterations

        

        # * You'll also need to store a boolean value for whether or
        # * not you fit the intercept and scale

        # I give these lines to you
        if norm:
            self.norm = norm
            self.normalize = True
        self.gradient = gradient_choices[norm]

    def fit(self,  X, y, alpha=0.01, num_iterations=10000, gamma=0.):
        '''
        INPUT: 2 dimensional numpy array, numpy array, float, int, float
        OUTPUT: numpy array

        Main routine to train the model coefficients to the data
        the given coefficients.
        '''

        # * You'll need to store the dimensions of the input here

        # * You'll also need to store the inputs for
        # * alpha (the lagrange multiplier) and gamma

        # * you'll need to update the stored value of num_iterations

        # * randomly initialize the regression weights

        # * Create an instance of GradientDescent

        # * Run gradient descent

        # * store the coefficients obtained from the gradient descent




    def predict(self, X):
        '''
        INPUT: 2 dimensional numpy array, numpy array
        OUTPUT: numpy array

        Calculate the predicted values (0 or 1) for the given data with
        the given coefficients.
        '''

        # * The hypothesis function wil predict probabilities (floats between 0 and 1) for each input.

        # * you will need to be able to return a set of values between 0 and 1 for each of these.

        # * return a bool (t/f) value for each percentage, such that percentages above 0.5 are
        # * returned as 1, else 0.
    
        threshold = .5
        bool_t = hypothesis(self, X, self.coeffs)>threshold 
        bool_f = [1 if i == True for i in bool_t]
        return bool_f



    def hypothesis( X, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array
        OUTPUT: numpy array

        Calculate the predicted percentages (floats between 0 and 1)
        for the given data with the given coefficients.
        '''

        # * The hypothesis function is going to return a proposed probability for each of the test data points
        # * this will be done using the logistic function and the coefficients you've derived from the gradient descent


#         for row_index,row in enumerate(X):
        return   float(1/(1+np.exp(-(coeffs[0]+np.dot(X,coeffs[1:].T)))))



    def cost_function(self, X, y, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: float

        Calculate the value of the cost function for the data with the
        given coefficients.
        '''

        # * call the hypothesis function to return a set of probabilities into a single vector h

        # * return the log-likelihood for each of these predictions  1/M sum y_i*h_i + (1-y_i)*(1-h_i)
        # * using the dot product will help


        h = hypothesis(X,coeffs)

        length = len(X)
        log_likelihood = []

        cost = [(-1/len(X))*sum(y*(log(h)) + (1-y)*(1-h))]

        return cost


    def cost_gradient(self, X, y, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: numpy array

        Calculate the gradient of the cost function at the given value
        for the coeffs.

        Return an array of the same size as the coeffs array.
        '''

        # This function is not used in the above code, just kept here for measuring the current state of cost

        # * Calculate the hypothesis function with the input coefficients

        # * Return Sum x_i*(y_i - h_i)
        h = hypothesis(X,coeffs)

        return [(1/len(X)) * sum(((h-y))*(X))]





