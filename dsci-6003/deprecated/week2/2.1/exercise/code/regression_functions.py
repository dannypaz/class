import numpy as np

def hypothesis(X, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array
    OUTPUT: numpy array

    Calculate the predicted percentages (floats between 0 and 1) for the given
    data with the given coefficients.
    '''
    pass

def predict(X, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array
    OUTPUT: numpy array

    Calculate the predicted values (0 or 1) for the given data with the given
    coefficients.
    '''
    pass

def log_likelihood(X, y, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array, numpy array
    OUTPUT: float

    Calculate the log likelihood of the data with the given coefficients.
    '''
    pass

def log_likelihood_gradient(X, y, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array, numpy array
    OUTPUT: numpy array

    Calculate the gradient of the log likelihood at the given value for the
    coeffs. Return an array of the same size as the coeffs array.
    '''
    pass

def accuracy(y_true, y_pred):
    '''
    INPUT: numpy array, numpy array
    OUPUT: float

    Calculate the percent of predictions which equal the true values.
    '''
    pass

def precision(y_true, y_pred):
    '''
    INPUT: numpy array, numpy array
    OUTPUT: float

    Calculate the percent of positive predictions which were correct.
    '''
    pass

def recall(y_true, y_pred):
    '''
    INPUT: numpy array, numpy array
    OUTPUT: float

    Calculate the percent of positive cases which were correctly predicted.
    '''
    pass
