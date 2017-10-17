import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.base import clone


class AdaBoostBinaryClassifier(object):
    '''
    INPUT:
    - n_estimator (int)
      * The number of estimators to use in boosting
      * Default: 50

    - learning_rate (float)
      * Determines how fast the error would shrink
      * Lower learning rate means more accurate decision boundary,
        but slower to converge
      * Default: 1
    '''

    def __init__(self,
                 n_estimators=50,
                 learning_rate=1):

        self.base_estimator = DecisionTreeClassifier(max_depth=1)
        self.n_estimator = n_estimators
        self.learning_rate = learning_rate

        # Will be filled-in in the fit() step
        self.estimators_ = []
        self.estimator_weight_ = np.zeros(self.n_estimator, dtype=np.float)

    def fit(self, x, y):
        '''
        INPUT:
        - x: 2d numpy array, feature matrix
        - y: numpy array, labels

        Build the estimators for the AdaBoost estimator.
        '''

        # Initialize weights to 1 / n_samples
        sample_weight = np.ones(x.shape[0]) / x.shape[0]

        # Start boosting
        for i in xrange(self.n_estimator):
            estimator, sample_weight, estimator_weight = \
                self._boost(x, y, sample_weight)

            # Append estimator, sample_weights and error to lists
            self.estimators_.append(estimator)
            self.estimator_weight_[i] = estimator_weight


    def _boost(self, x, y, sample_weight):
        '''
        INPUT:
        - x: 2d numpy array, feature matrix
        - y: numpy array, labels
        - sample_weight: numpy array

        OUTPUT:
        - estimator: DecisionTreeClassifier
        - sample_weight: numpy array (updated weights)
        - estimator_weight: float (weight of estimator)

        Go through one iteration of the AdaBoost algorithm. Build one estimator.
        '''

        estimator = clone(self.base_estimator)

        # Fit according to sample weights, emphasizing certain data points
        estimator.fit(x, y, sample_weight=sample_weight)

        # Instances incorrectly classified
        incorrect = estimator.predict(x) != y

        # Error fraction
        estimator_error = np.sum(sample_weight * incorrect) / np.sum(sample_weight)

        # Update estimator weight
        estimator_weight = self.learning_rate * (np.log((1. - estimator_error) / estimator_error))

        # Update sample weight
        sample_weight *= np.exp(estimator_weight * incorrect)

        return estimator, sample_weight, estimator_weight

    def predict(self, x):
        '''
        INPUT:
        - x: 2d numpy array, feature matrix

        OUTPUT:
        - labels: numpy array of predictions (0 or 1)
        '''
        # get predictions
        predictions = np.array([estimator.predict(x) for estimator in self.estimators_])

        # negative predictions should be -1 instead of 0
        predictions[predictions == 0] = -1

        return np.dot(predictions.T, self.estimator_weight_) >= 0

    def score(self, x, y):
        '''
        INPUT:
        - x: 2d numpy array, feature matrix
        - y: numpy array, labels

        OUTPUT:
        - score: float (accuracy score between 0 and 1)
        '''

        y_predict = self.predict(x)
        return np.sum(y_predict == y) / float(len(y))

