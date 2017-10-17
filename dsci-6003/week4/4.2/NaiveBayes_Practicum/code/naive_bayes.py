from __future__ import division
from collections import Counter, defaultdict
import numpy as np
import itertools
import operator

class NaiveBayes(object):
    def __init__(self, alpha=1.):
        """
        INPUT:
        -alpha: float, laplace smoothing constant.

        ATTRIBUTES:
        - class_counts: the number of samples per class; keys=labels
        - class_feature_counts: the number of samples per feature per label;
                               keys=labels, values=Counter with key=feature
        - class_freq: the frequency of each class in the data
        - p: the number of features
        """
        self.class_counts = defaultdict(int)
        self.class_feature_counts = defaultdict(Counter)
        self.class_freq = None
        self.alpha = float(alpha)
        self.p = None

    def _compute_likelihoods(self, X, y):
        '''
        INPUT:
        - X: List of list of tokens.
        - y: numpy array, labels

        OUTPUT: None

        Compute the word count for each class and the frequency of each feature
        per class.  (Compute class_counts and class_feature_counts).
        '''

        for idx,label in enumerate(y): ## go through each class, keys are the y labels
            self.class_counts[label] +=len(X[idx]) ## add in the size of the document
            self.class_feature_counts[label]+=Counter(X[idx]) 


    def fit(self, X, y):
        '''
        INPUT:
        - X: List of list of tokens.
        - y: numpy array, labels

        OUTPUT: None
        '''
        # Compute class frequency P(y)
        y_count = Counter(y)
        self.class_freq = Counter(y) # dictionary of class:probability


        # Compute number of features
        self.p = len(set(itertools.chain(*X)))

        # Compute likelihoods
        self._compute_likelihoods(X, y)

    def posteriors(self, X):
        '''
        INPUT:
        - X: List of list of tokens.

        OUTPUT:
        List of dictionaries with key=label, value=log(P(y)) + sum(log(P(x_i|y))).
        '''
        ### frequency of each label
        list_dicts = []
        current_dict = defaultdict(int)
        for idx,label in enumerate(self.class_counts.keys()):
            current_dict[label] = np.log(self.class_freq[label]/sum(self.class_freq.values())) +\
            sum( np.log([(self.class_feature_counts[label][i]+self.alpha) /(self.class_counts[label]+self.alpha*self.p) for i in X[idx]]))  ## get probability associated with a class                
        list_dicts.append(current_dict)
        return list_dicts

    def predict(self, X):
        """
        INPUT:
        - X: A list of lists of tokens.

        OUTPUT:
        - predictions: a numpy array with predicted labels.

        """
        #import operator
        #x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        #sorted_x = sorted(x.items(), key=operator.itemgetter(1))
        final_predictions = []
        for i in range(len(X)):
            temp= sorted(self.posteriors(X)[i].items(), key=operator.itemgetter(1),reverse=True) #sort the features for the current word
            for prediction in temp:
                final_predictions.append(prediction[0]) ## append the top feature
                break
        print(final_predictions, ' final predictions')
        return np.array(final_predictions)

    def score(self, X, y):
        '''
        INPUT:
        - X: List of list of tokens.
        - y: numpy array, labels

        OUTPUT:
        - accuracy: float between 0 and 1

        Calculate the accuracy, the percent predicted correctly.
        '''

        return np.mean(self.predict(X) == y)
