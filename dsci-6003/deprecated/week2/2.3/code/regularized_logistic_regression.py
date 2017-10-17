import numpy as np

def hypothesis(X, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array
    OUTPUT: numpy array

    Calculate the predicted percentages (floats between 0 and 1) 
    for the given data with the given coefficients.
    '''
    pass

def predict(X, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array
    OUTPUT: numpy array

    Calculate the predicted values (0 or 1) for the given data with 
    the given coefficients.
    '''
    pass

def cost_function(X, y, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array, numpy array
    OUTPUT: float

    Calculate the value of the cost function for the data with the 
    given coefficients.
    '''
    pass

def cost_regularized(X, y, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array, numpy array
    OUTPUT: float

    Calculate the value of the cost function with regularization 
    for the data with the given coefficients.
    '''
    pass

def cost_gradient(X, y, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array, numpy array
    OUTPUT: numpy array

    Calculate the gradient of the cost function at the given value 
    for the coeffs. 

    Return an array of the same size as the coeffs array.
    '''
    pass

def gradient_regularized(X, y, coeffs):
    '''
    INPUT: 2 dimensional numpy array, numpy array, numpy array
    OUTPUT: numpy array

    Calculate the gradient of the cost function with regularization 
    at the given value for the coeffs. 

    Return an array of the same size as the coeffs array.
    '''
    pass

