import numpy as np
from gradient_descent_solution import GradientDescent

__author__ = "Jared Thompson"

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

        self.alpha = None
        self.gamma = None
        self.coeffs = None
        self.num_iterations = 0
        self.fit_intercept = fit_intercept
        self.scale = scale
        self.normalize = False
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
        (m, n) = (float(x) for x in X.shape)
        (self.alpha, self.gamma) = (alpha, gamma)
        self.num_iterations += num_iterations
        self.coeffs = np.random.randn(n)
        gradient = GradientDescent(self.fit_intercept, self.normalize, self.gradient)
        gradient.run(X, y, self.coeffs, self.alpha, num_iterations)
        self.coeffs = gradient.coeffs

    def predict(self, X):
        '''
        INPUT: 2 dimensional numpy array, numpy array
        OUTPUT: numpy array

        Calculate the predicted values (0 or 1) for the given data with
        the given coefficients.
        '''
        return np.around(self.hypothesis(X, self.coeffs)).astype(bool)

    def hypothesis(self, X, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array
        OUTPUT: numpy array

        Calculate the predicted percentages (floats between 0 and 1)
        for the given data with the given coefficients.
        '''
        return 1. / (1. + np.exp(-X.dot(coeffs)))

    def cost_function(self, X, y, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: float

        Calculate the value of the cost function for the data with the
        given coefficients.
        '''
        h = self.hypothesis(X, coeffs)
        (m, n) = (float(x) for x in X.shape)
        return (1./m) * (y.dot(h) + (1 - y).dot(1 - h))

    def cost_lasso(self, X, y, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: float

        Calculate the value of the cost function with lasso regularization
        for the data with the given coefficients.
        '''
        h = self.hypothesis(X, coeffs)
        (m, n) = (float(x) for x in X.shape)
        return (1./m) * (y.dot(h) + (1 - y).dot(1 - h) + self.gamma * np.sum([np.abs(c) for c in coeffs]))

    def cost_ridge(self, X, y, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: float

        Calculate the value of the cost function with ridge regularization
        for the data with the given coefficients.
        '''
        h = self.hypothesis(X, coeffs)
        (m, n) = (float(x) for x in X.shape)
        return (1./m) * (y.dot(h) + (1 - y).dot(1 - h) + self.gamma * coeffs.dot(coeffs.T) / 2)

    def cost_gradient(self, X, y, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: numpy array

        Calculate the gradient of the cost function at the given value
        for the coeffs.

        Return an array of the same size as the coeffs array.
        '''
        h = self.hypothesis(X, coeffs)
        return X.T.dot(y - h)

    def cost_gradient_lasso(self, X, y, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: numpy array

        Calculate the gradient of the cost function with regularization
        at the given value for the coeffs.

        Return an array of the same size as the coeffs array.
        '''
        (m, n) = (float(x) for x in X.shape)
        h = self.hypothesis(X, coeffs)
        weights = [c/np.abs(c) for c in coeffs[1:]]
        weights = np.insert(weights, 0, 0)
        return X.T.dot(y - h) + self.gamma * weights / n

    def cost_gradient_ridge(self, X, y, coeffs):
        '''
        INPUT: 2 dimensional numpy array, numpy array, numpy array
        OUTPUT: numpy array

        Calculate the gradient of the cost function with regularization
        at the given value for the coeffs.

        Return an array of the same size as the coeffs array.
        '''
        (m, n) = (float(x) for x in X.shape)
        h = self.hypothesis(X, coeffs)
        weights = coeffs[1:]
        weights = np.insert(weights, 0, 0)
        return X.T.dot(y - h) + self.gamma * weights / n