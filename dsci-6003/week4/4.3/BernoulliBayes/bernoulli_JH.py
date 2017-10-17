# Put import statements here

__author__='Jonathan Hilgart'
import numpy as np
from collections import defaultdict
from collections import Counter

class BernoulliBayes(object):

    def __init__(self):
        self.prior = defaultdict(int)
        self.pvc = defaultdict(lambda : defaultdict(int))

    def fit(self,X,y):
        pass
        '''
        Input: 
            - X: (2d numpy array) Contains input data
            - y: (numpy array) Contains labels
        Ouput: 
            - None, fit model to input data
        '''
        # for each class c in C
            # count all documents in D belonging to that class, Nc
            # update the prior[c] with Nc
            # for each word v in V
                # count all docs in D containing v belonging to that class, Ncv
                # add in the count to the conditional probability table P(v, c) = (N_{cv} + 1)/(Nc + 2)
        # store P(v,c) and Priors
        unique_labels = np.unique(y)
        self.unique_labels = unique_labels
        total_vocab = np.shape(X)[1]
        self.total_vocab=total_vocab
        self.y=y
        y_copy = list(y)
        count_y = Counter(y_copy)
        for index,unique_class in enumerate(unique_labels): ## unique labels
                Ncv = 0
                Nc=Counter(y_copy)[unique_class]
                self.prior[unique_class]=Nc
                for v in range(total_vocab):
                    Ncv = sum(X[y==unique_class].T[v])
                    self.pvc[unique_class][v]= (Ncv +1) /(Nc+2)


    def predict(self,X):
        # For each point in X
            # for each class c in C
                    # initialize score[c] = log(prior[c])
                    # for all v in V:
                        # if v is 1:
                            # score[c] += log(P(v, c))
                        # else:
                            # score[c] += log(1 - P(v, c)
            # predict argmax(score[c])
        # Return predictions
        predictions = []
        for row_count,row in enumerate(X):
            score = defaultdict(int)
            for class_count,c in enumerate(self.unique_labels):
                score[c]=np.log(self.prior[c])
                for v in range(self.total_vocab):
                    if row[v] ==1:
                        score[c] += np.log(self.pvc[c][v])
                    else:
                        score[c] += np.log(1-self.pvc[c][v])
            predictions.append(np.argmax(list(score.values()),axis=0))
        return predictions








         