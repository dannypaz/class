from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble.partial_dependence import plot_partial_dependence
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#%pylab inline
from collections import Counter


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

        self.base_estimator = DecisionTreeClassifier(max_depth=1) ## create a decision tree
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
        sample_weights=[1/len(x) for _ in self.n_estimator]

        for i in range(self.n_estimator):
            estimator,sample_weight_i,estimator_weight = _boost(x,y,sample_weights)
            self.estimator_weight_[i]=estimator_weight
            self.estimators_[i]=estimator
            sample_weights = sample_weight_i



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

        # Calculate instances incorrectly classified and store as incorrect

        predict = estimator.predict(x)
        number_incorrectly_classified = 0

        for count,prediction in enumerate(predict):
            if prediction !=y[count]:
                number_incorrectly_classified+=1

        incorrect = estimator.predict(x)

        # calculate fraction of error as estimator_error

        estimator_error=(number_incorrectly_classified /len(y))

        # Update estimator weights

        estimator_weight = float(log((1-estimator_error)/estimator_error)) ##alpha

        # Update sample weights

        sample_weight_i =sample_weight* np.exp(estimator_weight * number_incorrectly_classified)

        return estimator,sample_weight_i,estimator_weight


    def predict(self, x):
        '''
        INPUT:
        - x: 2d numpy array, feature matrix

        OUTPUT:
        - labels: numpy array of predictions (0 or 1)
        '''

        # get predictions from tree family
        final_predictions = []

        for estimator_idx,estimator in enumerate(self.estimators_):
            predictions = estimator.predict(x)*self.estimator_weight_[i] ## predict given the estimator weight
            for i,item in enumerate(predictions):
                if item <0:
                    predictions[i]=-1
  
            final_predictions.append(predictions[i])

        predict = []

        for prediction_idx, prediction_list in enumerate(final_predictions):
            current_prediction = []
            for p in prediction_list[prediction_idx]: ##go through each prediction list, take all of the first, second , third ...etc predictions 
                current_prediction.append(p)
            predict.append(Counter(current_prediction).most_common(1)[0][0]) ## find the most common prediction

        return np.array(predict)


    def score(self, x, y):
        '''
        INPUT:
        - x: 2d numpy array, feature matrix
        - y: numpy array, labels

        OUTPUT:
        - score: float (accuracy score between 0 and 1)
        '''


        # calculate score as usual
        return (y-self.predict(x))/len(y)


