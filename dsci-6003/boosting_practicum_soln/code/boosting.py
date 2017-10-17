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
            # For each of n_estimators, boost
                # Append estimator, sample_weights and error to lists

        weights = np.ones(x.shape[0]) / x.shape[0]
        for m in range(1,self.n_estimator + 1):
            estimator, estimator_weight, weights = self._boost(x,y,weights)
            self.estimators_.append(estimator)
            self.estimator_weight_[m - 1] = estimator_weight




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
        estimator.fit(x,y,sample_weight = sample_weight)
        # Calculate instances incorrectly classified and store as incorrect
        incorrect = (y != estimator.predict(x)).astype(int)
        # calculate fraction of error as estimator_error
        estimator_error = sample_weight.dot(incorrect.T)/sample_weight.sum()
        # Update estimator weights
        alpha_m = np.log((1 - estimator_error)/estimator_error)

        # Update sample weights
        sample_weight = sample_weight * np.exp(alpha_m * incorrect)
        
        return estimator, alpha_m, sample_weight


    def predict(self, x):
        '''
        INPUT:
        - x: 2d numpy array, feature matrix

        OUTPUT:
        - labels: numpy array of predictions (0 or 1)
        '''

        # get predictions from tree family

        # set negative predictions to -1 instead of 0 (so we have -1 vs. 1)

        total = np.zeros(x.shape[0]).astype(float)
        for i,model in enumerate(self.estimators_):
            predictions = np.array([-1 if r == 0 else 1 for r in model.predict(x)])
            total += self.estimator_weight_[i] * predictions

        return [-1 if t < 0 else 1 for t in total]



    def score(self, x, y):
        '''
        INPUT:
        - x: 2d numpy array, feature matrix
        - y: numpy array, labels

        OUTPUT:
        - score: float (accuracy score between 0 and 1)
        '''


        # calculate score as usual
        pred = self.predict(x)
        y_adjusted = np.array([-1 if ry == 0 else ry for ry in y])
        return (y_adjusted == pred).sum()/float(len(y))
