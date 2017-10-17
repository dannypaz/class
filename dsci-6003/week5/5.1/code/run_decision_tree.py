import pandas as pd
from itertools import izip
from DecisionTree import DecisionTree


def test_tree(filename):
    df = pd.read_csv(filename)
    y = df.pop('Result').values
    X = df.values
    print X
    
    tree = DecisionTree()
    tree.fit(X, y, df.columns)
    print tree
    print

    y_predict = tree.predict(X)
    print '%26s   %10s   %10s' % ("FEATURES", "ACTUAL", "PREDICTED")
    print '%26s   %10s   %10s' % ("----------", "----------", "----------")
    for features, true, predicted in izip(X, y, y_predict):
        print '%26s   %10s   %10s' % (str(features), str(true), str(predicted))


if __name__ == '__main__':
    test_tree('data/playgolf.csv')
