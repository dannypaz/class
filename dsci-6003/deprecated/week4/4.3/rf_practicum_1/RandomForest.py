from DecisionTree import DecisionTree

class RandomForest(object):
    '''A Random Forest class'''

    def __init__(self, num_trees, num_features):
        '''
           num_trees:  number of trees to create in the forest:
        num_features:  the number of features to consider when choosing the
                           best split for each node of the decision trees
        '''
        self.num_trees = num_trees
        self.num_features = num_features
        self.forest = None

    def fit(self, X, y):
        '''
        X:  two dimensional numpy array representing feature matrix
                for test data
        y:  numpy array representing labels for test data
        '''
        self.forest = self.build_forest(X, y, self.num_trees, X.shape[0], \
                                        self.num_features)

    def build_forest(self, X, y, num_trees, num_samples, num_features):

        # * Return a list of num_trees DecisionTrees.

        pass

    def predict(self, X):

        '''
        Return a numpy array of the labels predicted for the given test data.
        '''

        # * Each one of the trees is allowed to predict on the same row of input data. The majority vote
        # is the output of the whole forest. This becomes a single prediction.

        pass

    def score(self, X, y):

        '''
        Return the accuracy of the Random Forest for the given test data.
        '''

        # * In this case you simply compute the accuracy formula as we have defined in class. Compare predicted y to
        # the actual input y.

        pass
