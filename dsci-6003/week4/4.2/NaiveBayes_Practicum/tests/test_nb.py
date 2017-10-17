from __future__ import division
import nose
from naive_bayes import NaiveBayes
from nose.tools import assert_equal, assert_not_equal
import numpy as np

X = ['a long document about fishing',
     'a book on fishing',
     'a book on knot-tying']
X = [x.split() for x in X]
y = np.array(['fishing', 'fishing', 'knot-tying'])
nb = NaiveBayes()
nb.fit(X, y)

def test_class_freq():
    assert nb.class_freq['fishing'] == 2
    assert nb.class_freq['knot-tying'] == 1

def test_class_counts():
    assert_equal(nb.class_counts['fishing'], 9)

def test_p_is_number_features():
    assert_equal(nb.p, 8)

def test_class_feature_counts():
    assert_equal(nb.class_feature_counts['fishing']['document'], 1)
    assert_equal(nb.class_feature_counts['knot-tying']['fishing'], 0)
    assert_equal(nb.class_feature_counts['fishing']['fishing'], 2)

def laplace(n, d, p):
    return (n + 1) / (d + 1 * p)

def test_predict():
    test_X = [["book"]]
    p = 8
    fishing_likelihood = sum((np.log(laplace(1, 9, p)),
                             np.log(2)))
    knot_tying_likelihood = sum((np.log(laplace(1, 4, p)),
                                np.log(1)))
    posts = nb.posteriors(test_X)
    preds = nb.predict(test_X)

    assert_equal(fishing_likelihood, posts[0]['fishing'])
    assert_equal(knot_tying_likelihood, posts[0]['knot-tying'])
    assert_equal(preds[0], 'fishing')
    assert_not_equal(preds[0], 'knot-tying')

def test_score():
    print(nb.posteriors(X))
    assert_equal(nb.score(X, y), 2./3)
