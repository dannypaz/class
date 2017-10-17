import nose.tools as n
import numpy as np
from DecisionTree import DecisionTree as DT
from TreeNode import TreeNode as TN


def test_entropy():
    array = [1, 1, 2, 1, 2]
    # * use the above array as an argument to the _entropy method of DT
    # this is the actual value for the above array
    actual = 0.67301
    message = 'Entropy value for %r: Got %.2f. Should be %.2f' \
              % (array, result, actual)
    # * use a nose assert_almost_equal here with result actual and message


def test_gini():
    array = [1, 1, 2, 1, 2]
    # * use the above array as an argument to the _gini method of DT
   
    # this is the actual value for the above array
    actual = 0.48
    message = 'Gini value for %r: Got %.2f. Should be %.2f' \
              % (array, result, actual)
    # * use a nose assert_almost_equal as above


def fake_data():
    X = np.array([[1, 'bat'], [2, 'cat'], [2, 'rat'], [3, 'bat'], [3, 'bat']])
    y = np.array([1, 0, 1, 0, 1])
    X1 = np.array([[1, 'bat'], [3, 'bat'], [3, 'bat']])
    y1 = np.array([1, 0, 1])
    X2 = np.array([[2, 'cat'], [2, 'rat']])
    y2 = np.array([0, 1])
    return X, y, X1, y1, X2, y2


def test_make_split():
    # * use fake_data() to generate a new split
    
    # * set the split index = 1 and the value equal to 'bat'

    # * create a new decision tree
   
    # * assign the decision tree .categorical = [False,True]

    # * create a new make split here using the _make_split method (result = make_split)

    # set up a try-except loop here
    try:
        # * check to see that the split worked by assigning it to X1_result, y1_result, X2_result, y2_result = result

    except ValueError:
        # * if this fails use a nose assert_true statement
    
    actual = (X1, y1, X2, y2)
    message = '_make_split got results\n%r\nShould be\n%r' % (result, actual)
    
    # * use 4 nose ok_ statements to check that X1 = X1_result, y1=y1_result, etc


def test_information_gain():
    X, y, X1, y1, X2, y2 = fake_data()
    # * use the above generated data in the _information_gain method of a decision tree
    
    # this is the expected value of information gain
    actual = 0.01384
    message = 'Information gain for:\n%r, %r, %r:\nGot %.3f. Should be %.3f' \
              % (y, y1, y2, result, actual)

    # * use a nose assert_almost_equal here as above


def test_choose_split_index():
    # Here we generate fake data and set index and value to something we know
    X, y, X1, y1, X2, y2 = fake_data()
    index, value = 1, 'cat'

    # * create a new decision tree and set categorical to [False,True]

    # * use X and y in the new _choose_split_index

    # here we set up a new try-except
    try:
        # * set split_index, split_value, splits = result
    except ValueError:
        message = 'result not in correct form. Should be:\n' \
                  '    split_index, split_value, splits'
        # * use a nose assert_true statement - if False, then use message above
    message = 'choose split for data:\n%r\n%r\n' \
              'split index, split value should be: %r, %r\n' \
              'not: %r, %r' \
              % (X, y, index, value, split_index, split_value)
    # * use two nose eq_ methods here, one comparing split_index, index, message and one comparing split_value, value, message

def test_predict():
    # This is a handworked example for you to study
    root = TN()
    root.column = 1
    root.name = 'column 1'
    root.value = 'bat'
    root.left = TN()
    root.left.leaf = True
    root.left.name = "one"
    root.right = TN()
    root.right.leaf = True
    root.right.name = "two"
    data = [10, 'cat']
    result = root.predict_one(data)
    actual = "two"
    message = 'Predicted %r. Should be %r.\nTree:\n%r\ndata:\n%r' \
              % (result, actual, root, data)
    n.eq_(result, actual, message)

