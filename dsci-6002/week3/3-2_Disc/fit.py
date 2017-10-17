from scipy.optimize import minimize
from scipy.misc import factorial
from scipy.special import comb
import numpy as np

def fit_poisson(data):

    def poisson(k, lamb):
        """poisson pdf, parameter lamb is the fit parameter"""
        return (lamb**k/factorial(k)) * np.exp(-lamb)


    def negLogLikelihood(params, data):
        """ the negative log-Likelohood-Function"""
        lnl = - np.sum(np.log(poisson(data, params[0])))
        return lnl

    result = minimize(negLogLikelihood,  # function to minimize
                      x0=np.ones(1),     # start value
                      args=(data.values,),      # additional arguments for function
                      method='Powell',   # minimization method, see docs
                      )
    return result.x.flatten()[0]

def fit_negative_binomial(data):
    m = data.mean()[0] # pr / (1 - p)
    v = (np.sum((data - m)**2) / (len(data) - 1))[0] # m / (1 - p)
    p = 1 - m / v
    r = (m - m*p) / p
    return r, 1-p
