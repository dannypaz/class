import numpy as np

class NaiveBayes(object):

    def __init__(self, alpha=1):
        self.prior = {}
        self.per_feature_per_label = {}
        self.feature_sum_per_label = {}
        self.likelihood = {}
        self.posterior = {}
        self.alpha = alpha
        self.p = None

    def compute_prior(self, y):
        pass

    def compute_likelihood(self, X, y):
        pass

    def fit(self, X, y):
        self.p = X.shape[1]
        self.compute_prior(y)
        self.compute_likelihood(X, y)

    def predict(self, X):
        pass

    def score(self, X, y):
        pass
