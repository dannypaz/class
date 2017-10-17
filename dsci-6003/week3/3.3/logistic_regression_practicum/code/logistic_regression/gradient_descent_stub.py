import numpy as np

__author__ = "Jonathan Hilgart"


class GradientDescent(object):
    def __init__(self, fit_intercept=True, normalize=False, gradient=None, mu=None, sigma=None):
        '''
        INPUT: GradientDescent, boolean
        OUTPUT: None
        Initialize class variables. cost is the function used to compute the
        cost.
        '''

        # * initialize and store None to the local copy of coefficients (weights) and alpha (input in the run function)
        # * store boolean values for fit_intercept and normalize
        # * store local copies of gradient, mu and sigma
        self.coeffs=None
        self.alpha=None
        self.fit_intercept = fit_intercept
        self.normalize = normalize
        self.gradient = gradient
        self.mu = mu
        self.sigma = sigma




    def run(self, X, y, coeffs=None, alpha=0.01, num_iterations=100):


        # * calculate normalization factors
        calculate_normalization_factors(X)
        # * run maybe_modify_matrix here and return the modified matrix

        X= maybe_modify_matrix(X)

        # * update the local copies of coefficents and alpha

        

        # * if there aren't input coefficients, initialize them to zero.
        if coeffs ==None:
            self.coeffs=np.zeros(len(X))
        # * Recall that there should be as many coefficients as features.

        # I give you this line here. if fit_intercept = True, set the intercept to 0
        if self.fit_intercept:
            self.coeffs = np.insert(self.coeffs, 0, 0)

        # * for each of the num_iterations, update self.coeffs at each step.

        for n in range(num_iterations):
            #update b as b - alpha * gradient(J)
            self.coeffs = self.coeffs- alpha*self.gradient(X,self.coeffs)


    def calculate_normalization_factors(self, X):
        '''
        INPUT: GradientDescent, 2 dimensional numpy array
        OUTPUT: None
        Initialize mu and sigma instance variables to be the numpy arrays
        containing the mean and standard deviation for each column of X.
        '''

        # * set the local copy of mu to be the average of each column of X
        self.mu=np.mean(X,axis=0)

        # * set the local copy of sigma to be the standard deviation of each column of X
        self.sigma=np.std(X,axis=0)

        # I give this to you - Don't normalize the intercept column
        self.mu[self.sigma == 0] = 0
        self.sigma[self.sigma == 0] = 1

    def add_intercept(self, X):
        '''
        INPUT: 2 dimensional numpy array
        OUTPUT: 2 dimensional numpy array
        Return a new 2d array with a column of ones added as the first
        column of X.
        '''
        # I give this line to you
        return np.hstack((np.ones((X.shape[0], 1)), X))

    def maybe_modify_matrix(self, X):
        '''
        INPUT: GradientDescent, 2 dimensional numpy array
        OUTPUT: 2 dimensional numpy array
        Depending on the settings, normalizes X and adds a feature for the
        intercept.
        '''
        # I give this line to you

        if self.normalize:
            X = (X - self.mu) / self.sigma

        if self.fit_intercept:
            return self.add_intercept(X)

        return X