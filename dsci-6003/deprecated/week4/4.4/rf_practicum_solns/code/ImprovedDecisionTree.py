import pandas as pd
import numpy as np
import math
from collections import Counter
from TreeNode import TreeNode


class ImprovedDecisionTree(object):
    '''
    A decision tree class.
    '''

    def __init__(self, impurity_criterion='entropy', leaf_size=None,
                 depth=None, same_ratio=None, error_threshold=None):
        '''
        Initialize an empty ImprovedDecisionTree.
        '''

        self.root = None  # root Node
        self.feature_names = None  # string names of features (for interpreting
                                   # the tree)
        self.categorical = None  # Boolean array of whether variable is
                                 # categorical (or continuous)
        self.impurity_criterion = self._entropy \
                                  if impurity_criterion == 'entropy' \
                                  else self._gini
        self.leaf_size = leaf_size
        self.depth = depth
        self.same_ratio = same_ratio
        self.error_threshold = error_threshold

    def fit(self, X, y, feature_names=None):
        '''
        INPUT:
            - X: 2d numpy array
            - y: 1d numpy array
            - feature_names: numpy array of strings
        OUTPUT: None
        Build the decision tree.
        X is a 2 dimensional array with each column being a feature and each
        row a data point.
        y is a 1 dimensional array with each value being the corresponding
        label.
        feature_names is an optional list containing the names of each of the
        features.
        '''

        if feature_names is None or len(feature_names) != X.shape[1]:
            self.feature_names = np.arange(X.shape[1])
        else:
            self.feature_names = feature_names

        # Create True/False array of whether the variable is categorical
        is_categorical = lambda x: isinstance(x, str) or \
                                   isinstance(x, bool) or \
                                   isinstance(x, unicode)
        self.categorical = np.vectorize(is_categorical)(X[0])

        self.root = self._build_tree(X, y)

    def _pre_prune(self, y, splits, depth):
        '''
        INPUT:
            - y: 1d numpy array
            - splits: tuple of numpy arrays
            - depth: int
        OUTPUT:
            - Boolean
        Checks pre-prunning parameters and return True/False if any stopping
        threshold has been reached.
        '''

        X1, y1, X2, y2 = splits

        if self.leaf_size is not None:
            if self.leaf_size >= X1.shape[0] or self.leaf_size >= X2.shape[0]:
                return True
        elif self.depth is not None and depth >= self.depth:
            return True
        elif self.same_ratio is not None:
            y1_ratio = Counter(y1).most_common(1) / float(y1.shape[0])
            y2_ratio = Counter(y2).most_common(1) / float(y2.shape[0])
            if y1_ratio >= self.same_ratio or y2_ratio >= self.same_ratio:
                return True
        elif self.error_threshold is not None:
            if self.error_threshold > self._information_gain(y, y1, y2):
                return True
        return False

    def _build_tree(self, X, y, depth=-1):
        '''
        INPUT:
            - X: 2d numpy array
            - y: 1d numpy array
        OUTPUT:
            - TreeNode
        Recursively build the decision tree. Return the root node.
        '''

        depth += 1

        node = TreeNode()
        index, value, splits = self._choose_split_index(X, y)
        
        if splits is not None:
            preprune = self._pre_prune(y, splits, depth)
        else:
            preprune = False

        if index is None or len(np.unique(y)) == 1 or preprune:
            node.leaf = True
            node.classes = Counter(y)
            node.name = node.classes.most_common(1)[0][0]
        else:
            X1, y1, X2, y2 = splits
            node.column = index
            node.name = self.feature_names[index]
            node.value = value
            node.categorical = self.categorical[index]
            node.left = self._build_tree(X1, y1, depth)
            node.right = self._build_tree(X2, y2, depth)
        return node

    def _entropy(self, y):
        '''
        INPUT:
            - y: 1d numpy array
        OUTPUT:
            - float
        Return the entropy of the array y.
        '''

        n = y.shape[0]
        summation = 0
        for c_i in np.unique(y):
            prob = sum(y == c_i) / float(n)
            summation += prob * np.log2(prob)
        return -summation

    def _gini(self, y):
        '''
        INPUT:
            - y: 1d numpy array
        OUTPUT:
            - float
        Return the gini impurity of the array y.
        '''

        n = y.shape[0]
        summation = 0
        for c_i in np.unique(y):
            prob = sum(y == c_i) / float(n)
            summation += prob**2
        return 1 - summation

    def _make_split(self, X, y, split_index, split_value):
        '''
        INPUT:
            - X: 2d numpy array
            - y: 1d numpy array
            - split_index: int (index of feature)
            - split_value: int/float/bool/str (value of feature)
        OUTPUT:
            - X1: 2d numpy array (feature matrix for subset 1)
            - y1: 1d numpy array (labels for subset 1)
            - X2: 2d numpy array (feature matrix for subset 2)
            - y2: 1d numpy array (labels for subset 2)
        Return the two subsets of the dataset achieved by the given feature and
        value to split on.
        Call the method like this:
        >>> X1, y1, X2, y2 = self._make_split(X, y, split_index, split_value)
        X1, y1 is a subset of the data.
        X2, y2 is the other subset of the data.
        '''

        if self.categorical[split_index]:
            idx = X[:, split_index] == split_value
        else:
            idx = X[:, split_index] < split_value
        return X[idx], y[idx], X[idx == False], y[idx == False]

    def _information_gain(self, y, y1, y2):
        '''
        INPUT:
            - y: 1d numpy array
            - y1: 1d numpy array (labels for subset 1)
            - y2: 1d numpy array (labels for subset 2)
        OUTPUT:
            - float
        Return the information gain of making the given split.
        Use self.impurity_criterion(y) rather than calling _entropy or _gini
        directly.
        '''

        n = y.shape[0]
        child_inf = 0
        for y_i in (y1, y2):
            child_inf += self.impurity_criterion(y_i) * y_i.shape[0] / float(n)
        return self.impurity_criterion(y) - child_inf

    def _choose_split_index(self, X, y):
        '''
        INPUT:
            - X: 2d numpy array
            - y: 1d numpy array
        OUTPUT:
            - index: int (index of feature)
            - value: int/float/bool/str (value of feature)
            - splits: (2d array, 1d array, 2d array, 1d array)
        Determine which feature and value to split on. Return the index and
        value of the optimal split along with the split of the dataset.
        Return None, None, None if there is no split which improves information
        gain.
        Call the method like this:
        >>> index, value, splits = self._choose_split_index(X, y)
        >>> X1, y1, X2, y2 = splits
        '''

        split_index, split_value, splits = None, None, None
        gain = 0
        for i in xrange(X.shape[1]):
            values = np.unique(X[:, i])
            if len(values) < 1:
                continue
            for value in values:
                X1, y1, X2, y2 = self._make_split(X, y, i, value)
                new_gain = self._information_gain(y, y1, y2)
                if new_gain > gain:
                    split_index = i
                    split_value = value
                    splits = (X1, y1, X2, y2)
                    gain = new_gain
        return split_index, split_value, splits

    def prune(self, X, y, node=None):
        '''
        INPUT:
            - X: 2d numpy array
            - y: 1d numpy array
            - node: TreeNode root
        OUTPUT:
            None
        Recursively checks for leaves and compares error rate before and after 
        merging the leaves.  If merged improves error rate, merge leaves.
        '''

        if node is None:
            node = self.root

        if not node.left.leaf:
            self.prune(X, y, node.left)

        if not node.right.leaf:
            self.prune(X, y, node.right)

        if node.left.leaf and node.right.leaf:
            leaf_y = self.predict(X)
            merged_classes = node.left.classes + node.right.classes
            merged_name = merged_classes.most_common(1)[0][0]
            merged_y = np.array([merged_name] * y.shape[0])
            leaf_score = sum(leaf_y == y) / float(y.shape[0])
            merged_score = sum(merged_y == y) / float(y.shape[0])

            if merged_score >= leaf_score:
                node.leaf = True
                node.classes = merged_classes
                node.name = merged_name
                node.left = None
                node.right = None

    def predict(self, X):
        '''
        INPUT:
            - X: 2d numpy array
        OUTPUT:
            - y: 1d numpy array
        Return an array of predictions for the feature matrix X.
        '''

        return np.apply_along_axis(self.root.predict_one, axis=1, arr=X)

    def __str__(self):
        '''
        Return string representation of the Decision Tree.
        '''

        return str(self.root)
