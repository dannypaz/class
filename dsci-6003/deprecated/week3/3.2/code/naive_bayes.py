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
        for label in y:
            if label in self.prior:
                self.prior[label] += 1
            else:
                self.prior[label] = 1

    def compute_likelihood(self, X, y):
        for label, row_features in zip(y, X):
            if label in self.per_feature_per_label:
                self.per_feature_per_label[label] += row_features
            else:
                self.per_feature_per_label[label] = row_features

            if label in self.feature_sum_per_label:
                self.feature_sum_per_label[label] += sum(row_features)
            else:
                self.feature_sum_per_label[label] = sum(row_features)

        for label, per_feature_per_label_arr in self.per_feature_per_label.iteritems():
            feature_sum_per_label = self.feature_sum_per_label[label]
            numerator = per_feature_per_label_arr + self.alpha
            denominator = feature_sum_per_label + self.alpha * self.p
            self.likelihood[label] = numerator / denominator

    def fit(self, X, y):
        self.p = X.shape[1]
        self.compute_prior(y)
        self.compute_likelihood(X, y)

    def predict(self, X):
        predictions = []
        for row in X:
            max_label = None
            max_value = None
            for label, prior in self.prior.iteritems():
                value = np.log(prior) + sum(row * np.log(self.likelihood[label]))
                if max_label is None:
                    max_label = label
                    max_value = value
                else:
                    if value > max_value:
                        max_label = label
                        max_value = value
            predictions.append(max_label)
        return predictions

    def score(self, X, y):
        return sum(self.predict(X) == y) / float(len(y))
