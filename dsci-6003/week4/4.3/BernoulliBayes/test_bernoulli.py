from bernoulli import BernoulliBayes
import numpy as np
from nose.tools import assert_equal
import nose

X = np.array([[1,0,1],
			  [1,0,0],
	 		  [0,1,0],
	 		  [1,1,0],
			  [0,1,1]])

y = np.array([0,0,1,1,1])

bb = BernoulliBayes()
bb.fit(X,y)

def test_priors():
	assert_equal(bb.prior[0],2)
	assert_equal(bb.prior[1],3)

def test_pvc():
	assert_equal(bb.pvc[0][0], 3./4)
	assert_equal(bb.pvc[0][1], 1./4)
	assert_equal(bb.pvc[0][2], 2./4)
	assert_equal(bb.pvc[1][0], 2./5)
	assert_equal(bb.pvc[1][1], 4./5)
	assert_equal(bb.pvc[1][2], 2./5)

def test_predict():
	assert_equal(sum(bb.predict(X)),3)

